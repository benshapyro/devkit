import type { OutputType } from '../lib/tags';

export interface Skill {
  name: string;
  description: string;
  group: string;
  slug: string;
  excerpt: string;
  license?: string;
  tagline?: string;
  roles?: string[];
  tasks?: string[];
  favorite?: boolean;
  outputType?: OutputType;
  examplePrompt?: string;
}

export interface Hook {
  id: string;
  slug: string;
  name: string;
  description: string;
  event: string;
  matcher?: string;
}

export interface Command {
  id: string;
  slug: string;
  name: string;
  description: string;
  argumentHint?: string;
  allowedTools?: string;
}

export interface Agent {
  id: string;
  slug: string;
  name: string;
  description: string;
  tools?: string;
  model?: string;
}

export interface FilterState {
  search: string;
  groups: string[];
  roles: string[];
  tasks: string[];
}
