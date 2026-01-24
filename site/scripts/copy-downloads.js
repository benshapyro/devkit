/**
 * Copy skill zip files to public/downloads and generate manifest
 *
 * Reads: skills/.zip/{group}/{skill-name}.zip
 * Writes: site/public/downloads/{group}/{skill-name}.zip
 * Generates: site/src/data/download-manifest.json
 */

import { copyFileSync, existsSync, mkdirSync, readdirSync, statSync, writeFileSync } from "fs";
import { dirname, join, resolve } from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const siteRoot = resolve(__dirname, "..");
const projectRoot = resolve(siteRoot, "..");
const sourceDir = join(projectRoot, "skills", ".zip");
const destDir = join(siteRoot, "public", "downloads");
const manifestPath = join(siteRoot, "src", "data", "download-manifest.json");

function ensureDir(dirPath) {
  if (!existsSync(dirPath)) {
    mkdirSync(dirPath, { recursive: true });
  }
}

function copyZipFiles() {
  const manifest = {};

  try {
    if (!existsSync(sourceDir)) {
      console.log(`Source directory not found: ${sourceDir}`);
      console.log("No zip files to copy.");
      ensureDir(dirname(manifestPath));
      writeFileSync(manifestPath, JSON.stringify(manifest, null, 2));
      return;
    }

    const groups = readdirSync(sourceDir).filter((item) => {
      const itemPath = join(sourceDir, item);
      return statSync(itemPath).isDirectory();
    });

    let totalFiles = 0;

    for (const group of groups) {
      const groupSourcePath = join(sourceDir, group);
      const groupDestPath = join(destDir, group);

      const files = readdirSync(groupSourcePath).filter((file) => file.endsWith(".zip"));

      if (files.length === 0) {
        continue;
      }

      ensureDir(groupDestPath);

      for (const file of files) {
        const sourcePath = join(groupSourcePath, file);
        const destPath = join(groupDestPath, file);
        const slug = file.replace(".zip", "");
        const stats = statSync(sourcePath);

        copyFileSync(sourcePath, destPath);
        totalFiles++;

        // Use composite key to avoid collisions when same skill appears in multiple groups
        manifest[`${group}/${slug}`] = {
          path: `/downloads/${group}/${file}`,
          group,
          size: stats.size,
        };
      }
    }

    ensureDir(dirname(manifestPath));
    writeFileSync(manifestPath, JSON.stringify(manifest, null, 2));

    console.log(`Copied ${totalFiles} zip files to public/downloads/`);
    console.log(`Generated manifest with ${Object.keys(manifest).length} entries`);
  } catch (error) {
    console.error(`Error copying zip files: ${error.message}`);
    console.error("Stack trace:", error.stack);
    process.exit(1);
  }
}

copyZipFiles();
