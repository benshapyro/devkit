import type { Skill } from '../types';
import { DownloadButton } from './DownloadButton';
import { hasDownload } from '../lib/downloads';

interface Props {
  skill: Skill;
  baseUrl: string;
}

// Group to icon mapping (using simple geometric shapes)
const groupIcons: Record<string, string> = {
  'ai-automation': '◈',
  'business-strategy': '◆',
  'communications': '◇',
  'content-marketing': '▣',
  'data-documents': '▤',
  'design-ui': '◐',
  'development-tools': '⬡',
  'infrastructure-ops': '⬢',
  'internal-specialty': '◎',
  'marketing': '◉',
};

export function SkillCard({ skill, baseUrl }: Props) {
  const skillUrl = `${baseUrl}/skills/${skill.slug}`;
  const icon = groupIcons[skill.group] || '○';
  const displayRoles = skill.roles?.slice(0, 2) || [];
  const displayTasks = skill.tasks?.slice(0, 2) || [];

  return (
    <div
      className="group relative rounded-2xl overflow-hidden
                 bg-gradient-to-b from-zinc-900/80 to-zinc-900/40
                 border border-zinc-800/60
                 hover:border-zinc-700/80
                 transition-all duration-300 ease-out
                 hover:shadow-2xl hover:shadow-emerald-500/5"
    >
      {/* Download button overlay */}
      {hasDownload(skill.slug) && (
        <div className="absolute top-4 right-4 opacity-0 group-hover:opacity-100 group-focus-within:opacity-100 transition-opacity duration-200 z-10">
          <DownloadButton slug={skill.slug} baseUrl={baseUrl} variant="icon" />
        </div>
      )}

      <a
        href={skillUrl}
        aria-label={`View details for ${skill.name}`}
        className="block p-6 focus:outline-none focus:ring-2 focus:ring-emerald-500/50 focus:ring-inset rounded-2xl"
      >
        {/* Top accent line */}
        <div className="absolute top-0 inset-x-0 h-px bg-gradient-to-r from-transparent via-zinc-700/50 to-transparent" />

        {/* Hover glow */}
        <div className="absolute inset-0 bg-gradient-to-b from-emerald-500/[0.03] to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />

        <div className="relative">
          {/* Icon and group */}
          <div className="flex items-center gap-3 mb-3">
            <span className="text-2xl text-emerald-500/70 group-hover:text-emerald-400 transition-colors">
              {icon}
            </span>
            <span className="text-xs font-medium text-zinc-500 uppercase tracking-wider">
              {skill.group}
            </span>
          </div>

          {/* Title */}
          <h3 className="text-lg font-semibold text-zinc-100 group-hover:text-white transition-colors leading-snug">
            {skill.name}
          </h3>

          {/* Tagline (primary) or fallback to excerpt */}
          {skill.tagline ? (
            <p className="mt-2 text-sm text-zinc-400 font-medium">
              {skill.tagline}
            </p>
          ) : (
            <p className="mt-2 text-sm text-zinc-400 line-clamp-2 leading-relaxed">
              {skill.excerpt}
            </p>
          )}

          {/* Role and task badges */}
          {(displayRoles.length > 0 || displayTasks.length > 0) && (
            <div className="mt-4 flex flex-wrap gap-1.5">
              {displayRoles.map(role => (
                <span
                  key={role}
                  className="px-2 py-0.5 text-xs bg-zinc-800/70 text-zinc-400 rounded-full"
                >
                  {role}
                </span>
              ))}
              {displayTasks.map(task => (
                <span
                  key={task}
                  className="px-2 py-0.5 text-xs bg-emerald-500/10 text-emerald-400/80 rounded-full"
                >
                  {task}
                </span>
              ))}
            </div>
          )}

          {/* Bottom arrow indicator */}
          <div className="mt-4 flex items-center text-sm text-zinc-500 group-hover:text-emerald-400 transition-colors">
            <span className="opacity-0 -translate-x-2 group-hover:opacity-100 group-hover:translate-x-0 transition-all duration-200">
              View details →
            </span>
          </div>
        </div>
      </a>
    </div>
  );
}
