"""Tests for lib.core.config module."""

import json
import os
import pytest
from unittest.mock import patch
from tempfile import NamedTemporaryFile

# Add parent path for imports
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from lib.core.config import (
    Settings,
    ExtensionSettings,
    load_settings,
    get_setting,
    is_extension_enabled,
    get_extension_option,
    is_debug,
    is_quiet,
)


class TestExtensionSettings:
    """Tests for ExtensionSettings dataclass."""

    def test_default_values(self):
        """Default values are correct."""
        ext = ExtensionSettings()
        assert ext.enabled is True
        assert ext.options == {}

    def test_custom_values(self):
        """Custom values are stored."""
        ext = ExtensionSettings(
            enabled=False,
            options={"key": "value"},
        )
        assert ext.enabled is False
        assert ext.options["key"] == "value"


class TestSettings:
    """Tests for Settings dataclass."""

    def test_default_values(self):
        """Default values are correct."""
        settings = Settings()
        assert settings.debug is False
        assert settings.quiet is False
        assert settings.performance_budget_ms == 2000
        assert settings.coverage_threshold == 80.0
        assert settings.coverage_delta_only is True

    def test_from_dict_empty(self):
        """Empty dict returns defaults."""
        settings = Settings.from_dict({})
        assert settings.debug is False

    def test_from_dict_with_devkit(self):
        """Parses devkit section."""
        data = {
            "devkit": {
                "debug": True,
                "quiet": True,
                "performanceBudgetMs": 5000,
            }
        }
        settings = Settings.from_dict(data)
        assert settings.debug is True
        assert settings.quiet is True
        assert settings.performance_budget_ms == 5000

    def test_from_dict_with_extensions(self):
        """Parses extension settings."""
        data = {
            "devkit": {
                "extensions": {
                    "test-coverage": {
                        "enabled": True,
                        "options": {"threshold": 90},
                    },
                    "disabled-ext": False,
                }
            }
        }
        settings = Settings.from_dict(data)

        assert "test-coverage" in settings.extensions
        assert settings.extensions["test-coverage"].enabled is True
        assert settings.extensions["test-coverage"].options["threshold"] == 90

        assert "disabled-ext" in settings.extensions
        assert settings.extensions["disabled-ext"].enabled is False


class TestLoadSettings:
    """Tests for load_settings function."""

    def test_missing_file_returns_defaults(self):
        """Missing file returns default settings."""
        with patch("lib.core.config.get_settings_path") as mock_path:
            mock_path.return_value = Path("/nonexistent/path/settings.json")
            settings = load_settings()
            assert settings.debug is False

    def test_valid_file_loads(self):
        """Valid JSON file is parsed."""
        with NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump({"devkit": {"debug": True}}, f)
            f.flush()

            try:
                settings = load_settings(Path(f.name))
                assert settings.debug is True
            finally:
                os.unlink(f.name)


class TestGetSetting:
    """Tests for get_setting function."""

    def test_simple_key(self):
        """Simple key lookup works."""
        settings = Settings(debug=True)
        result = get_setting("debug", settings=settings)
        assert result is True

    def test_missing_key_returns_default(self):
        """Missing key returns default value."""
        settings = Settings()
        result = get_setting("nonexistent", default="fallback", settings=settings)
        assert result == "fallback"


class TestIsExtensionEnabled:
    """Tests for is_extension_enabled function."""

    def test_unconfigured_defaults_to_enabled(self):
        """Unconfigured extension defaults to enabled."""
        settings = Settings()
        result = is_extension_enabled("some-extension", settings=settings)
        assert result is True

    def test_explicitly_enabled(self):
        """Explicitly enabled extension returns True."""
        settings = Settings()
        settings.extensions["test-ext"] = ExtensionSettings(enabled=True)
        result = is_extension_enabled("test-ext", settings=settings)
        assert result is True

    def test_explicitly_disabled(self):
        """Explicitly disabled extension returns False."""
        settings = Settings()
        settings.extensions["test-ext"] = ExtensionSettings(enabled=False)
        result = is_extension_enabled("test-ext", settings=settings)
        assert result is False


class TestGetExtensionOption:
    """Tests for get_extension_option function."""

    def test_missing_extension_returns_default(self):
        """Missing extension returns default value."""
        settings = Settings()
        result = get_extension_option("missing", "option", default="default", settings=settings)
        assert result == "default"

    def test_missing_option_returns_default(self):
        """Missing option returns default value."""
        settings = Settings()
        settings.extensions["test-ext"] = ExtensionSettings(enabled=True, options={})
        result = get_extension_option("test-ext", "missing", default="default", settings=settings)
        assert result == "default"

    def test_existing_option_returned(self):
        """Existing option is returned."""
        settings = Settings()
        settings.extensions["test-ext"] = ExtensionSettings(
            enabled=True,
            options={"key": "value"},
        )
        result = get_extension_option("test-ext", "key", settings=settings)
        assert result == "value"


class TestIsDebug:
    """Tests for is_debug function."""

    def test_env_var_overrides(self):
        """CLAUDE_HOOK_DEBUG env var overrides settings."""
        with patch.dict(os.environ, {"CLAUDE_HOOK_DEBUG": "1"}):
            assert is_debug() is True


class TestIsQuiet:
    """Tests for is_quiet function."""

    def test_env_var_overrides(self):
        """CLAUDE_QUIET env var overrides settings."""
        with patch.dict(os.environ, {"CLAUDE_QUIET": "1"}):
            assert is_quiet() is True
