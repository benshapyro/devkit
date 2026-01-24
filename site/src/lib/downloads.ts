/**
 * Download utilities for skill packages.
 *
 * The manifest uses composite keys in the format `{group}/{slug}`.
 * These utilities accept just the slug and search for matching entries.
 */

import manifest from "../data/download-manifest.json";

/**
 * Manifest entry containing download metadata for a skill.
 */
export interface DownloadEntry {
  path: string;
  group: string;
  size: number;
}

/**
 * Type for the download manifest structure.
 */
type DownloadManifest = Record<string, DownloadEntry>;

const typedManifest = manifest as DownloadManifest;

/**
 * Finds a manifest entry by slug.
 * Searches for keys ending with `/{slug}` to handle composite keys.
 */
function findEntryBySlug(slug: string): [string, DownloadEntry] | undefined {
  if (!slug) return undefined; // Guard against empty strings

  const suffix = `/${slug}`;
  const entry = Object.entries(typedManifest).find(
    ([key]) => key.endsWith(suffix) || key === slug
  );
  return entry;
}

/**
 * Get download information for a skill by its slug.
 *
 * @param slug - The skill slug (e.g., "react-patterns")
 * @returns The download entry or undefined if not found
 */
export function getDownloadInfo(slug: string): DownloadEntry | undefined {
  const entry = findEntryBySlug(slug);
  return entry?.[1];
}

/**
 * Check if a download is available for a skill.
 *
 * @param slug - The skill slug (e.g., "react-patterns")
 * @returns true if a download exists for this slug
 */
export function hasDownload(slug: string): boolean {
  return findEntryBySlug(slug) !== undefined;
}

/**
 * Format a file size in bytes to a human-readable string.
 *
 * @param bytes - File size in bytes
 * @returns Formatted string (e.g., "3.4 KB", "1.2 MB")
 */
export function formatFileSize(bytes: number): string {
  if (bytes < 0) {
    return "0 B";
  }

  const units = ["B", "KB", "MB", "GB", "TB"];
  let unitIndex = 0;
  let size = bytes;

  while (size >= 1024 && unitIndex < units.length - 1) {
    size /= 1024;
    unitIndex++;
  }

  // Show integers for bytes, one decimal for larger units
  if (unitIndex === 0) {
    return `${Math.round(size)} ${units[unitIndex]}`;
  }

  return `${size.toFixed(1)} ${units[unitIndex]}`;
}

/**
 * Get the full download URL for a skill.
 *
 * @param slug - The skill slug (e.g., "react-patterns")
 * @param baseUrl - The base URL to prepend (e.g., "https://example.com")
 * @returns The full download URL or undefined if the skill has no download
 */
export function getDownloadUrl(slug: string, baseUrl: string): string | undefined {
  const entry = getDownloadInfo(slug);
  if (!entry) {
    return undefined;
  }

  // Remove trailing slash from baseUrl if present
  const normalizedBase = baseUrl.endsWith("/") ? baseUrl.slice(0, -1) : baseUrl;

  return `${normalizedBase}${entry.path}`;
}
