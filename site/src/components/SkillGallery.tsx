import { useState, useMemo, useEffect, useRef } from 'react';
import type { Skill } from '../types';
import { useUrlFilters } from '../hooks/useUrlFilters';
import { useDebouncedValue } from '../hooks/useDebouncedValue';
import { SearchInput } from './SearchInput';
import { FilterSidebar } from './FilterSidebar';
import { MobileFilterDrawer } from './MobileFilterDrawer';
import { SkillCard } from './SkillCard';
import { ErrorBoundary } from './ErrorBoundary';

interface Props {
  skills: Skill[];
  baseUrl: string;
}

function SkillGalleryInner({ skills, baseUrl }: Props) {
  const { filters, setFilters } = useUrlFilters();
  const [searchInput, setSearchInput] = useState(filters.search);
  const [isFilterDrawerOpen, setIsFilterDrawerOpen] = useState(false);
  const debouncedSearch = useDebouncedValue(searchInput, 300);
  const searchInputRef = useRef<HTMLInputElement>(null);

  // Sync debounced search to URL
  useEffect(() => {
    setFilters({ search: debouncedSearch });
  }, [debouncedSearch, setFilters]);

  // Keyboard shortcut: Cmd+K (Mac) or Ctrl+K (Windows/Linux) to focus search
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        searchInputRef.current?.focus();
      }
    };

    document.addEventListener('keydown', handleKeyDown);
    return () => document.removeEventListener('keydown', handleKeyDown);
  }, []);

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
        {/* Mobile filter button - only visible on mobile */}
        <div className="md:hidden mb-4">
          <button
            type="button"
            onClick={() => setIsFilterDrawerOpen(true)}
            className="flex items-center gap-2 px-4 py-2.5 bg-zinc-800/50 border border-zinc-700/50 rounded-lg text-sm text-zinc-300 hover:bg-zinc-800 transition-colors"
          >
            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z" />
            </svg>
            Filters
            {filters.groups.length > 0 && (
              <span className="bg-emerald-500 text-white text-xs px-1.5 rounded-full">
                {filters.groups.length}
              </span>
            )}
          </button>
        </div>

        <SearchInput ref={searchInputRef} value={searchInput} onChange={setSearchInput} />

        {/* Screen reader announcement */}
        <div role="status" aria-live="polite" aria-atomic="true" className="sr-only">
          {filteredSkills.length} skill{filteredSkills.length !== 1 ? 's' : ''} found
        </div>

        {/* Results summary bar */}
        <div className="flex items-center justify-between mb-6 pb-4 border-b border-zinc-800/50">
          <p className="text-sm text-zinc-400">
            Showing <span className="text-white font-medium">{filteredSkills.length}</span> of {skills.length} skills
            {filters.groups.length > 0 && (
              <span className="ml-2 text-zinc-500">
                in {filters.groups.length} group{filters.groups.length !== 1 ? 's' : ''}
              </span>
            )}
          </p>
          {(filters.search || filters.groups.length > 0) && (
            <button
              type="button"
              onClick={clearFilters}
              className="text-sm text-zinc-500 hover:text-emerald-400 transition-colors"
            >
              Reset filters
            </button>
          )}
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
            {filteredSkills.map((skill, index) => (
              <div
                key={skill.slug}
                className="animate-fade-in-up opacity-0"
                style={{ animationDelay: `${Math.min(index * 50, 500)}ms` }}
              >
                <SkillCard skill={skill} baseUrl={baseUrl} />
              </div>
            ))}
          </div>
        )}
      </div>

      <MobileFilterDrawer
        isOpen={isFilterDrawerOpen}
        onClose={() => setIsFilterDrawerOpen(false)}
        groups={groups}
        selected={filters.groups}
        onToggle={toggleGroup}
        onClear={clearFilters}
      />
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
