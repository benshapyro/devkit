import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const skills = defineCollection({
  loader: glob({
    // Match all SKILL.md files, excluding archive directories
    pattern: ['**/SKILL.md', '!**/archive/**', '!**/.archive/**'],
    base: '../skills',
    // Generate ID that preserves group/skill-name structure
    // entry = "ai-automation/prompt-engineering/SKILL.md"
    generateId: ({ entry }) => {
      // Remove /SKILL.md suffix and return "group/skill-name"
      return entry.replace(/\/SKILL\.md$/, '');
    },
  }),
  schema: z.object({
    name: z.string(),
    description: z.string(),
    license: z.string().optional(),
  }),
});

const hooks = defineCollection({
  loader: glob({
    // Match all .md files except CLAUDE.md and README.md
    pattern: ['*.md', '!CLAUDE.md', '!README.md', '!**/archive/**'],
    base: '../hooks',
    // Generate ID from filename without .md extension
    generateId: ({ entry }) => entry.replace(/\.md$/, ''),
  }),
  schema: z.object({
    tool: z.string(),
    event: z.string(),
    matcher: z.string().optional(),
    type: z.string(),
    command: z.string(),
    timeout: z.number().optional(),
  }),
});

const commands = defineCollection({
  loader: glob({
    // Match all .md files except CLAUDE.md and README.md
    pattern: ['*.md', '!CLAUDE.md', '!README.md', '!**/archive/**'],
    base: '../commands',
    // Generate ID from filename without .md extension
    generateId: ({ entry }) => entry.replace(/\.md$/, ''),
  }),
  schema: z.object({
    tool: z.string(),
    description: z.string(),
    'allowed-tools': z.string().optional(),
    'argument-hint': z.string().optional(),
    model: z.string().optional(),
    'disable-model-invocation': z.boolean().optional(),
  }),
});

const agents = defineCollection({
  loader: glob({
    // Match all .md files except CLAUDE.md and README.md
    pattern: ['*.md', '!CLAUDE.md', '!README.md', '!**/archive/**'],
    base: '../agents',
    // Generate ID from filename without .md extension
    generateId: ({ entry }) => entry.replace(/\.md$/, ''),
  }),
  schema: z.object({
    tool: z.string().optional(),
    name: z.string(),
    description: z.string(),
    tools: z.string().optional(),
    model: z.string().optional(),
    permissionMode: z.string().optional(),
    skills: z.string().optional(),
  }),
});

export const collections = { skills, hooks, commands, agents };

// Helper to extract group and slug from entry ID
// ID format: "group/skill-name" (e.g., "ai-automation/prompt-engineering")
export function parseSkillId(id: string) {
  const parts = id.split('/');
  // Handle both "group/skill-name" and edge case of just "skill-name"
  const group = parts.length > 1 ? parts[0] : 'uncategorized';
  const slug = parts.length > 1 ? parts[1] : parts[0];
  return { group, slug };
}

// Helper to extract slug from hook/command/agent ID
// ID format: "hook-name" (e.g., "dangerous-command-blocker")
export function parseArtifactId(id: string) {
  return { slug: id };
}

// Helper to create excerpt from description
export function createExcerpt(description: string, maxLength = 120) {
  return description.length > maxLength
    ? description.slice(0, maxLength - 3) + '...'
    : description;
}
