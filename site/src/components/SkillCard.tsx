import type { Skill } from '../types';

interface Props {
  skill: Skill;
  baseUrl: string;
}

export function SkillCard({ skill, baseUrl }: Props) {
  return (
    <a
      href={`${baseUrl}/skills/${skill.slug}`}
      className="block rounded-lg border border-zinc-800 bg-zinc-900 p-4
                 hover:border-zinc-600 hover:bg-zinc-800/50
                 transition-all duration-200
                 focus:outline-none focus:ring-2 focus:ring-emerald-500"
      role="listitem"
    >
      <span className="text-xs text-emerald-400 uppercase tracking-wide font-medium">
        {skill.group}
      </span>
      <h3 className="text-white font-medium mt-1 text-lg">
        {skill.name}
      </h3>
      <p className="text-zinc-400 text-sm mt-2 line-clamp-2">
        {skill.excerpt}
      </p>
    </a>
  );
}
