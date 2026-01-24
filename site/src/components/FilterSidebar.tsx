interface Props {
  groups: [string, number][];
  selected: string[];
  onToggle: (group: string) => void;
  onClear: () => void;
}

export function FilterSidebar({ groups, selected, onToggle, onClear }: Props) {
  return (
    <aside className="w-60 shrink-0">
      <div className="sticky top-24">
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-sm font-semibold text-zinc-300 uppercase tracking-wide">
            Filter by Group
          </h2>
          {selected.length > 0 && (
            <button
              type="button"
              onClick={onClear}
              className="text-xs text-zinc-500 hover:text-emerald-400 transition-colors"
            >
              Clear all
            </button>
          )}
        </div>

        <div className="space-y-1.5" role="group" aria-label="Filter by group">
          {groups.map(([group, count]) => {
            const isChecked = selected.includes(group);
            return (
              <button
                type="button"
                key={group}
                onClick={() => onToggle(group)}
                className={`w-full flex items-center justify-between px-3 py-2 rounded-lg text-sm transition-all duration-200
                  ${isChecked
                    ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/30'
                    : 'bg-zinc-900/50 text-zinc-400 border border-transparent hover:bg-zinc-800/50 hover:text-zinc-300'
                  }`}
                aria-pressed={isChecked}
              >
                <span>{group}</span>
                <span className={`text-xs px-1.5 py-0.5 rounded ${isChecked ? 'bg-emerald-500/20' : 'bg-zinc-800'}`}>
                  {count}
                </span>
              </button>
            );
          })}
        </div>
      </div>
    </aside>
  );
}
