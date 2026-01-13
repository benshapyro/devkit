# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added
- README.md with comprehensive documentation, architecture diagram, and examples for all artifact types
- CHANGELOG.md to track project changes
- README-SPEC.md capturing documentation requirements

### Changed
- Updated CLAUDE.md with changelog maintenance instructions

## [0.1.0] - 2025-01-08

### Added
- Initial devkit structure with four artifact types: skills, hooks, commands, agents
- Skills library with document processing (PDF, Word, PowerPoint, Excel), development tools, business frameworks, and content utilities
- 7 agents migrated from personal config: code-reviewer, debugger, documentation-researcher, git-helper, performance-optimizer, refactoring-assistant, spec-discovery
- 5 hooks migrated from personal config for security, formatting, and testing automation
- 10 commands: backlog, greenfield, learn, plan, progress, research, review, ship, slop, validate
- Skill creator tooling: init_skill.py, package_skill.py, quick_validate.py
- CUSTOMIZATION.md specification for hooks, commands, and agents
- CLAUDE.md files in each subdirectory for context-aware assistance

### Changed
- Commands updated with allowed-tools restrictions and improved error handling
- Reduced command verbosity for cleaner output

## Types of Changes

- **Added** for new features
- **Changed** for changes in existing functionality
- **Deprecated** for soon-to-be removed features
- **Removed** for now removed features
- **Fixed** for bug fixes
- **Security** for vulnerability fixes
