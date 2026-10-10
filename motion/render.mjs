import {bundle} from '@remotion/bundler';
import {getCompositions, renderMedia, renderStill, openBrowser} from '@remotion/renderer';
import {mkdir} from 'node:fs/promises';
import path from 'node:path';

const mode=process.argv[2]||'qa';
const output=path.resolve('out/v3');
await mkdir(output,{recursive:true});
const serveUrl=await bundle({entryPoint:path.resolve('src/index.ts'),publicDir:path.resolve('public')});
const browser=await openBrowser('chrome');
try {
  const compositions=await getCompositions(serveUrl,{puppeteerInstance:browser});
  for(const composition of compositions){
    if(process.argv[3]&&!composition.id.startsWith(process.argv[3]))continue;
    const board=composition.id.includes('-board-');
    if(mode==='qa'){
      for(const frame of board?[0]:[70,218,360,480,600,680]){
        const out=path.join(output,`${composition.id}-${frame}.png`);
        await renderStill({composition,serveUrl,frame,output:out,puppeteerInstance:browser,imageFormat:'png',overwrite:true});
        console.log('QA',composition.id,frame);
      }
    } else if(mode==='films'&&!board){
      await renderMedia({composition,serveUrl,outputLocation:path.join(output,`${composition.id}.mp4`),codec:'h264',crf:21,pixelFormat:'yuv420p',imageFormat:'png',concurrency:3,puppeteerInstance:browser,overwrite:true});
      console.log('FILM',composition.id);
    }
  }
}finally{await browser.close({silent:true});}
