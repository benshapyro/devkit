import { useState, useMemo, useEffect } from 'react';
import type { Skill } from '../types';
import { useUrlFilters } from '../hooks/useUrlFilters';
import { useDebouncedValue } from '../hooks/useDebouncedValue';
import { SearchInput } from './SearchInput';
import { FilterSidebar } from './FilterSidebar';
import { SkillCard } from './SkillCard';
import { ErrorBoundary } from './ErrorBoundary';

interface Props {
  skills: Skill[];
  baseUrl: string;
}

function SkillGalleryInner({ skills, baseUrl }: Props) {
  const { filters, setFilters } = useUrlFilters();
  const [searchInput, setSearchInput] = useState(filters.search);
  const debouncedSearch = useDebouncedValue(searchInput, 300);

  // Sync debounced search to URL
  useEffect(() => {
    setFilters({ search: debouncedSearch });
  }, [debouncedSearch, setFilters]);

  // Extract groups with counts
  const groups = useMemo(() => {
    const counts = new Map<string, number>();
    skills.forEach(s => counts.set(s.group, (counts.get(s.group) || 0) + 1));
    return Array.from(counts.entries()).sort((a, b) => a[0].localeCompare(b[0]));
  }, [skills]);

  // Filter skills
  const filteredSkills = useMemo(() => {
    return skills.filter(skill => {
      const searchLower = filters.search.toLowerCase();
      const matchesSearch = !filters.search ||
        skill.name.toLowerCase().includes(searchLower) ||
        skill.description.toLowerCase().includes(searchLower);

      const matchesGroup = filters.groups.length === 0 ||
        filters.groups.includes(skill.group);

      return matchesSearch && matchesGroup;
    });
  }, [skills, filters]);

  const toggleGroup = (group: string) => {
    setFilters({
      groups: filters.groups.includes(group)
        ? filters.groups.filter(g => g !== group)
        : [...filters.groups, group],
    });
  };

  const clearFilters = () => {
    setSearchInput('');
    setFilters({ groups: [], search: '' });
  };

  return (
    <div className="flex gap-8">
      <FilterSidebar
        groups={groups}
        selected={filters.groups}
        onToggle={toggleGroup}
        onClear={clearFilters}
      />

      <div className="flex-1">
        <SearchInput value={searchInput} onChange={setSearchInput} />

        {/* Screen reader announcement */}
        <div role="status" aria-live="polite" aria-atomic="true" className="sr-only">
          {filteredSkills.length} skill{filteredSkills.length !== 1 ? 's' : ''} found
        </div>

        {filteredSkills.length === 0 ? (
          <p className="text-zinc-400 text-center py-12">
            No skills match your filters.
          </p>
        ) : (
          <div
            role="list"
            aria-label="Skills"
            className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4"
          >
            {filteredSkills.map(skill => (
              <SkillCard key={skill.slug} skill={skill} baseUrl={baseUrl} />
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export function SkillGallery(props: Props) {
  return (
    <ErrorBoundary>
      <SkillGalleryInner {...props} />
    </ErrorBoundary>
  );
}
