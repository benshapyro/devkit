interface Props {
  groups: [string, number][];
  selected: string[];
  onToggle: (group: string) => void;
  onClear: () => void;
}

export function FilterSidebar({ groups, selected, onToggle, onClear }: Props) {
  return (
    <aside className="w-56 shrink-0">
      <fieldset className="border-0 p-0 m-0">
        <legend className="text-sm font-semibold text-zinc-300 uppercase tracking-wide mb-3">
          Groups
        </legend>

        <button
          onClick={onClear}
          className="text-sm text-zinc-500 hover:text-zinc-300 mb-4 transition-colors"
          type="button"
        >
          Clear filters
        </button>

        <div className="space-y-2" role="group" aria-label="Filter by group">
          {groups.map(([group, count]) => {
            const id = `filter-${group.replace(/\s+/g, '-').toLowerCase()}`;
            const isChecked = selected.includes(group);

            return (
              <label
                key={group}
                htmlFor={id}
                className="flex items-center gap-2 cursor-pointer text-sm group/item"
              >
                <input
                  type="checkbox"
                  id={id}
                  checked={isChecked}
                  onChange={() => onToggle(group)}
                  className="w-4 h-4 rounded border-zinc-600 bg-zinc-800
                           text-emerald-500 focus:ring-emerald-500 focus:ring-offset-zinc-900
                           cursor-pointer"
                />
                <span className={`transition-colors ${isChecked ? 'text-white' : 'text-zinc-400 group-hover/item:text-zinc-300'}`}>
                  {group}
                </span>
                <span className="text-zinc-600 ml-auto">{count}</span>
              </label>
            );
          })}
        </div>
      </fieldset>
    </aside>
  );
}
