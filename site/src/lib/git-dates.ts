import { execSync } from 'node:child_process';
import { join } from 'node:path';

/**
 * Get the last modified date from git for a given skill directory
 * @param skillPath - Path relative to skills directory (e.g., "ai-automation/prompt-engineering")
 * @returns ISO date string of last commit, or current date if git fails
 */
export function getSkillLastModified(skillPath: string): string {
  try {
    const fullPath = join(process.cwd(), '../skills', skillPath);

    // Get the last commit date for any file in this skill directory
    const command = `git log -1 --format=%cI -- "${fullPath}"`;
    const output = execSync(command, {
      encoding: 'utf8',
      cwd: join(process.cwd(), '..'),
      stdio: ['pipe', 'pipe', 'pipe'],
    }).trim();

    // If no commits found for this path, return current date
    if (!output) {
      return new Date().toISOString();
    }

    return output;
  } catch (error) {
    // If git fails, return current date
    console.warn(`Failed to get git date for ${skillPath}:`, error);
    return new Date().toISOString();
  }
}

/**
 * Format a date string for display
 * @param isoDate - ISO date string
 * @returns Formatted date like "Jan 15, 2024"
 */
export function formatDate(isoDate: string): string {
  const date = new Date(isoDate);
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
  });
}

/**
 * Get relative time string like "2 days ago" or "3 months ago"
 * @param isoDate - ISO date string
 * @returns Relative time string
 */
export function getRelativeTime(isoDate: string): string {
  const date = new Date(isoDate);
  const now = new Date();
  const diffMs = now.getTime() - date.getTime();
  const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24));

  if (diffDays === 0) return 'Today';
  if (diffDays === 1) return 'Yesterday';
  if (diffDays < 7) return `${diffDays} days ago`;
  if (diffDays < 30) return `${Math.floor(diffDays / 7)} weeks ago`;
  if (diffDays < 365) return `${Math.floor(diffDays / 30)} months ago`;
  return `${Math.floor(diffDays / 365)} years ago`;
}
