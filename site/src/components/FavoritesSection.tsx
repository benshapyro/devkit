import type { Skill } from '../types';
import { FeaturedSkillCard } from './FeaturedSkillCard';
import { FAVORITE_SKILLS } from '../lib/tags';

interface Props {
  skills: Skill[];
  baseUrl: string;
}

export function FavoritesSection({ skills, baseUrl }: Props) {
  // Get favorites in the specified order
  const favorites = FAVORITE_SKILLS
    .map(slug => skills.find(s => s.slug === slug))
    .filter((s): s is Skill => s !== undefined);

  if (favorites.length === 0) return null;

  const [featured, ...rest] = favorites;

  return (
    <section className="mb-16">
      {/* Section header with editorial styling */}
      <div className="flex items-center gap-4 mb-8">
        <h2 className="font-display text-2xl md:text-3xl font-bold text-[#0C0407]">
          Staff Picks
        </h2>
        <div className="flex-1 h-px bg-[#E5E2D8]" />
      </div>

      {/* Asymmetric grid */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-6">
        {/* Featured card (2x2) */}
        <FeaturedSkillCard
          skill={featured}
          baseUrl={baseUrl}
          featured={true}
        />

        {/* Remaining cards */}
        {rest.map(skill => (
          <FeaturedSkillCard
            key={skill.slug}
            skill={skill}
            baseUrl={baseUrl}
          />
        ))}
      </div>
    </section>
  );
}
