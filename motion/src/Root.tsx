import React from 'react';
import {Composition, Folder} from 'remotion';
import {FilmV3} from './FilmV3';
import {CaseBoard} from './CaseBoard';
import type {Lang, Role} from './data';

const FPS = 30;
const DURATION = 24 * FPS;

const Film: React.FC<{role: Role; lang: Lang}> = ({role, lang}) => (
  <FilmV3 role={role} lang={lang} />
);

export const Root: React.FC = () => {
  const roles: Role[] = ['manager'];
  const langs: Lang[] = ['en', 'zh'];

  return (
    <>
      {roles.map((role) => (
        <Folder name={role} key={role}>
          {langs.map((lang)=><Composition key={`${role}-board-${lang}`} id={`${role}-board-${lang}`} component={CaseBoard} defaultProps={{role,lang}} durationInFrames={1} fps={30} width={1600} height={1040}/>)}
          {langs.map((lang) => (
            <Composition
              key={`${role}-${lang}`}
              id={`${role}-${lang}`}
              component={Film}
              defaultProps={{role, lang}}
              durationInFrames={DURATION}
              fps={FPS}
              width={1280}
              height={720}
            />
          ))}
        </Folder>
      ))}
    </>
  );
};
