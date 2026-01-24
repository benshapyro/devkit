import type { Hook } from '../types';

interface Props {
  hook: Hook;
  baseUrl: string;
}

// Event type to icon mapping
const eventIcons: Record<string, string> = {
  PreToolUse: '⚡',
  PostToolUse: '⚡',
  UserPromptSubmit: '⌨',
  PermissionRequest: '🔒',
  Notification: '🔔',
  Stop: '⏹',
  SubagentStop: '⏹',
  PreCompact: '📦',
  SessionStart: '▶',
  SessionEnd: '◼',
};

export function HookCard({ hook, baseUrl }: Props) {
  const hookUrl = `${baseUrl}/hooks/${hook.slug}`;
  const icon = eventIcons[hook.event] || '⚡';

  return (
    <div
      className="group relative rounded-2xl overflow-hidden
                 bg-gradient-to-b from-zinc-900/80 to-zinc-900/40
                 border border-zinc-800/60
                 hover:border-zinc-700/80
                 transition-all duration-300 ease-out
                 hover:shadow-2xl hover:shadow-amber-500/5"
    >
      <a
        href={hookUrl}
        aria-label={`View details for ${hook.name}`}
        className="block p-6 focus:outline-none focus:ring-2 focus:ring-amber-500/50 focus:ring-inset rounded-2xl"
      >
        {/* Top accent line */}
        <div className="absolute top-0 inset-x-0 h-px bg-gradient-to-r from-transparent via-zinc-700/50 to-transparent" />

        {/* Hover glow */}
        <div className="absolute inset-0 bg-gradient-to-b from-amber-500/[0.03] to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />

        <div className="relative">
          {/* Icon and event type */}
          <div className="flex items-center gap-3 mb-4">
            <span className="text-2xl text-amber-500/70 group-hover:text-amber-400 transition-colors">
              {icon}
            </span>
            <span className="text-xs font-medium text-zinc-500 uppercase tracking-wider">
              {hook.event}
            </span>
          </div>

          {/* Title */}
          <h3 className="text-lg font-semibold text-zinc-100 group-hover:text-white transition-colors leading-snug">
            {hook.name}
          </h3>

          {/* Description */}
          <p className="mt-3 text-sm text-zinc-400 line-clamp-2 leading-relaxed">
            {hook.description}
          </p>

          {/* Matcher badge if present */}
          {hook.matcher && (
            <div className="mt-4">
              <span className="inline-flex items-center px-2 py-1 rounded text-xs font-mono bg-zinc-800/50 text-zinc-400 border border-zinc-700/50">
                {hook.matcher}
              </span>
            </div>
          )}

          {/* Bottom arrow indicator */}
          <div className="mt-4 flex items-center text-sm text-zinc-500 group-hover:text-amber-400 transition-colors">
            <span className="opacity-0 -translate-x-2 group-hover:opacity-100 group-hover:translate-x-0 transition-all duration-200">
              View details →
            </span>
          </div>
        </div>
      </a>
    </div>
  );
}
