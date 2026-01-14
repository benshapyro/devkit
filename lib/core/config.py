"""
Configuration loading for devkit extensions.

Provides:
- Settings loading from ~/.claude/settings.json
- Type-safe settings access
- Default value handling
"""

import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional


@dataclass
class ExtensionSettings:
    """Settings for a specific extension."""
    enabled: bool = True
    options: dict[str, Any] = field(default_factory=dict)


@dataclass
class Settings:
    """Global devkit settings."""
    # Extension-specific settings
    extensions: dict[str, ExtensionSettings] = field(default_factory=dict)

    # Global settings
    debug: bool = False
    quiet: bool = False
    performance_budget_ms: int = 2000  # 2 seconds default

    # Coverage enforcer settings
    coverage_threshold: float = 80.0
    coverage_delta_only: bool = True

    # Security settings
    security_patterns: list[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict) -> "Settings":
        """Create Settings from dictionary."""
        settings = cls()

        # Parse extension settings
        extensions = data.get("devkit", {}).get("extensions", {})
        for name, ext_data in extensions.items():
            if isinstance(ext_data, dict):
                settings.extensions[name] = ExtensionSettings(
                    enabled=ext_data.get("enabled", True),
                    options=ext_data.get("options", {}),
                )
            elif isinstance(ext_data, bool):
                settings.extensions[name] = ExtensionSettings(enabled=ext_data)

        # Parse global settings
        devkit = data.get("devkit", {})
        settings.debug = devkit.get("debug", False)
        settings.quiet = devkit.get("quiet", False)
        settings.performance_budget_ms = devkit.get("performanceBudgetMs", 2000)
        settings.coverage_threshold = devkit.get("coverageThreshold", 80.0)
        settings.coverage_delta_only = devkit.get("coverageDeltaOnly", True)
        settings.security_patterns = devkit.get("securityPatterns", [])

        return settings


def get_settings_path() -> Path:
    """Get path to Claude Code settings.json."""
    # Check environment variable first
    custom_path = os.getenv("CLAUDE_SETTINGS_PATH")
    if custom_path:
        return Path(custom_path)

    # Default location
    home = Path.home()
    return home / ".claude" / "settings.json"


def load_settings(path: Optional[Path] = None) -> Settings:
    """
    Load settings from settings.json.

    Args:
        path: Optional custom path. If None, uses default location.

    Returns:
        Settings object with parsed values or defaults
    """
    if path is None:
        path = get_settings_path()

    try:
        with open(path, "r") as f:
            data = json.load(f)
        return Settings.from_dict(data)
    except (FileNotFoundError, json.JSONDecodeError):
        return Settings()


def get_setting(key: str, default: Any = None, settings: Optional[Settings] = None) -> Any:
    """
    Get a specific setting value.

    Args:
        key: Setting key (supports dot notation like "extensions.coverage.enabled")
        default: Default value if not found
        settings: Optional Settings object. If None, loads from disk.

    Returns:
        Setting value or default
    """
    if settings is None:
        settings = load_settings()

    parts = key.split(".")
    obj: Any = settings

    for part in parts:
        if hasattr(obj, part):
            obj = getattr(obj, part)
        elif isinstance(obj, dict) and part in obj:
            obj = obj[part]
        else:
            return default

    return obj


def is_extension_enabled(name: str, settings: Optional[Settings] = None) -> bool:
    """
    Check if a specific extension is enabled.

    Args:
        name: Extension name
        settings: Optional Settings object

    Returns:
        True if enabled (or not configured, defaults to enabled)
    """
    if settings is None:
        settings = load_settings()

    ext = settings.extensions.get(name)
    if ext is None:
        return True  # Default to enabled

    return ext.enabled


def get_extension_option(
    name: str,
    option: str,
    default: Any = None,
    settings: Optional[Settings] = None
) -> Any:
    """
    Get an option value for a specific extension.

    Args:
        name: Extension name
        option: Option name
        default: Default value
        settings: Optional Settings object

    Returns:
        Option value or default
    """
    if settings is None:
        settings = load_settings()

    ext = settings.extensions.get(name)
    if ext is None:
        return default

    return ext.options.get(option, default)


# Environment variable shortcuts
def is_debug() -> bool:
    """Check if debug mode is enabled."""
    if os.getenv("CLAUDE_HOOK_DEBUG"):
        return True
    return get_setting("debug", False)


def is_quiet() -> bool:
    """Check if quiet mode is enabled."""
    if os.getenv("CLAUDE_QUIET"):
        return True
    return get_setting("quiet", False)


def get_performance_budget() -> int:
    """Get performance budget in milliseconds."""
    return get_setting("performance_budget_ms", 2000)
