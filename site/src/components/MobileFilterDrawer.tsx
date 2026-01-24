interface Props {
  isOpen: boolean;
  onClose: () => void;
  groups: [string, number][];
  selected: string[];
  onToggle: (group: string) => void;
  onClear: () => void;
}

export function MobileFilterDrawer({ isOpen, onClose, groups, selected, onToggle, onClear }: Props) {
  // Don't render if closed
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 md:hidden">
      {/* Backdrop */}
      <div
        className="absolute inset-0 bg-black/60 backdrop-blur-sm"
        onClick={onClose}
        aria-hidden="true"
      />

      {/* Drawer - slides up from bottom */}
      <div className="absolute bottom-0 left-0 right-0 bg-zinc-900 rounded-t-2xl max-h-[70vh] overflow-y-auto">
        {/* Header */}
        <div className="sticky top-0 bg-zinc-900 p-4 border-b border-zinc-800 flex items-center justify-between">
          <h2 className="font-semibold text-white">Filters</h2>
          <div className="flex items-center gap-2">
            {selected.length > 0 && (
              <button
                type="button"
                onClick={onClear}
                className="text-sm text-zinc-500 hover:text-white transition-colors"
              >
                Clear all
              </button>
            )}
            <button
              type="button"
              onClick={onClose}
              className="p-2 text-zinc-400 hover:text-white transition-colors"
              aria-label="Close filters"
            >
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
        </div>

        {/* Filter buttons - reuse same structure as FilterSidebar */}
        <div className="p-4 space-y-1" role="group" aria-label="Filter by category">
          {groups.map(([group, count]) => {
            const isChecked = selected.includes(group);
            return (
              <button
                type="button"
                key={group}
                onClick={() => onToggle(group)}
                className={`w-full flex items-center justify-between px-3 py-3 rounded-lg text-sm transition-all
                  ${isChecked
                    ? 'bg-emerald-500/10 text-emerald-400'
                    : 'text-zinc-400 hover:bg-zinc-800/50'
                  }`}
                aria-pressed={isChecked}
              >
                <span>{group}</span>
                <span className={`text-xs tabular-nums ${isChecked ? 'text-emerald-500/70' : 'text-zinc-600'}`}>
                  {count}
                </span>
              </button>
            );
          })}
        </div>

        {/* Footer with show results button */}
        <div className="sticky bottom-0 bg-zinc-900 p-4 border-t border-zinc-800">
          <button
            type="button"
            onClick={onClose}
            className="w-full py-3 bg-emerald-500 hover:bg-emerald-400 text-white font-medium rounded-xl transition-colors"
          >
            Show Results
          </button>
        </div>
      </div>
    </div>
  );
}
