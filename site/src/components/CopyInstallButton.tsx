import { useState } from 'react';

interface Props {
  skillPath: string;  // e.g., "development-tools/mcp-builder"
}

/**
 * Copy install command button for skill packages.
 *
 * Copies a shell command to clipboard that installs the skill
 * to the user's Claude Code skills directory.
 */
export function CopyInstallButton({ skillPath }: Props) {
  const [copied, setCopied] = useState(false);

  // Command to copy the skill directory
  const command = `cp -r skills/${skillPath} ~/.claude/skills/`;

  const handleCopy = async () => {
    if (!navigator.clipboard) return;

    try {
      await navigator.clipboard.writeText(command);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch (err) {
      console.error('Failed to copy:', err);
    }
  };

  const copyIcon = (
    <svg
      className="w-5 h-5"
      fill="none"
      stroke="currentColor"
      viewBox="0 0 24 24"
      aria-hidden="true"
    >
      <path
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth={2}
        d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"
      />
    </svg>
  );

  const checkIcon = (
    <svg
      className="w-5 h-5 text-[#DB4545]"
      fill="none"
      stroke="currentColor"
      viewBox="0 0 24 24"
      aria-hidden="true"
    >
      <path
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth={2}
        d="M5 13l4 4L19 7"
      />
    </svg>
  );

  return (
    <button
      type="button"
      onClick={handleCopy}
      className="inline-flex items-center gap-2 px-4 py-2 rounded-lg
                 bg-white hover:bg-[#F2EFE4]
                 border border-[#E5E2D8] hover:border-[#D1CEC4]
                 text-[#6E7191] hover:text-[#0C0407]
                 transition-all duration-200
                 focus:outline-none focus:ring-2 focus:ring-zinc-500 focus:ring-offset-2 focus:ring-offset-zinc-900"
      aria-label={copied ? 'Copied!' : 'Copy install command'}
    >
      {copied ? checkIcon : copyIcon}
      <span className="font-medium">{copied ? 'Copied!' : 'Copy install'}</span>
    </button>
  );
}
