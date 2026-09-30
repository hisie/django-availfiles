# django-simplefiles

A minimal, frontend-agnostic file library for Django. `SimpleFile` is a
flat model — upload a file, get a URL back — deliberately **not** related
to any other model via a foreign key. The point is a place to put a file
once and link to it from anywhere (a blog post body, a product
description, an email), not a structured per-model attachment relation.

## What this package does, and doesn't, do

- `SimpleFile`: `file`, `original_filename` (captured automatically on
  save), an optional `label`, `uploaded_by`, `uploaded_at`.
- Registers with Django admin.
- It does **not** ship any views, URLs, upload endpoint, or picker UI —
  that's genuinely framework/host-specific (a dashboard page, a rich-text
  editor's file-picker, a plain form), and belongs in an integration
  layer. For an Oscar dashboard + TinyMCE integration, see
  [django-oscar-simplefiles](https://github.com/hisie/django-oscar-simplefiles).
- No opinion on which file types are allowed. A deployment might restrict
  this library to non-image files (if images already have their own
  upload flow elsewhere) — that's a policy decision for whichever upload
  view is actually used, not something this model enforces.

## Installation

```
uv add django-simplefiles
```

```python
INSTALLED_APPS = [
    ...,
    "simplefiles",
]
```

Run `manage.py migrate`.

## Development

```
uv sync
uv run pytest
```
