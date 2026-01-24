import type { Skill } from '../types';
import { DownloadButton } from './DownloadButton';
import { hasDownload } from '../lib/downloads';

interface Props {
  skill: Skill;
  baseUrl: string;
}

export function SkillCard({ skill, baseUrl }: Props) {
  return (
    <a
      href={`${baseUrl}/skills/${skill.slug}`}
      className="group relative block rounded-xl overflow-hidden
                 bg-zinc-900/50 backdrop-blur-sm
                 border border-zinc-800/50
                 hover:border-emerald-500/30
                 transition-all duration-300 ease-out
                 hover:scale-[1.02] hover:-translate-y-1
                 hover:shadow-lg hover:shadow-emerald-500/5
                 focus:outline-none focus:ring-2 focus:ring-emerald-500"
      role="listitem"
    >
      {/* Gradient top accent */}
      <div className="absolute top-0 left-0 right-0 h-px bg-gradient-to-r from-transparent via-emerald-500/50 to-transparent opacity-0 group-hover:opacity-100 transition-opacity" />

      {/* Download button overlay */}
      {hasDownload(skill.slug) && (
        <div
          className="absolute top-3 right-3 opacity-0 group-hover:opacity-100 transition-opacity z-10"
          onClick={(e) => e.stopPropagation()}
        >
          <DownloadButton slug={skill.slug} baseUrl={baseUrl} variant="icon" />
        </div>
      )}

      <div className="p-5">
        <span className="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
          {skill.group}
        </span>
        <h3 className="text-white font-semibold mt-3 text-lg group-hover:text-emerald-50 transition-colors">
          {skill.name}
        </h3>
        <p className="text-zinc-400 text-sm mt-2 line-clamp-2 leading-relaxed">
          {skill.excerpt}
        </p>
      </div>
    </a>
  );
}
