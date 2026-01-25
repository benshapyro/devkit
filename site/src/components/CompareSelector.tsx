import { useState, useEffect, useRef, useMemo } from 'react';
import type { Skill } from '../types';
import { CompareView } from './CompareView';

interface Props {
  skills: Skill[];
  baseUrl: string;
}

export function CompareSelector({ skills, baseUrl }: Props) {
  const [selected, setSelected] = useState<string[]>([]);
  const [search, setSearch] = useState('');
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  // Read from URL on mount
  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const skillsParam = params.get('skills');
    if (skillsParam) {
      const validSlugs = skillsParam
        .split(',')
        .filter(s => skills.some(sk => sk.slug === s))
        .slice(0, 3);
      setSelected(validSlugs);
    }
  }, [skills]);

  // Update URL when selection changes
  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    if (selected.length > 0) {
      params.set('skills', selected.join(','));
    } else {
      params.delete('skills');
    }
    const newUrl = selected.length > 0
      ? `${window.location.pathname}?${params}`
      : window.location.pathname;
    window.history.replaceState({}, '', newUrl);
  }, [selected]);

  // Close dropdown when clicking outside
  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        setIsDropdownOpen(false);
      }
    };

    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  // Filter skills based on search
  const filteredSkills = useMemo(() => {
    if (!search) return skills;
    const searchLower = search.toLowerCase();
    return skills.filter(s =>
      s.name.toLowerCase().includes(searchLower) ||
      s.group.toLowerCase().includes(searchLower)
    );
  }, [skills, search]);

  const toggleSkill = (slug: string) => {
    if (selected.includes(slug)) {
      setSelected(selected.filter(s => s !== slug));
    } else if (selected.length < 3) {
      setSelected([...selected, slug]);
    }
  };

  const removeSkill = (slug: string) => {
    setSelected(selected.filter(s => s !== slug));
  };

  const selectedSkills = useMemo(() => {
    return selected
      .map(slug => skills.find(s => s.slug === slug))
      .filter((s): s is Skill => s !== undefined);
  }, [selected, skills]);

  const handleSearchFocus = () => {
    setIsDropdownOpen(true);
  };

  const handleSearchChange = (value: string) => {
    setSearch(value);
    setIsDropdownOpen(true);
  };

  const handleSelectSkill = (slug: string) => {
    toggleSkill(slug);
    setSearch('');
    setIsDropdownOpen(false);
    inputRef.current?.focus();
  };

  return (
    <div>
      {/* Selection area */}
      <div className="mb-8">
        <div ref={dropdownRef} className="relative">
          {/* Search input */}
          <div className="relative">
            <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
              <svg
                className="w-5 h-5 text-[#A1A1A1]"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={1.5}
                  d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                />
              </svg>
            </div>
            <input
              ref={inputRef}
              type="search"
              value={search}
              onChange={(e) => handleSearchChange(e.target.value)}
              onFocus={handleSearchFocus}
              placeholder="Search skills to compare..."
              className="w-full md:w-96 pl-12 pr-4 py-3
                         bg-white border border-[#E5E2D8]
                         rounded-xl text-[#0C0407] placeholder-[#A1A1A1]
                         focus:outline-none focus:ring-2 focus:ring-[#DB4545]/30 focus:border-[#DB4545]/30
                         transition-all duration-200"
              aria-label="Search skills to compare"
              aria-expanded={isDropdownOpen}
              aria-controls="skill-dropdown"
            />
          </div>

          {/* Skill list dropdown */}
          {isDropdownOpen && (
            <div
              id="skill-dropdown"
              className="absolute z-10 mt-2 w-full md:w-96 bg-white border border-[#E5E2D8] rounded-xl max-h-64 overflow-y-auto shadow-xl"
              role="listbox"
              aria-label="Available skills"
            >
              {filteredSkills.length === 0 ? (
                <p className="p-4 text-sm text-[#A1A1A1]">No skills match your search.</p>
              ) : (
                filteredSkills.slice(0, 15).map(skill => {
                  const isSelected = selected.includes(skill.slug);
                  const isDisabled = selected.length >= 3 && !isSelected;

                  return (
                    <button
                      key={skill.slug}
                      type="button"
                      onClick={() => !isDisabled && handleSelectSkill(skill.slug)}
                      className={`w-full p-3 text-left transition-colors flex items-center justify-between
                        ${isSelected ? 'bg-[#DB4545]/10' : 'hover:bg-[#F2EFE4]'}
                        ${isDisabled ? 'opacity-50 cursor-not-allowed' : 'cursor-pointer'}
                      `}
                      disabled={isDisabled}
                      role="option"
                      aria-selected={isSelected}
                    >
                      <div>
                        <span className="text-[#0C0407]">{skill.name}</span>
                        <span className="text-xs text-[#A1A1A1] ml-2">{skill.group}</span>
                      </div>
                      {isSelected && (
                        <svg className="w-4 h-4 text-[#DB4545]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                        </svg>
                      )}
                    </button>
                  );
                })
              )}
            </div>
          )}
        </div>

        {/* Selected skills pills */}
        <div className="flex flex-wrap items-center gap-2 mt-4" role="list" aria-label="Selected skills">
          {selectedSkills.map(skill => (
            <span
              key={skill.slug}
              className="px-3 py-1.5 bg-[#DB4545]/10 text-[#DB4545] border border-[#DB4545]/20 rounded-full text-sm flex items-center gap-2"
              role="listitem"
            >
              {skill.name}
              <button
                type="button"
                onClick={() => removeSkill(skill.slug)}
                className="hover:text-[#DB4545] transition-colors"
                aria-label={`Remove ${skill.name} from comparison`}
              >
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </span>
          ))}
          {selected.length < 3 && (
            <span className="text-sm text-[#A1A1A1]">
              {selected.length === 0
                ? 'Select up to 3 skills'
                : `Select ${3 - selected.length} more${selected.length < 2 ? ' (minimum 2)' : ''}`}
            </span>
          )}
        </div>
      </div>

      {/* Screen reader announcement */}
      <div role="status" aria-live="polite" aria-atomic="true" className="sr-only">
        {selected.length} skill{selected.length !== 1 ? 's' : ''} selected for comparison
      </div>

      {/* Comparison view - only show when 2+ skills selected */}
      {selectedSkills.length >= 2 ? (
        <CompareView skills={selectedSkills} baseUrl={baseUrl} />
      ) : (
        <div className="text-center py-16 bg-[#F2EFE4] border border-[#E5E2D8] rounded-xl">
          <svg className="w-16 h-16 mx-auto text-[#A1A1A1] mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
          </svg>
          <p className="text-[#6E7191] text-lg">Select at least 2 skills to compare</p>
          <p className="text-[#A1A1A1] text-sm mt-2">Use the search above to find and add skills</p>
        </div>
      )}
    </div>
  );
}
