interface Props {
  groups: [string, number][];
  selected: string[];
  onToggle: (group: string) => void;
  onClear: () => void;
}

export function FilterSidebar({ groups, selected, onToggle, onClear }: Props) {
  return (
    <aside className="w-64 shrink-0 hidden md:block">
      <div className="sticky top-24">
        <div className="p-4 rounded-xl bg-zinc-900/50 border border-zinc-800/50">
          <div className="flex items-center justify-between mb-4 pb-3 border-b border-zinc-800/50">
            <h2 className="text-xs font-semibold text-zinc-400 uppercase tracking-wider">
              Categories
            </h2>
            {selected.length > 0 && (
              <button
                type="button"
                onClick={onClear}
                className="text-xs text-zinc-500 hover:text-white transition-colors"
              >
                Clear
              </button>
            )}
          </div>

          <div className="space-y-1" role="group" aria-label="Filter by category">
            {groups.map(([group, count]) => {
              const isChecked = selected.includes(group);
              return (
                <button
                  type="button"
                  key={group}
                  onClick={() => onToggle(group)}
                  className={`w-full flex items-center justify-between px-3 py-2.5 rounded-lg text-sm transition-all duration-150
                    ${isChecked
                      ? 'bg-emerald-500/10 text-emerald-400'
                      : 'text-zinc-400 hover:bg-zinc-800/50 hover:text-zinc-200'
                    }`}
                  aria-pressed={isChecked}
                >
                  <span className="truncate">{group}</span>
                  <span className={`ml-2 text-xs tabular-nums ${isChecked ? 'text-emerald-500/70' : 'text-zinc-600'}`}>
                    {count}
                  </span>
                </button>
              );
            })}
          </div>
        </div>
      </div>
    </aside>
  );
}
