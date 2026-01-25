import { ROLE_TAGS, TASK_TAGS } from '../lib/tags';

interface Props {
  groups: [string, number][];
  selectedGroups: string[];
  selectedRoles: string[];
  selectedTasks: string[];
  favoritesOnly: boolean;
  favoritesCount: number;
  onToggleGroup: (group: string) => void;
  onToggleRole: (role: string) => void;
  onToggleTask: (task: string) => void;
  onToggleFavorites: () => void;
  onClear: () => void;
}

export function FilterSidebar({
  groups,
  selectedGroups,
  selectedRoles,
  selectedTasks,
  favoritesOnly,
  favoritesCount,
  onToggleGroup,
  onToggleRole,
  onToggleTask,
  onToggleFavorites,
  onClear,
}: Props) {
  const hasFilters = selectedGroups.length > 0 || selectedRoles.length > 0 || selectedTasks.length > 0;

  return (
    <aside className="w-64 shrink-0 hidden md:block">
      <div className="sticky top-24 space-y-6">
        {/* Favorites toggle - only show if user has favorites */}
        {favoritesCount > 0 && (
          <section className="mb-8" aria-label="Filter by favorites">
            <button
              type="button"
              onClick={onToggleFavorites}
              className={`w-full flex items-center justify-between px-3 py-2.5 rounded-lg text-sm transition-all
                ${favoritesOnly
                  ? 'bg-amber-500/20 text-amber-400 border border-amber-500/30'
                  : 'bg-zinc-800/50 text-zinc-400 border border-zinc-700/50 hover:bg-zinc-800'
                }`}
              aria-pressed={favoritesOnly}
            >
              <span className="flex items-center gap-2">
                <span role="img" aria-label="Star">⭐</span>
                <span>My Favorites</span>
              </span>
              <span className={`text-xs tabular-nums ${favoritesOnly ? 'text-amber-500/70' : 'text-zinc-600'}`}>
                {favoritesCount}
              </span>
            </button>
          </section>
        )}

        {/* Roles section */}
        <div className="p-4 rounded-xl bg-zinc-900/50 border border-zinc-800/50">
          <h2 className="text-xs font-semibold text-zinc-400 uppercase tracking-wider mb-4 pb-3 border-b border-zinc-800/50">
            I am a...
          </h2>
          <div className="space-y-1" role="group" aria-label="Filter by role">
            {ROLE_TAGS.map(role => {
              const isChecked = selectedRoles.includes(role);
              return (
                <button
                  type="button"
                  key={role}
                  onClick={() => onToggleRole(role)}
                  className={`w-full flex items-center px-3 py-2 rounded-lg text-sm transition-all duration-150
                    ${isChecked
                      ? 'bg-emerald-500/10 text-emerald-400'
                      : 'text-zinc-400 hover:bg-zinc-800/50 hover:text-zinc-200'
                    }`}
                  aria-pressed={isChecked}
                >
                  <span className="truncate">{role}</span>
                </button>
              );
            })}
          </div>
        </div>

        {/* Tasks section */}
        <div className="p-4 rounded-xl bg-zinc-900/50 border border-zinc-800/50">
          <h2 className="text-xs font-semibold text-zinc-400 uppercase tracking-wider mb-4 pb-3 border-b border-zinc-800/50">
            I want to...
          </h2>
          <div className="space-y-1" role="group" aria-label="Filter by task">
            {TASK_TAGS.map(task => {
              const isChecked = selectedTasks.includes(task);
              return (
                <button
                  type="button"
                  key={task}
                  onClick={() => onToggleTask(task)}
                  className={`w-full flex items-center px-3 py-2 rounded-lg text-sm transition-all duration-150
                    ${isChecked
                      ? 'bg-emerald-500/10 text-emerald-400'
                      : 'text-zinc-400 hover:bg-zinc-800/50 hover:text-zinc-200'
                    }`}
                  aria-pressed={isChecked}
                >
                  <span className="truncate">{task}</span>
                </button>
              );
            })}
          </div>
        </div>

        {/* Categories section (collapsed by default) */}
        <details className="p-4 rounded-xl bg-zinc-900/50 border border-zinc-800/50">
          <summary className="text-xs font-semibold text-zinc-400 uppercase tracking-wider cursor-pointer">
            Categories ({groups.length})
          </summary>
          <div className="mt-4 space-y-1" role="group" aria-label="Filter by category">
            {groups.map(([group, count]) => {
              const isChecked = selectedGroups.includes(group);
              return (
                <button
                  type="button"
                  key={group}
                  onClick={() => onToggleGroup(group)}
                  className={`w-full flex items-center justify-between px-3 py-2 rounded-lg text-sm transition-all duration-150
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
        </details>

        {/* Clear all button */}
        {hasFilters && (
          <button
            type="button"
            onClick={onClear}
            className="w-full px-4 py-2 text-sm text-zinc-500 hover:text-white transition-colors"
          >
            Clear all filters
          </button>
        )}
      </div>
    </aside>
  );
}
