import type { Skill } from '../types';
import { DownloadButton } from './DownloadButton';
import { hasDownload } from '../lib/downloads';
import { OUTPUT_TYPES } from '../lib/tags';

interface Props {
  skill: Skill;
  baseUrl: string;
  isFavorite: boolean;
  onToggleFavorite: () => void;
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

export function SkillCard({ skill, baseUrl, isFavorite, onToggleFavorite }: Props) {
  const skillUrl = `${baseUrl}/skills/${skill.slug}`;
  const icon = groupIcons[skill.group] || '○';
  const displayRoles = skill.roles?.slice(0, 2) || [];
  const displayTasks = skill.tasks?.slice(0, 2) || [];

  return (
    <div
      className="group relative rounded-2xl overflow-hidden
                 bg-white
                 border border-[#E5E2D8]
                 hover:border-[#D1CEC4]
                 transition-all duration-300 ease-out
                 hover:shadow-2xl hover:shadow-[#DB4545]/5"
    >
      {/* Star button for favorites */}
      <button
        type="button"
        onClick={(e) => {
          e.preventDefault();
          e.stopPropagation();
          onToggleFavorite();
        }}
        className={`absolute top-4 p-2 rounded-full transition-all duration-200 z-10
          ${hasDownload(skill.slug) ? 'right-14' : 'right-4'}
          ${isFavorite
            ? 'text-amber-400 bg-amber-500/20'
            : 'text-[#A1A1A1] hover:text-amber-400 opacity-0 group-hover:opacity-100 group-focus-within:opacity-100'
          } focus-visible:opacity-100 focus-visible:ring-2 focus-visible:ring-amber-500/50`}
        aria-label={isFavorite ? 'Remove from favorites' : 'Add to favorites'}
        aria-pressed={isFavorite}
      >
        <svg
          className="w-5 h-5"
          fill={isFavorite ? 'currentColor' : 'none'}
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"
          />
        </svg>
      </button>

      {/* Download button overlay */}
      {hasDownload(skill.slug) && (
        <div className="absolute top-4 right-4 opacity-0 group-hover:opacity-100 group-focus-within:opacity-100 transition-opacity duration-200 z-10">
          <DownloadButton slug={skill.slug} baseUrl={baseUrl} variant="icon" />
        </div>
      )}

      <a
        href={skillUrl}
        aria-label={`View details for ${skill.name}`}
        className="block p-6 focus:outline-none focus:ring-2 focus:ring-[#DB4545]/50 focus:ring-inset rounded-2xl"
      >
        {/* Top accent line */}
        <div className="absolute top-0 inset-x-0 h-px bg-gradient-to-r from-transparent via-[#E5E2D8] to-transparent" />

        {/* Hover glow */}
        <div className="absolute inset-0 bg-gradient-to-b from-[#DB4545]/[0.03] to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />

        <div className="relative">
          {/* Icon and group */}
          <div className="flex items-center gap-3 mb-3">
            <span className="text-2xl text-[#DB4545]/70 group-hover:text-[#DB4545] transition-colors" aria-hidden="true">
              {icon}
            </span>
            <span className="text-xs font-medium text-[#6E7191] uppercase tracking-wider">
              {skill.group}
            </span>
            {/* Output type indicator */}
            {skill.outputType && OUTPUT_TYPES[skill.outputType] && (
              <span
                className="text-sm text-[#6E7191]"
                title={OUTPUT_TYPES[skill.outputType].label}
                aria-label={`Produces: ${OUTPUT_TYPES[skill.outputType].label}`}
              >
                <span aria-hidden="true">{OUTPUT_TYPES[skill.outputType].emoji}</span>
              </span>
            )}
          </div>

          {/* Title */}
          <h3 className="text-lg font-semibold text-[#0C0407] group-hover:text-[#0C0407] transition-colors leading-snug">
            {skill.name}
          </h3>

          {/* Last updated date */}
          {skill.lastUpdated && (
            <p className="mt-1 text-xs text-[#A1A1A1]">
              Updated {skill.lastUpdated}
            </p>
          )}

          {/* Tagline (primary) or fallback to excerpt */}
          {skill.tagline ? (
            <p className="mt-2 text-sm text-[#6E7191] font-medium">
              {skill.tagline}
            </p>
          ) : (
            <p className="mt-2 text-sm text-[#6E7191] line-clamp-2 leading-relaxed">
              {skill.excerpt}
            </p>
          )}

          {/* Role and task badges */}
          {(displayRoles.length > 0 || displayTasks.length > 0) && (
            <div className="mt-4 flex flex-wrap gap-1.5">
              {displayRoles.map(role => (
                <span
                  key={role}
                  className="px-2 py-0.5 text-xs bg-[#F2EFE4] text-[#6E7191] rounded-full"
                >
                  {role}
                </span>
              ))}
              {displayTasks.map(task => (
                <span
                  key={task}
                  className="px-2 py-0.5 text-xs bg-[#DB4545]/10 text-[#DB4545] rounded-full"
                >
                  {task}
                </span>
              ))}
            </div>
          )}

          {/* Example prompt */}
          {skill.examplePrompt && (
            <p className="mt-3 text-xs text-[#A1A1A1] italic truncate" title={skill.examplePrompt}>
              Try: "{skill.examplePrompt}"
            </p>
          )}

          {/* Bottom arrow indicator */}
          <div className="mt-4 flex items-center text-sm text-[#6E7191] group-hover:text-[#DB4545] transition-colors">
            <span className="opacity-0 -translate-x-2 group-hover:opacity-100 group-hover:translate-x-0 transition-all duration-200">
              View details →
            </span>
          </div>
        </div>
      </a>
    </div>
  );
}
