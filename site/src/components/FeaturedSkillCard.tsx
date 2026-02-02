import type { Skill } from '../types';

interface Props {
  skill: Skill;
  baseUrl: string;
  featured?: boolean;
}

export function FeaturedSkillCard({ skill, baseUrl, featured = false }: Props) {
  const skillUrl = `${baseUrl}/skills/${skill.slug}`;

  return (
    <a
      href={skillUrl}
      className={`group relative block overflow-hidden rounded-2xl
                  bg-white
                  border border-[#E5E2D8] hover:border-[#DB4545]/30
                  transition-all duration-300
                  ${featured ? 'row-span-2 col-span-2' : ''}`}
    >
      {/* Glow effect for featured */}
      {featured && (
        <div className="absolute inset-0 bg-gradient-to-br from-[#DB4545]/10 via-transparent to-transparent opacity-50" />
      )}

      <div className={`relative p-6 ${featured ? 'p-8' : 'p-6'} h-full flex flex-col`}>
        {/* Tagline */}
        {skill.tagline && (
          <span className={`text-[#DB4545] font-medium mb-2 ${featured ? 'text-lg' : 'text-sm'}`}>
            {skill.tagline}
          </span>
        )}

        {/* Name */}
        <h3 className={`font-display font-bold text-[#0C0407] group-hover:text-[#0C0407] transition-colors
                        ${featured ? 'text-3xl md:text-4xl' : 'text-xl'}`}>
          {skill.name}
        </h3>

        {/* Last updated date */}
        {skill.lastUpdated && (
          <p className={`mt-2 text-[#A1A1A1] ${featured ? 'text-sm' : 'text-xs'}`}>
            Updated {skill.lastUpdated}
          </p>
        )}

        {/* Description - only on featured */}
        {featured && (
          <p className="mt-4 text-[#6E7191] text-lg leading-relaxed line-clamp-3">
            {skill.excerpt}
          </p>
        )}

        {/* Role badges */}
        {skill.roles && skill.roles.length > 0 && (
          <div className={`flex flex-wrap gap-2 ${featured ? 'mt-6' : 'mt-4'}`}>
            {skill.roles.slice(0, featured ? 3 : 2).map(role => (
              <span
                key={role}
                className="px-2 py-1 text-xs bg-[#F2EFE4] text-[#6E7191] rounded-full"
              >
                {role}
              </span>
            ))}
          </div>
        )}

        {/* Arrow indicator */}
        <div className="mt-auto pt-4 flex items-center text-[#6E7191] group-hover:text-[#DB4545] transition-colors">
          <span className={`${featured ? 'text-base' : 'text-sm'}`}>
            Explore →
          </span>
        </div>
      </div>
    </a>
  );
}
