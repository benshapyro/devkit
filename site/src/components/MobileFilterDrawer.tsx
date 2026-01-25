import { ROLE_TAGS, TASK_TAGS } from '../lib/tags';

interface Props {
  isOpen: boolean;
  onClose: () => void;
  groups: [string, number][];
  selectedGroups: string[];
  selectedRoles: string[];
  selectedTasks: string[];
  onToggleGroup: (group: string) => void;
  onToggleRole: (role: string) => void;
  onToggleTask: (task: string) => void;
  onClear: () => void;
  favoritesOnly: boolean;
  favoritesCount: number;
  onToggleFavorites: () => void;
}

export function MobileFilterDrawer({
  isOpen,
  onClose,
  groups,
  selectedGroups,
  selectedRoles,
  selectedTasks,
  onToggleGroup,
  onToggleRole,
  onToggleTask,
  onClear,
  favoritesOnly,
  favoritesCount,
  onToggleFavorites,
}: Props) {
  // Don't render if closed
  if (!isOpen) return null;

  const totalSelected = selectedGroups.length + selectedRoles.length + selectedTasks.length + (favoritesOnly ? 1 : 0);

  return (
    <div className="fixed inset-0 z-50 md:hidden">
      {/* Backdrop */}
      <div
        className="absolute inset-0 bg-black/60 backdrop-blur-sm"
        onClick={onClose}
        aria-hidden="true"
      />

      {/* Drawer - slides up from bottom */}
      <div className="absolute bottom-0 left-0 right-0 bg-white rounded-t-2xl max-h-[80vh] overflow-y-auto">
        {/* Header */}
        <div className="sticky top-0 bg-white p-4 border-b border-[#E5E2D8] flex items-center justify-between">
          <h2 className="font-semibold text-[#0C0407]">Filters</h2>
          <div className="flex items-center gap-2">
            {totalSelected > 0 && (
              <button
                type="button"
                onClick={onClear}
                className="text-sm text-[#6E7191] hover:text-[#0C0407] transition-colors"
              >
                Clear all
              </button>
            )}
            <button
              type="button"
              onClick={onClose}
              className="p-2 text-[#6E7191] hover:text-[#0C0407] transition-colors"
              aria-label="Close filters"
            >
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
        </div>

        <div className="p-4 space-y-6">
          {/* Favorites toggle */}
          {favoritesCount > 0 && (
            <section aria-label="Filter by favorites">
              <button
                type="button"
                onClick={onToggleFavorites}
                className={`w-full flex items-center justify-between px-4 py-3 rounded-xl text-sm transition-all
                  ${favoritesOnly
                    ? 'bg-amber-500/20 text-amber-400 border border-amber-500/30'
                    : 'bg-white text-[#6E7191] border border-[#E5E2D8]'
                  }`}
                aria-pressed={favoritesOnly}
              >
                <span className="flex items-center gap-2">
                  <span role="img" aria-label="Star">⭐</span>
                  <span>My Favorites</span>
                </span>
                <span className="text-xs tabular-nums">
                  {favoritesCount}
                </span>
              </button>
            </section>
          )}

          {/* Roles Section */}
          <section>
            <h3 className="text-xs font-medium text-[#6E7191] uppercase tracking-wider mb-3">
              I am a...
            </h3>
            <div className="flex flex-wrap gap-2" role="group" aria-label="Filter by role">
              {ROLE_TAGS.map(role => {
                const isChecked = selectedRoles.includes(role);
                return (
                  <button
                    type="button"
                    key={role}
                    onClick={() => onToggleRole(role)}
                    className={`px-3 py-1.5 rounded-full text-sm transition-all
                      ${isChecked
                        ? 'bg-[#DB4545]/20 text-[#DB4545] border border-[#DB4545]/30'
                        : 'bg-white text-[#6E7191] border border-[#E5E2D8] hover:bg-[#F2EFE4]'
                      }`}
                    aria-pressed={isChecked}
                  >
                    {role}
                  </button>
                );
              })}
            </div>
          </section>

          {/* Tasks Section */}
          <section>
            <h3 className="text-xs font-medium text-[#6E7191] uppercase tracking-wider mb-3">
              I want to...
            </h3>
            <div className="flex flex-wrap gap-2" role="group" aria-label="Filter by task">
              {TASK_TAGS.map(task => {
                const isChecked = selectedTasks.includes(task);
                return (
                  <button
                    type="button"
                    key={task}
                    onClick={() => onToggleTask(task)}
                    className={`px-3 py-1.5 rounded-full text-sm transition-all
                      ${isChecked
                        ? 'bg-[#DB4545]/20 text-[#DB4545] border border-[#DB4545]/30'
                        : 'bg-white text-[#6E7191] border border-[#E5E2D8] hover:bg-[#F2EFE4]'
                      }`}
                    aria-pressed={isChecked}
                  >
                    {task}
                  </button>
                );
              })}
            </div>
          </section>

          {/* Categories Section */}
          <section>
            <h3 className="text-xs font-medium text-[#6E7191] uppercase tracking-wider mb-3">
              Categories
            </h3>
            <div className="space-y-1" role="group" aria-label="Filter by category">
              {groups.map(([group, count]) => {
                const isChecked = selectedGroups.includes(group);
                return (
                  <button
                    type="button"
                    key={group}
                    onClick={() => onToggleGroup(group)}
                    className={`w-full flex items-center justify-between px-3 py-2.5 rounded-lg text-sm transition-all
                      ${isChecked
                        ? 'bg-[#DB4545]/10 text-[#DB4545]'
                        : 'text-[#6E7191] hover:bg-[#F2EFE4]'
                      }`}
                    aria-pressed={isChecked}
                  >
                    <span>{group}</span>
                    <span className={`text-xs tabular-nums ${isChecked ? 'text-[#DB4545]/70' : 'text-[#A1A1A1]'}`}>
                      {count}
                    </span>
                  </button>
                );
              })}
            </div>
          </section>
        </div>

        {/* Footer with show results button */}
        <div className="sticky bottom-0 bg-white p-4 border-t border-[#E5E2D8]">
          <button
            type="button"
            onClick={onClose}
            className="w-full py-3 bg-[#DB4545] hover:bg-[#c43d3d] text-white font-medium rounded-xl transition-colors"
          >
            Show Results
            {totalSelected > 0 && (
              <span className="ml-2 text-white">
                ({totalSelected} filter{totalSelected !== 1 ? 's' : ''})
              </span>
            )}
          </button>
        </div>
      </div>
    </div>
  );
}
