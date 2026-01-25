import { hasDownload, getDownloadUrl, getDownloadInfo, formatFileSize } from "../lib/downloads";

interface Props {
  slug: string;
  baseUrl: string;
  variant: "icon" | "full";
  className?: string;
}

/**
 * Download button for skill packages.
 *
 * Two variants:
 * - `icon`: Small circular button with download icon (for card overlays)
 * - `full`: Full button with icon, text, and file size (for detail pages)
 */
export function DownloadButton({ slug, baseUrl, variant, className = "" }: Props) {
  if (!hasDownload(slug)) {
    return null;
  }

  const url = getDownloadUrl(slug, baseUrl);
  const info = getDownloadInfo(slug);

  if (!url || !info) {
    return null;
  }

  const downloadIcon = (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 20 20"
      fill="currentColor"
      className={variant === "icon" ? "w-4 h-4" : "w-5 h-5"}
      aria-hidden="true"
    >
      <path d="M10.75 2.75a.75.75 0 0 0-1.5 0v8.614L6.295 8.235a.75.75 0 1 0-1.09 1.03l4.25 4.5a.75.75 0 0 0 1.09 0l4.25-4.5a.75.75 0 0 0-1.09-1.03l-2.955 3.129V2.75Z" />
      <path d="M3.5 12.75a.75.75 0 0 0-1.5 0v2.5A2.75 2.75 0 0 0 4.75 18h10.5A2.75 2.75 0 0 0 18 15.25v-2.5a.75.75 0 0 0-1.5 0v2.5c0 .69-.56 1.25-1.25 1.25H4.75c-.69 0-1.25-.56-1.25-1.25v-2.5Z" />
    </svg>
  );

  if (variant === "icon") {
    return (
      <a
        href={url}
        download
        className={`inline-flex items-center justify-center w-8 h-8 rounded-full
                    bg-[#DB4545]/90 hover:bg-[#DB4545]
                    text-white
                    transition-all duration-200
                    hover:scale-110
                    focus:outline-none focus:ring-2 focus:ring-[#DB4545] focus:ring-offset-2 focus:ring-offset-zinc-900
                    ${className}`}
        title={`Download (${formatFileSize(info.size)})`}
        aria-label={`Download skill package (${formatFileSize(info.size)})`}
      >
        {downloadIcon}
      </a>
    );
  }

  return (
    <a
      href={url}
      download
      className={`inline-flex items-center gap-2 px-4 py-2 rounded-lg
                  bg-[#DB4545]/10 hover:bg-[#DB4545]/20
                  border border-[#DB4545]/30 hover:border-[#DB4545]/50
                  text-[#DB4545] hover:text-[#DB4545]
                  transition-all duration-200
                  focus:outline-none focus:ring-2 focus:ring-[#DB4545] focus:ring-offset-2 focus:ring-offset-zinc-900
                  ${className}`}
      aria-label={`Download skill package (${formatFileSize(info.size)})`}
    >
      {downloadIcon}
      <span className="font-medium">Download</span>
      <span className="text-[#DB4545]/70 text-sm">({formatFileSize(info.size)})</span>
    </a>
  );
}
