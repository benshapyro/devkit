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

export const collections = { skills };

// Helper to extract group and slug from entry ID
// ID format: "group/skill-name" (e.g., "ai-automation/prompt-engineering")
export function parseSkillId(id: string) {
  const parts = id.split('/');
  // Handle both "group/skill-name" and edge case of just "skill-name"
  const group = parts.length > 1 ? parts[0] : 'uncategorized';
  const slug = parts.length > 1 ? parts[1] : parts[0];
  return { group, slug };
}

// Helper to create excerpt from description
export function createExcerpt(description: string, maxLength = 120) {
  return description.length > maxLength
    ? description.slice(0, maxLength - 3) + '...'
    : description;
}
