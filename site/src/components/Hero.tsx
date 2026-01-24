interface Props {
  skillCount: number;
}

export function Hero({ skillCount }: Props) {
  return (
    <section className="relative py-24 px-8 overflow-hidden">
      {/* Decorative grid pattern */}
      <div
        aria-hidden="true"
        className="absolute inset-0 opacity-[0.02]"
        style={{
          backgroundImage: `linear-gradient(rgba(255,255,255,0.1) 1px, transparent 1px),
                           linear-gradient(90deg, rgba(255,255,255,0.1) 1px, transparent 1px)`,
          backgroundSize: '64px 64px',
        }}
      />

      {/* Gradient orb */}
      <div
        aria-hidden="true"
        className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-emerald-500/10 rounded-full blur-[128px] pointer-events-none"
      />

      <div className="relative z-10 max-w-4xl mx-auto text-center">
        {/* Badge */}
        <div
          role="status"
          aria-live="polite"
          className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-sm font-medium mb-8"
        >
          <span
            aria-hidden="true"
            className="w-2 h-2 rounded-full bg-emerald-400 motion-safe:animate-pulse"
          />
          {skillCount} skills available
        </div>

        <h1 className="text-5xl md:text-7xl font-bold tracking-tight">
          <span className="bg-gradient-to-b from-white via-zinc-100 to-zinc-400 bg-clip-text text-transparent">
            Devkit Skills
          </span>
          <br />
          <span className="text-zinc-500">Gallery</span>
        </h1>

        <p className="mt-6 text-lg md:text-xl text-zinc-400 max-w-2xl mx-auto leading-relaxed">
          Portable skills for agentic CLI tools. Browse, search, and download
          production-ready capabilities for Claude Code and beyond.
        </p>

        {/* Keyboard shortcut hint */}
        <div
          role="note"
          aria-label="Use Command+K keyboard shortcut to search"
          className="mt-8 flex items-center justify-center gap-2 text-sm text-zinc-500"
        >
          <kbd className="px-2 py-1 rounded bg-zinc-800/50 border border-zinc-700/50 font-mono text-xs">⌘</kbd>
          <kbd className="px-2 py-1 rounded bg-zinc-800/50 border border-zinc-700/50 font-mono text-xs">K</kbd>
          <span>to search</span>
        </div>
      </div>
    </section>
  );
}
