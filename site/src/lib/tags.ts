// Role tags - "I am a..."
export const ROLE_TAGS = [
  'Frontend Developer',
  'Backend Developer',
  'Full-Stack Developer',
  'AI/ML Engineer',
  'DevOps Engineer',
  'Digital Marketer',
  'Content Creator',
  'Salesperson',
  'Product Manager',
  'Designer',
  'Data Analyst',
] as const;

export type RoleTag = typeof ROLE_TAGS[number];

// Task tags - "I want to..."
export const TASK_TAGS = [
  'Write Code',
  'Debug Code',
  'Test Code',
  'Review Code',
  'Document',
  'Deploy',
  'Create Images',
  'Create Videos',
  'Create Presentations',
  'Write Emails',
  'Analyze Data',
  'Automate Tasks',
  'Learn & Research',
] as const;

export type TaskTag = typeof TASK_TAGS[number];

// Favorite skill slugs (for curation)
export const FAVORITE_SKILLS = [
  'cadre-os',
  'ai-art-generation',
  'brainstorming',
  'frontend-design',
  'prompt-engineering',
  'presentation-composer',
  'product-discovery',
] as const;

// Output type indicators for skill cards
export const OUTPUT_TYPES = {
  document: { emoji: '📄', label: 'Document' },
  code: { emoji: '💻', label: 'Code' },
  visual: { emoji: '🎨', label: 'Visual' },
  guidance: { emoji: '💬', label: 'Guidance' },
} as const;

export type OutputType = keyof typeof OUTPUT_TYPES;
