---
name: rmit-harvard
description: "Format, insert, and check citations and reference lists in RMIT Harvard author-date style. Use when adding or updating in-text citations, building an alphabetised reference list, or validating citation consistency across report text and notebook markdown cells."
---

# RMIT Harvard Citations

Apply the **RMIT Harvard author-date style** to in-text citations and reference lists in written reports and notebook markdown. The authoritative style guide lives online at the [RMIT Easy Cite RMIT Harvard guide](https://www.lib.rmit.edu.au/easy-cite/?styleguide=styleguide-1); consult it for anything not covered below, since the live guide may be updated.

## 1. Citation style rules

### 1.1 In-text citation format

| Scenario | Format | Example |
|----------|--------|---------|
| Paraphrasing (end of sentence) | `(Author Year)` | `... (Giglio et al. 2016).` |
| Paraphrasing (author in sentence) | `Author (Year)` | `Giglio et al. (2016) explain that ...` |
| Two authors | `(Author and Author Year)` | `... (Schroeder and Giglio 2018).` |
| Three or more authors | `(Author et al. Year)` | `... (Giglio et al. 2016).` |
| Multiple sources | `(Author Year; Author Year)` | `... (Giglio et al. 2016; Schroeder and Giglio 2018).` |
| Organisation as author | `(Organisation Year)` | `... (NASA 2023).` |
| No date | `(Author n.d.)` | `... (Wotton n.d.).` |
| Direct quote | `(Author Year:page)` | `... (Hill and Martinez-Diez 2020:18).` |

### 1.2 Reference list format

Entries appear in a **References** section, alphabetised by author surname:

```
Author Surname, Initials Year *Title*, Publisher, accessed Day Month Year. URL
```

**Examples:**

```
Giglio L, Schroeder W and Justice CO 2016, 'The collection 6 MODIS active fire detection algorithm and fire products', *Remote Sensing of Environment*, vol. 178, pp. 31-41, accessed 3 May 2026. https://doi.org/10.1016/j.rse.2016.02.054

Example A 2025, 'Understanding Decision Trees: A Complete Guide', *Example Publisher*, accessed 13 May 2026. https://example.com/article

Schroeder W and Giglio L 2018, 'NASA VIIRS Land Surface Active Fire Product', *NASA Technical Report*, accessed 3 May 2026. https://example.com/report.pdf
```

### 1.3 Prohibited characters

- **Do not use em dashes** (`---`, `--`, or the Unicode em dash) in markdown text. Replace with colons, semicolons, or restructured sentences.
- The only allowed `---` is the horizontal rule divider in its own markdown cell.

---

## 2. Placing citations

Citations belong in the analytical prose of the document, included inline within the sentence, not as footnotes or endnotes. Every **decision justification** must carry a reference.

In notebook-style scripts, keep citations in the markdown cells that carry the written analysis:

| Cell type | Citation placement |
|-----------|-------------------|
| Title / heading cell | No citations. Heading only. |
| Code cell | No citations. Code only. |
| Observations / narrative markdown cell | **Yes**: inline citations in the analytical text. |
| Divider cell | No citations. Separator only. |

**Correct example:**

```markdown
# %% [markdown]
# ### Observations: Chosen Strategy Justification
#
# Median imputation is selected for numeric columns due to its robustness
# to the right skew observed in `wind_speed` (skewness = 1.79) and
# `brightness` (skewness = 1.21) (Little and Rubin 2019).
# For `month`, the median (7 = July) avoids the seasonal bias that mode
# imputation (1 = January) would introduce (van Buuren 2018).
```

In plain Markdown report files, use the same style without `# %%` markers:

```markdown
The dataset exhibits moderate class imbalance, with one class dominating at
44.3% while another is the least represented at 8.8% (Giglio et al. 2016).
This imbalance necessitates careful evaluation metric selection, as accuracy
alone would be misleading (He and Ma 2013).
```

---

## 3. Cross-file citation consistency

When citations appear across more than one file, keep them consistent:

1. **Same source, same format** — a source cited as `(Giglio et al. 2016)` in one file must use the same format everywhere.
2. **Single reference list** — prefer one consolidated, alphabetised reference list for the whole document.
3. **No orphans** — every in-text citation must have a matching reference-list entry, and every reference-list entry must be cited at least once in the text.

---

## 4. Validation checklist

Run through this checklist before completing citation work.

### 4.1 Per-citation

- [ ] Every decision justification has at least one inline citation.
- [ ] Citations use correct RMIT Harvard format: `(Author Year)` or `Author (Year)`.
- [ ] Three or more authors use `et al.`.
- [ ] Two authors use `and` between names.
- [ ] Direct quotes include a page number and use single inverted commas.
- [ ] No em dashes in markdown text.
- [ ] Citations are integrated naturally into the sentence, not tacked on.

### 4.2 Cross-file

- [ ] All in-text citations have matching reference-list entries.
- [ ] No orphan citations (cited in text but missing from the list).
- [ ] No orphan references (listed but never cited).

### 4.3 Reference list

- [ ] Reference list is alphabetised by author surname.
- [ ] Each entry follows `Author Year, *Title*, Publisher, accessed Date. URL`.
- [ ] Journal articles include volume and page numbers where available.
- [ ] URLs are accessible and correctly formatted.
- [ ] Access dates are current and consistent.

---

## 5. Source

The authoritative RMIT Harvard style guide is the [RMIT Easy Cite RMIT Harvard guide](https://www.lib.rmit.edu.au/easy-cite/?styleguide=styleguide-1). Treat this skill as a quick reference and consult the live guide for the current rules; confirm referencing requirements with your educators before relying on it.
