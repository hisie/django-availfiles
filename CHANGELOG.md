# Changelog

All notable changes to this project are documented in this file.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

## [0.2.1] - 2026-10-02

Docs-only — this `CHANGELOG.md` itself didn't exist until after 0.2.0
was published; bumping so PyPI's project page reflects it (PyPI freezes
the README/description at publish time, so it would otherwise stay
stale relative to what's in git).

## [0.2.0] - 2026-09-30

First real release. Published as `django-simplefiles` initially; PyPI
rejected that name as too similar to the existing `django-simple-files`
(0.1.0 was built under that name but never actually published) —
renamed throughout before any real release.

### Added

- `AvailFile`: `file`, `original_filename` (captured automatically on
  save), an optional `label`, `uploaded_by`, `uploaded_at`. Deliberately
  no FK from any other model, no views/URLs, no opinion on allowed file
  types — a flat library meant to be linked to from anywhere, not a
  per-model attachment relation.
- Registers with Django admin.
- 3 tests, 100% coverage.

[Unreleased]: https://github.com/hisie/django-availfiles/compare/0.2.1...HEAD
[0.2.1]: https://github.com/hisie/django-availfiles/compare/0.2.0...0.2.1
[0.2.0]: https://github.com/hisie/django-availfiles/releases/tag/0.2.0
