interface Props {
  value: string;
  onChange: (value: string) => void;
}

export function SearchInput({ value, onChange }: Props) {
  return (
    <div className="mb-6">
      <label htmlFor="skill-search" className="sr-only">
        Search skills by name or description
      </label>
      <input
        type="search"
        id="skill-search"
        placeholder="Search skills..."
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="w-full px-4 py-3 bg-zinc-900 border border-zinc-800 rounded-lg
                   text-white placeholder-zinc-500
                   focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent
                   transition-colors"
        aria-label="Search skills by name or description"
      />
    </div>
  );
}
