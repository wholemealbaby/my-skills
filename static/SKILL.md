---
name: static
description: Statically edit and analyze Python files (including Jupyter-style # %% cell scripts) and .ipynb notebooks without executing code, running CLI commands, or invoking MCP. Use for safe, execution-free refactors, renames, docstring edits, import reorganization, cell restructuring, or read-only inspection.
---

# Static

Edit and analyze `.py` files (including `# %%` cell scripts) and `.ipynb` notebooks **statically only**.

## Forbidden
- Executing code: no `python`, `pytest`, `jupyter`, linters, formatters, or running cells/kernels.
- Shell/CLI: no `cat`, `grep`, `sed`, `git`, `find`, etc.
- MCP tools of any kind.
- Installing or importing packages.
- Notebook execution features (e.g. `execute_cell`, `run_all`).

If execution seems required, stop and tell the user the skill forbids it.

## Allowed
- Standard file read/write/edit tools.
- Notebook toolset, non-executing ops only: read, create, edit, insert, delete, reorder cells; edit metadata.

## Workflow
1. Read targets fully before editing.
2. State the plan; find every affected location by reading, not grepping.
3. Edit minimally with precise replacements (or notebook cell tools). Preserve markers, JSON structure, cell ids, metadata.
4. Verify by re-reading: syntax, references, bracket balance, JSON validity.

## Output
Report targets, changes, static verification, and anything unverifiable without execution. End with: `Verified statically (no execution).`