import {Config} from '@remotion/cli/config';

Config.setOverwriteOutput(true);
Config.setCodec('h264');
Config.setVideoImageFormat('jpeg');
Config.setPixelFormat('yuv420p');
Config.setConcurrency(4);
