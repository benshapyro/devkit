import { forwardRef } from 'react';

interface Props {
  value: string;
  onChange: (value: string) => void;
}

export const SearchInput = forwardRef<HTMLInputElement, Props>(
  ({ value, onChange }, ref) => {
    return (
      <div className="relative mb-6">
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
          ref={ref}
          type="search"
          value={value}
          onChange={(e) => onChange(e.target.value)}
          placeholder="Search skills..."
          className="w-full pl-12 pr-4 py-3
                     bg-white border border-[#E5E2D8]
                     rounded-xl text-[#0C0407] placeholder-[#A1A1A1]
                     focus:outline-none focus:ring-2 focus:ring-[#DB4545]/30 focus:border-[#DB4545]/30
                     transition-all duration-200"
          aria-label="Search skills"
        />
      {value && (
        <button
          type="button"
          onClick={() => onChange('')}
          className="absolute inset-y-0 right-0 pr-4 flex items-center text-[#A1A1A1] hover:text-[#0C0407] transition-colors"
          aria-label="Clear search"
        >
          <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      )}
    </div>
  );
  }
);

SearchInput.displayName = 'SearchInput';
