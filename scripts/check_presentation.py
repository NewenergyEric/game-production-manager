#!/usr/bin/env python3
"""Verify committed presentation bytes, GIF timing, and optional MP4 encoding."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import struct
import subprocess


def gif_info(data: bytes) -> tuple[int, int, list[int]]:
    if data[:6] not in (b"GIF87a", b"GIF89a"):
        raise ValueError("Not a GIF")
    width, height = struct.unpack_from("<HH", data, 6)
    packed = data[10]
    pos = 13 + (3 * 2 ** ((packed & 7) + 1) if packed & 128 else 0)
    delays: list[int] = []
    delay = 0

    def skip_blocks(offset: int) -> int:
        while data[offset]:
            offset += 1 + data[offset]
        return offset + 1

    while pos < len(data):
        tag = data[pos]
        pos += 1
        if tag == 0x3B:
            return width, height, delays
        if tag == 0x21:
            label = data[pos]
            pos += 1
            if label == 0xF9:
                delay = int.from_bytes(data[pos + 2:pos + 4], "little") * 10
            pos = skip_blocks(pos)
        elif tag == 0x2C:
            packed = data[pos + 8]
            pos += 9
            if packed & 128:
                pos += 3 * 2 ** ((packed & 7) + 1)
            pos = skip_blocks(pos + 1)
            delays.append(delay)
            delay = 0
        else:
            raise ValueError(f"Unexpected GIF block: {tag}")
    raise ValueError("Missing GIF trailer")


def webp_info(data):
    if data[:4] != b'RIFF' or data[8:12] != b'WEBP': raise ValueError('Not WebP')
    pos=12; width=height=0; delays=[]
    while pos+8 <= len(data):
        kind=data[pos:pos+4]; size=int.from_bytes(data[pos+4:pos+8],'little'); payload=data[pos+8:pos+8+size]
        if len(payload)!=size: raise ValueError('Truncated WebP chunk')
        if kind==b'VP8X': width=1+int.from_bytes(payload[4:7],'little');height=1+int.from_bytes(payload[7:10],'little')
        if kind==b'ANMF': delays.append(int.from_bytes(payload[12:15],'little'))
        pos+=8+size+(size%2)
    return width,height,delays


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--probe", action="store_true", help="Also validate MP4s with ffprobe")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / "assets/readme/visual-manifest.json").read_text(encoding="utf-8"))
    errors: list[str] = []
    for name, expected in manifest["assets"].items():
        path = root / name
        try:
            data = path.read_bytes()
            if hashlib.sha256(data).hexdigest() != expected["sha256"]:
                raise ValueError("SHA-256 mismatch")
            if len(data) != expected["bytes"]:
                raise ValueError("Byte count mismatch")
            if path.suffix == ".gif":
                width, height, delays = gif_info(data)
                if (width, height) != (800, 450) or len(delays) != 480 or set(delays) != {50}:
                    raise ValueError(f"Expected 800×450, 480 frames, 50 ms each; got {width}×{height}, {len(delays)} frames, delays {set(delays)}")
                if len(data) > 6 * 1024 * 1024:
                    raise ValueError("GIF exceeds the 6 MiB preview budget")
            elif path.suffix == '.webp':
                width,height,delays=webp_info(data)
                if (width,height)!=(800,450) or len(delays)!=480 or set(delays)!={50}:
                    raise ValueError(f'WebP timing/dimensions mismatch: {width}x{height}, {len(delays)}, {set(delays)}')
                if len(data)>3*1024*1024: raise ValueError('WebP exceeds 3 MiB budget')
            elif path.suffix == ".png":
                if data[:8] != b"\x89PNG\r\n\x1a\n" or list(struct.unpack_from(">II", data, 16)) != expected["dimensions"]:
                    raise ValueError("PNG dimensions mismatch")
            elif path.suffix == '.mp4':
                pos=0; atoms=[]
                while pos+8<=len(data):
                    size=int.from_bytes(data[pos:pos+4],'big');kind=data[pos+4:pos+8];header=8
                    if size==1: size=int.from_bytes(data[pos+8:pos+16],'big');header=16
                    if size==0: size=len(data)-pos
                    if size<header: raise ValueError('Invalid MP4 atom')
                    atoms.append(kind);pos+=size
                if b'moov' not in atoms or b'mdat' not in atoms or atoms.index(b'moov')>atoms.index(b'mdat'): raise ValueError('MP4 is missing faststart metadata')
            if path.suffix == ".mp4" and args.probe:
                result = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=codec_name,width,height,r_frame_rate,nb_frames,duration", "-of", "json", str(path)], check=True, capture_output=True, text=True)
                stream = json.loads(result.stdout)["streams"][0]
                if (stream["codec_name"], stream["width"], stream["height"], stream["r_frame_rate"], stream["nb_frames"]) != ("h264", 1280, 720, "30/1", "720") or abs(float(stream["duration"]) - 24) > .01:
                    raise ValueError(f"MP4 encoding mismatch: {stream}")
            print(f"PASS {name}")
        except (OSError, ValueError, IndexError, KeyError, struct.error, subprocess.CalledProcessError) as exc:
            errors.append(f"FAIL {name}: {exc}")
    if errors:
        print("\n".join(errors))
        return 1
    print("Presentation verified: bilingual, 24 s, faststart MP4 / 20 FPS GIF and WebP.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
