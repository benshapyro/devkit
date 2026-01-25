import type { Agent } from '../types';

interface Props {
  agent: Agent;
  baseUrl: string;
}

export function AgentCard({ agent, baseUrl }: Props) {
  const agentUrl = `${baseUrl}/agents/${agent.slug}`;

  return (
    <div
      className="group relative rounded-2xl overflow-hidden
                 bg-white
                 border border-[#E5E2D8]
                 hover:border-[#D1CEC4]
                 transition-all duration-300 ease-out
                 hover:shadow-2xl hover:shadow-[#08749B]/5"
    >
      <a
        href={agentUrl}
        aria-label={`View details for ${agent.name}`}
        className="block p-6 focus:outline-none focus:ring-2 focus:ring-[#08749B]/50 focus:ring-inset rounded-2xl"
      >
        {/* Top accent line */}
        <div className="absolute top-0 inset-x-0 h-px bg-gradient-to-r from-transparent via-[#E5E2D8] to-transparent" />

        {/* Hover glow */}
        <div className="absolute inset-0 bg-gradient-to-b from-[#08749B]/[0.03] to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />

        <div className="relative">
          {/* Icon and type label */}
          <div className="flex items-center gap-3 mb-4">
            <span className="text-2xl text-[#08749B]/70 group-hover:text-[#08749B] transition-colors">
              ◉
            </span>
            <span className="text-xs font-medium text-[#A1A1A1] uppercase tracking-wider">
              Agent
            </span>
          </div>

          {/* Title (agent name) */}
          <h3 className="text-lg font-semibold text-[#0C0407] transition-colors leading-snug">
            {agent.name}
          </h3>

          {/* Description */}
          <p className="mt-3 text-sm text-[#6E7191] line-clamp-2 leading-relaxed">
            {agent.description}
          </p>

          {/* Model badge if present */}
          {agent.model && (
            <div className="mt-4">
              <span className="inline-flex items-center px-2 py-1 rounded text-xs font-mono bg-[#F2EFE4] text-[#6E7191] border border-[#E5E2D8]">
                {agent.model}
              </span>
            </div>
          )}

          {/* Bottom arrow indicator */}
          <div className="mt-4 flex items-center text-sm text-[#6E7191] group-hover:text-[#08749B] transition-colors">
            <span className="opacity-0 -translate-x-2 group-hover:opacity-100 group-hover:translate-x-0 transition-all duration-200">
              View details →
            </span>
          </div>
        </div>
      </a>
    </div>
  );
}
