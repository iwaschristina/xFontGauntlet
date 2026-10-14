# xFontGauntlet

**Current font test corpus — v2.9 (G202 regression coverage atop G201)**

xFontGauntlet is a regression corpus for the Font Renamer (x01), Font Converter (x02), Font Finder/Copier (x03), xFontMedic Font Audit/Repair (x04), and associated movers. It includes real, synthetic, unusual, and intentionally malformed fonts; package and folder structures; sidecars and companions; manifests; expected results; and corpus management/validation tools.

## Authoritative distribution

**The complete `xFontGauntlet_v2.9.zip` on the tagged [GitHub Release](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.9) is the current corpus**, not an extracted Git checkout. Intentional ZIP entry spellings, invalid/edge-case path structures, and empty directory records cannot all be represented faithfully in normal Git.

| Property | v2.9 |
| --- | --- |
| Historical baseline | G202 appended to preserved G201 |
| Groups | 200 |
| Declared logical cases | 2,867 |
| Files within archive | 43,623 |
| ZIP directory entries | 10,072 |
| Archive size | 78,579,361 bytes |
| SHA-256 | `6e0897b253c5df00b45822b113f679161ef9a547d4fd3c9c839456d2f55dc57b` |

## Contents and use

The ZIP root contains `TestCorpus/` (test groups, font specimens, and related sidecars/packages), `Tools/` (corpus maintenance and validators), and 20 guide, manifest, catalog, and summary files at the root alongside those two directories.

1. Download the **original** ZIP from the matching versioned Release. Do not recompress, extract-and-repackage, rename members, normalize paths, or filter unconventional binary fixtures.
2. Compare SHA-256 against `checksums/v2.9.sha256` using PowerShell `Get-FileHash xFontGauntlet_v2.9.zip -Algorithm SHA256` or `sha256sum xFontGauntlet_v2.9.zip`.
3. Read `00_CURRENT_CORPUS_GUIDE.txt` and `Tools/README_START_HERE.txt` **inside the archive** for detailed organization, groups, expectations and validators.
4. Stage tests in **disposable workspaces** with the included tools when a scenario requires a normal filesystem. Some ZIP paths are intentionally unusual or invalid after extraction on particular filesystems; do not alter the authoritative ZIP to accommodate them.
5. Test the Font Finder/Copier's discovery and sidecar/package preservation, the Converter's outputs, skipping and recovery behavior, the Renamer's identity/duplicate marking, and the movers' atomicity, sidecar ownership, cancellation and rollback. Use the expected results for each case.

The v2.9 release retains all G200/G201 fixtures and adds 23 G202 cases for x01 mixed-namespace moves and locality, x02 extended-path external workers/Ghostscript dependency staging, and x04 UFO/UFOZ, PCF, VF and PFM parsing boundaries. x03 functional coverage remains intact. Original root manifest, lock and catalog records are archived at Tools/Corpus Contamination Finder/Changed Renamed or Removed Corpus Files/G202_Post_v2_8_Coverage/Originals/. Group 13 remains unchanged and excluded from routine converter runs. The legacy PowerShell suite retains the same five existing failures, with zero new failures; see RELEASE_NOTES_v2.9.md. Static corpus-integrity/fixture validation and production-tool runtime acceptance are **different checks**. Packaging a release does not certify that production tools pass all scenarios.

v2.9 preserves the verified v2.8 root layout, all original font fixtures and every Group 13 entry. All earlier releases remain available for historical use.

## Repository policy

This repository stores documentation, integrity records, and release automation, **not an extracted corpus or historical binary ZIPs in Git history**. The release asset is the source of truth. Each future approved/verified version gets its own immutable release ZIP and matching Git tag. Preserve all historical artifacts and retired/changed corpus-file records. Never silently remove, regenerate, rename, normalize, transform, or replace test fixtures.

## Release

See [v2.9 release](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.9) and `RELEASE_NOTES_v2.9.md`. The published v2.9 ZIP passed an independent re-download and full-file SHA-256 verification. Historical validators and real production-tool runs remain separate from this integrity check. A release must not be considered published or authoritative until its uploaded ZIP is independently downloaded and its complete SHA-256 verified.
