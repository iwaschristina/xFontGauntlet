# xFontGauntlet

**Current font test corpus — v2.8 (G201 regression coverage atop G200)**

xFontGauntlet is a regression corpus for the Font Renamer (x01), Font Converter (x02), Font Finder/Copier (x03), xFontMedic Font Audit/Repair (x04), and associated movers. It includes real, synthetic, unusual, and intentionally malformed fonts; package and folder structures; sidecars and companions; manifests; expected results; and corpus management/validation tools.

## Authoritative distribution

**The complete `xFontGauntlet_v2.8.zip` on the tagged [GitHub Release](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.8) is the current corpus**, not an extracted Git checkout. Intentional ZIP entry spellings, invalid/edge-case path structures, and empty directory records cannot all be represented faithfully in normal Git.

| Property | v2.8 |
| --- | --- |
| Historical baseline | G201 appended to preserved G200 |
| Groups | 199 |
| Declared logical cases | 2,844 |
| Files within archive | 43,561 |
| ZIP directory entries | 10,041 |
| Archive size | 74,597,059 bytes |
| SHA-256 | `3b8b27fb6242ee14f92bf41a0e1490577040198171184384e200a51f33b172ac` |

## Contents and use

The ZIP root contains `TestCorpus/` (test groups, font specimens, and related sidecars/packages), `Tools/` (corpus maintenance and validators), and 20 guide, manifest, catalog, and summary files at the root alongside those two directories.

1. Download the **original** ZIP from the matching versioned Release. Do not recompress, extract-and-repackage, rename members, normalize paths, or filter unconventional binary fixtures.
2. Compare SHA-256 against `checksums/v2.8.sha256` using PowerShell `Get-FileHash xFontGauntlet_v2.8.zip -Algorithm SHA256` or `sha256sum xFontGauntlet_v2.8.zip`.
3. Read `00_CURRENT_CORPUS_GUIDE.txt` and `Tools/README_START_HERE.txt` **inside the archive** for detailed organization, groups, expectations and validators.
4. Stage tests in **disposable workspaces** with the included tools when a scenario requires a normal filesystem. Some ZIP paths are intentionally unusual or invalid after extraction on particular filesystems; do not alter the authoritative ZIP to accommodate them.
5. Test the Font Finder/Copier's discovery and sidecar/package preservation, the Converter's outputs, skipping and recovery behavior, the Renamer's identity/duplicate marking, and the movers' atomicity, sidecar ownership, cancellation and rollback. Use the expected results for each case.

The v2.8 release retains the G200 UFO3 repairs and adds 22 G201 regression cases for x01 deep-path discovery/package budgeting, x02 long-path host recovery/output safety and x04 headless reports/Python 3 fallback. x03 functional coverage remains intact. Original root manifest, lock and catalog records are preserved at Tools/Corpus Contamination Finder/Changed Renamed or Removed Corpus Files/G201_Post_v2_7_Coverage/Originals/. Group 13 is unchanged and remains excluded from routine x02 converter runs. The historical PowerShell integrity suite has the same five failures as v2.7, with zero new failures; see RELEASE_NOTES_v2.8.md. Static corpus-integrity/fixture validation and production-tool runtime acceptance are **different checks**. Packaging a release does not certify that production tools pass all scenarios.

v2.8 preserves the verified v2.7 root layout, all original font fixtures and every Group 13 entry. All earlier releases remain available for historical use.

## Repository policy

This repository stores documentation, integrity records, and release automation, **not an extracted corpus or historical binary ZIPs in Git history**. The release asset is the source of truth. Each future approved/verified version gets its own immutable release ZIP and matching Git tag. Preserve all historical artifacts and retired/changed corpus-file records. Never silently remove, regenerate, rename, normalize, transform, or replace test fixtures.

## Release

See [v2.8 release](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.8) and `RELEASE_NOTES_v2.8.md`. The published v2.8 ZIP passed an independent re-download and full-file SHA-256 verification. Historical validators and real production-tool runs remain separate from this integrity check. A release must not be considered published or authoritative until its uploaded ZIP is independently downloaded and its complete SHA-256 verified.
