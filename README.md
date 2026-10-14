# xFontGauntlet

**Current font test corpus — v2.12 (G204 regression coverage atop corrected G105 baseline)**

xFontGauntlet is a regression corpus for the Font Renamer (x01), Font Converter (x02), Font Finder/Copier (x03), xFontMedic Font Audit/Repair (x04), and associated movers. It includes real, synthetic, unusual, and intentionally malformed fonts; package and folder structures; sidecars and companions; manifests; expected results; and corpus management/validation tools.

## Authoritative distribution

**The complete `xFontGauntlet_v2.12.zip` on the tagged [GitHub Release](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.12) is the current corpus**, not an extracted Git checkout. Intentional ZIP entry spellings, invalid/edge-case path structures, and empty directory records cannot all be represented faithfully in normal Git.

| Property | v2.12 |
| --- | --- |
| Historical baseline | G204 appended to corrected v2.11/G105 |
| Groups | 202 |
| Declared logical cases | 2,916 |
| Files within archive | 43,828 |
| ZIP directory entries | 10,148 |
| Archive size | 90,867,436 bytes |
| SHA-256 | `adb26da2fc0942cd65c31cdbb747755a3c7a0c845d58504f42f53592bc3b25b0` |

## G105 external-reference correction

v2.11 repairs the G105-03 positive duplicate-mover fixture so the externally referenced UFO Project folder has its canonical renamer name *before* execution. `ExternalConsumer.designspace` and the fixture contract both refer to that exact folder; the reference remains resolvable through renaming and duplicate moving. The original folder members and original changed JSON/XML records are retained under `Tools/Corpus Contamination Finder/Changed Renamed or Removed Corpus Files/G105_External_Reference_Repair_v2_11/Originals/`. No other active fixtures were changed. Group 13 remains unchanged and intentionally excluded from routine converter runs.

## Contents and use

The ZIP root contains `TestCorpus/` (test groups, font specimens, and related sidecars/packages), `Tools/` (corpus maintenance and validators), and 20 guide, manifest, catalog, and summary files at the root alongside those two directories.

1. Download the **original** ZIP from the matching versioned Release. Do not recompress, extract-and-repackage, rename members, normalize paths, or filter unconventional binary fixtures.
2. Compare SHA-256 against `checksums/v2.12.sha256` using PowerShell `Get-FileHash xFontGauntlet_v2.12.zip -Algorithm SHA256` or `sha256sum xFontGauntlet_v2.12.zip`.
3. Read `00_CURRENT_CORPUS_GUIDE.txt` and `Tools/README_START_HERE.txt` **inside the archive** for detailed organization, groups, expectations and validators.
4. Stage tests in **disposable workspaces** with the included tools when a scenario requires a normal filesystem. Some ZIP paths are intentionally unusual or invalid after extraction on particular filesystems; do not alter the authoritative ZIP to accommodate them.
5. Test the Font Finder/Copier's discovery and sidecar/package preservation, the Converter's outputs, skipping and recovery behavior, the Renamer's identity/duplicate marking, and the movers' atomicity, sidecar ownership, cancellation and rollback. Use the expected results for each case.

The complete v2.12 release retains every v2.11 font/test fixture, including the corrected G105-03 designspace and prior G197/G198 positive UFO3 repairs. It adds 32 G204 cases: eight x01 duplicate mover filename-case/designspace scenarios; three x02 empty format-10 cmap and 27-source recovery/UFO preflight scenarios; and 21 x04 UFO/UFOZ, PCF, FNT/FON, and feature-file parsing scenarios. x03 coverage is unchanged. The three regenerated root integrity/catalog records have original byte copies in `Tools/Corpus Contamination Finder/Changed Renamed or Removed Corpus Files/G204_Post_v2_11_Coverage/Originals/`. Group 13 remains unchanged and excluded from routine x02 converter runs. Both v2.11 and v2.12 have the same six inherited PowerShell integrity validator failures and zero new failures; see `RELEASE_NOTES_v2.12.md`. Static archive verification does not certify production-tool runtime outcomes.

v2.12 preserves the verified v2.11 root layout and all earlier releases remain available. The outer corpus forbids case-folded path collisions; G204's intentionally case-colliding negative fixtures are sealed in nested packages for supported staging.

## Repository policy

This repository stores documentation, integrity records, and release automation, **not an extracted corpus or historical binary ZIPs in Git history**. The release asset is the source of truth. Each future approved/verified version gets its own immutable release ZIP and matching Git tag. Preserve all historical artifacts and retired/changed corpus-file records. Never silently remove, regenerate, rename, normalize, transform, or replace test fixtures.

## Release

See [v2.11 release](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.12) and `RELEASE_NOTES_v2.12.md`. The published v2.11 ZIP is independently re-downloaded and SHA-256 verified by the release workflow. Historical validators and real production-tool runs remain separate from this integrity check. A release must not be considered published or authoritative until its uploaded ZIP is independently downloaded and its complete SHA-256 verified.
