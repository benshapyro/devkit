import type { Skill } from '../types';

interface Props {
  skills: Skill[];
  baseUrl: string;
}

export function CompareView({ skills, baseUrl }: Props) {
  // Determine grid columns based on number of skills
  const gridCols = skills.length === 2 ? 'grid-cols-1 md:grid-cols-2' : 'grid-cols-1 md:grid-cols-2 lg:grid-cols-3';

  return (
    <div className="animate-fade-in">
      <h2 className="text-lg font-semibold text-[#6E7191] mb-4">
        Comparing {skills.length} skills
      </h2>

      <div className={`grid gap-6 ${gridCols}`} role="list" aria-label="Skill comparison">
        {skills.map(skill => (
          <article
            key={skill.slug}
            className="bg-white border border-[#E5E2D8] rounded-xl p-6 flex flex-col h-full hover:border-[#D1CEC4] transition-colors"
            role="listitem"
          >
            {/* Header */}
            <div className="mb-4">
              <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-zinc-800 text-zinc-400 mb-3">
                {skill.group}
              </span>
              <h3 className="text-xl font-semibold text-[#0C0407]">
                {skill.name}
              </h3>
            </div>

            {/* Description */}
            <p className="text-zinc-400 text-sm leading-relaxed flex-grow">
              {skill.description}
            </p>

            {/* Footer with license and link */}
            <div className="mt-6 pt-4 border-t border-[#E5E2D8]/50 flex items-center justify-between">
              {skill.license && (
                <span className="text-xs text-[#A1A1A1]">
                  License: {skill.license}
                </span>
              )}
              <a
                href={`${baseUrl}/skills/${skill.slug}`}
                className="inline-flex items-center gap-1.5 text-sm text-[#DB4545] hover:text-[#DB4545] transition-colors ml-auto"
              >
                View details
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                </svg>
              </a>
            </div>
          </article>
        ))}
      </div>

      {/* Comparison table for quick reference */}
      <div className="mt-8 overflow-x-auto">
        <table className="w-full text-sm" role="table">
          <thead>
            <tr className="border-b border-[#E5E2D8]">
              <th scope="col" className="text-left py-3 px-4 text-[#A1A1A1] font-medium">Attribute</th>
              {skills.map(skill => (
                <th key={skill.slug} scope="col" className="text-left py-3 px-4 text-[#6E7191] font-medium">
                  {skill.name}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            <tr className="border-b border-[#E5E2D8]/50">
              <td className="py-3 px-4 text-[#A1A1A1]">Group</td>
              {skills.map(skill => (
                <td key={skill.slug} className="py-3 px-4 text-[#6E7191]">
                  <span className="inline-flex items-center px-2 py-0.5 rounded-full text-xs bg-zinc-800 text-zinc-400">
                    {skill.group}
                  </span>
                </td>
              ))}
            </tr>
            <tr className="border-b border-[#E5E2D8]/50">
              <td className="py-3 px-4 text-[#A1A1A1]">License</td>
              {skills.map(skill => (
                <td key={skill.slug} className="py-3 px-4 text-[#6E7191]">
                  {skill.license || <span className="text-zinc-600">Not specified</span>}
                </td>
              ))}
            </tr>
            <tr>
              <td className="py-3 px-4 text-[#A1A1A1]">Details</td>
              {skills.map(skill => (
                <td key={skill.slug} className="py-3 px-4">
                  <a
                    href={`${baseUrl}/skills/${skill.slug}`}
                    className="text-[#DB4545] hover:text-[#DB4545] transition-colors"
                  >
                    View full documentation
                  </a>
                </td>
              ))}
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}
