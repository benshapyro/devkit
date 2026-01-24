interface Props {
  skillCount: number;
}

export function Hero({ skillCount }: Props) {
  return (
    <section className="relative py-20 px-8 text-center">
      <div className="relative z-10 max-w-3xl mx-auto">
        <h1 className="text-5xl md:text-6xl font-bold tracking-tight bg-gradient-to-r from-white via-zinc-200 to-zinc-400 bg-clip-text text-transparent">
          Devkit Skills Gallery
        </h1>
        <p className="mt-6 text-xl text-zinc-400 max-w-2xl mx-auto">
          {skillCount} portable skills for agentic CLI tools.
          <br />
          <span className="text-zinc-500">Browse, search, and discover.</span>
        </p>
      </div>
    </section>
  );
}
