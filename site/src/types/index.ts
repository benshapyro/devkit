export interface Skill {
  name: string;
  description: string;
  group: string;
  slug: string;
  excerpt: string;
  license?: string;
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

export interface FilterState {
  search: string;
  groups: string[];
}
