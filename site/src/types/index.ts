export interface Skill {
  name: string;
  description: string;
  group: string;
  slug: string;
  excerpt: string;
  license?: string;
}

export interface FilterState {
  search: string;
  groups: string[];
}
