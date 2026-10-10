# Rebuild the presentation / 重建介绍素材

The core Skill remains Python standard-library only. This optional directory contains the Remotion source for the published film and case board. / 核心 Skill 仍仅依赖 Python 标准库；这里是可选的宣传素材工程。

## Render / 渲染

Use Node.js 20+ and an environment where Remotion can download/start Chrome Headless Shell. / 使用 Node.js 20+，环境需允许 Remotion 下载并启动无头浏览器。

```sh
cd motion
npm ci
npx tsc --noEmit
node render.mjs qa
node render.mjs films
```

Outputs are in `out/v3/`. The films are 1280×720, 30 FPS, 720 frames (24 s). The complete case boards are 1600×1040. / 视频输出为 24 秒、30 FPS；看板单独渲染完整状态，不截取过渡帧。

For live preview / 实时预览:

```sh
npm run studio
```

## Export for GitHub / 导出 GitHub 素材

FFmpeg is required for the GIF preview. Run the commands for both `zh` and `en`. / GIF 导出需要 FFmpeg；中英文分别执行。

```sh
ffmpeg -y -i out/v3/manager-zh.mp4 -c copy -movflags +faststart ../assets/readme/hero-zh.mp4
ffmpeg -y -i out/v3/manager-zh.mp4 -vf "fps=20,scale=800:450:flags=lanczos" -c:v libwebp_anim -lossless 0 -quality 82 -compression_level 6 -loop 0 -an ../assets/readme/hero-zh.webp
ffmpeg -y -i out/v3/manager-zh.mp4 -filter_complex "[0:v]fps=20,scale=800:450:flags=lanczos,split[a][b];[a]palettegen=max_colors=64:reserve_transparent=0[p];[b][p]paletteuse=dither=bayer:bayer_scale=4:diff_mode=rectangle" -loop 0 ../assets/readme/hero-zh.gif
```

Use frame 680 as `hero-zh.png` / `hero-en.png`; use the corresponding `*-board-*-0.png` as the case board. Animated WebP is the lighter default; GIF remains available. Keep WebP below 3 MiB and GIF below 6 MiB, both at 20 FPS. / 首页默认使用更小的动态 WebP，保留 GIF 下载；两者均保留 24 秒、20 FPS。MP4 保留 30 FPS 与 faststart；独立播放链接避免 GitHub 的 GIF 包装器覆盖目标。

## Content and checks / 内容与检查

- `src/story.json`: bilingual prompts, headlines and actual output filenames / 双语文案与真实交付文件名。
- `src/FilmV3.tsx`: frame-driven motion; six chapters with completed reading holds / 帧驱动动画、六段叙事与阅读停留。
- `src/CaseBoard.tsx`: complete case evidence, scope and limitations / 完整案例证据、口径和边界。
- `public/fonts/`: a bilingual Noto Sans SC variable subset, licensed under SIL OFL. When adding characters, rebuild the subset from the official font; verify glyph coverage. / 增字时需重建字体子集并核对缺字。
- `assets/readme/visual-manifest.json` (repository root): committed asset hashes, encoding and provenance. Update these measurements after rendering, then run `python scripts/check_presentation.py --probe` from the repository root. / 改动素材后更新实际哈希与测量结果，再执行检查。

The case footage illustrates the linked evidence. It is not a recording of an agent autonomously executing the complete workflow. / 案例画面用于解释已有证据，不冒充 Agent 自动执行全流程的实录。

Visual reference: [Art Director](https://github.com/NewenergyEric/art-director-skill). Original role-specific composition; navy, teal, mint and paper palette. / 各岗位采用原创排版和叙事，沿用参考的深蓝、青绿、薄荷绿与纸白风格。
