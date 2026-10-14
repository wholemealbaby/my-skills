---
name: report-writing
description: Write or edit the RMIT Deep Learning Assignment 2 report prose, its notebook markdown cells, or its figures. Use when drafting, revising, expanding, or reviewing report sections and notebook markdown, when adding, titling, or compressing a report figure, or when matching the existing report structure, section numbering, observation and inference style, and citation and figure conventions. Applies to report/text.md, the my_final notebook and its # %% twin, and report/images. Defers environment setup, running Python, and code-cell style to the python-and-notebook-environment and python-code-style skills, and to the no-em-dashes skill for dash cleanup.
---

# Report Writing

## What this governs

The report prose and the figures it uses, and nothing else.

- Prose source of truth: `A2/report/text.md`. This is the report. Preserve its
  finished prose; do not rewrite a section you were not asked to change.
- Notebook twin: `A2/my_final.ipynb` and its `# %%` twin `A2/my_final.py`. They
  carry the same section order as `text.md` and embed the same figures. Keep the
  two in step when a section changes.
- Figures: `A2/report/images/`, with the published set in `A2/report/images/jpgs/`.

Environment setup and how to run Python or notebook code belong to the
`python-and-notebook-environment` skill. Python and notebook code style belongs
to `python-code-style`. Dash cleanup for prose belongs to `no-em-dashes`. This
skill covers only report structure, prose, and figures.

## Report structure

New material goes into the existing numbered skeleton at the point it belongs.
Do not renumber or insert top-level sections.

- Title and byline: `# RMIT Deep Learning 2026 Assignment 2: Detecting
  Persuasion Techniques` then `*By Thomas Gosling (S3850201)*`.
- 1 Introduction
- 2 Tasks, 2.1 Part A, 2.2 Part B
- 3 Datasets, 3.1 Primary corpus, 3.2 Auxiliary corpus (SemEval-2020 Task 11),
  3.3 Augmented corpus (US-to-Australian entity substitution)
- 4 Exploration, 4.1 Homoglyph analysis and replacement, 4.2 De-duplication,
  4.3 Embedding and co-occurrence analysis, 4.4 Sequence length
- 5 Evaluation protocol, 5.1 Data Splits, 5.2 Classification Metrics,
  5.3 Modified Span Metrics, 5.4 Head Implementation, 5.5 Training Approach
- 6 Design Iterations
- 7 Hyper Parameter Optimisation, 7.1 HPO, 7.2 Dropout, 7.3 Selection Confirmation
- Product questions C1 to C4
- Runtime, privacy and deployment judgment
- Limitations, references and reproducibility
- Appendix: experiment register

The notebook also carries sections that are not in `text.md`: the imports,
configuration and helpers block (its section 2 with 2.1 and 2.2), the
Part A, Part B and product requirements cell, the 5.1 Augmentation Setup cell,
and the design-process iteration helpers. Keep those in the notebook only.

## Prose style

Applies to new and rewritten Markdown cells only. Do not revise older sections just to change their style.

Write analytical content as ordinary, connected prose in complete sentences. Do not use labeled fields, templates, bullet points, or other structured formats for Observation, Inference, and Decision. Instead, incorporate each into the prose in this order: state the Observation using a measured value from this project’s output, explain the Inference, including what the evidence does and does not establish, and then state the resulting Decision. Use a separate paragraph for each decision.

Close each analytical section with a sentence describing its limitations.

Do not use metaphors, figurative language, euphemisms, or vague wording in place of numbers. Do not personify model components or make causal claims about quantities that are collinear by construction. Avoid rhetorical staging of results.

Do not use em dashes or en dashes in prose.

## Figure pipeline

`report/images/jpgs/` is the source of truth for the report figures. Never add to
it without explicit user confirmation, and never retitle, recompress, or
overwrite a file already in it without asking.

For a new graph:

1. Write the raw image into `report/images/` first.
2. Run `scripts/add_title.py` to add the title and compress at `--quality 60`,
   writing the result into `report/images/`.
3. Show the user the titled and compressed image and ask before promoting it into
   `report/images/jpgs/`.
4. Only on confirmation, place the finished file in `report/images/jpgs/` and
   embed it.

Naming and embedding:

- Name the file `figureX.Y.Z.jpg` keyed to the section that uses it, matching the
  existing files such as `figure4.3.1.jpg` and `figure3.1.1.jpg`.
- Embed with `![Figure X.Y.Z](./images/jpgs/figureX.Y.Z.jpg)`, the path relative
  to `report/`, matching the existing cells. From the notebook the path is
  `./report/images/jpgs/figureX.Y.Z.jpg`.
- An HTML `<img ... width="N">` embed is acceptable where an existing figure uses
  one; otherwise prefer the markdown form.

## add_title.py

A copy of the tool ships at `scripts/add_title.py` beside this file. It adds a
centered, word-wrapped title to an image and writes a compressed JPEG.

```
python "<skill>/scripts/add_title.py" <image> <title words...> \
    [-o <output.jpg>] [-q 60] [--mode bar|overlay] \
    [--font-size N] [--color C] [--background C]
```

- `image`: input image path.
- `<title words...>`: the title text; words are joined with spaces.
- `-o`, `--output`: output JPEG path. Default `<image stem>_titled.jpg`.
- `-q`, `--quality`: Pillow JPEG quality, 1 to 95, lower is smaller. Use `60` for
  report figures.
- `--mode`: `bar` (default) grows a white title band above the image; `overlay`
  draws an opaque band over the top.
- `--font-size`: title size in pixels. Default 3 percent of image width.
- `--color`, `--background`: title and band colours. Default black on white.

The project invocation, using the interpreter this repo already uses:

```powershell
& "C:\Users\Ninya\miniconda3\envs\pytorch312\python.exe" `
    "A:\Projects\rmit\dl\.github\skills\report-writing\scripts\add_title.py" `
    "A:\Projects\rmit\dl\A2\report\images\figureX.Y.Z_raw.jpg" `
    "Figure X.Y.Z: short descriptive title" `
    -o "A:\Projects\rmit\dl\A2\report\images\figureX.Y.Z.jpg" --quality 60
```

`${CLAUDE_SKILL_DIR}` resolves to this skill's folder however it was installed.
If it is not set, point at `scripts/add_title.py` inside this skill directory. The
tool prints the path it wrote.
