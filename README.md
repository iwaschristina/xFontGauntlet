# xFontGauntlet

**Current font test corpus — v2.14 (G206 signature-probe and converter coverage atop G205)**

xFontGauntlet is a regression corpus for the Font Renamer (x01), Font Converter (x02), Font Finder/Copier (x03), xFontMedic Font Audit/Repair (x04), and associated movers. It includes real, synthetic, unusual, and intentionally malformed fonts; package and folder structures; sidecars and companions; manifests; expected results; and corpus management/validation tools.

## Authoritative distribution

**The complete `xFontGauntlet_v2.14.zip` on the tagged [GitHub Release](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.14) is the current corpus**, not an extracted Git checkout. Intentional ZIP entry spellings, invalid/edge-case path structures, and empty directory records cannot all be represented faithfully in normal Git.

| Property | v2.14 |
| --- | --- |
| Historical baseline | G206 appended to preserved v2.13/G205 |
| Groups | 204 |
| Declared logical cases | 2,938 |
| Files within archive | 43,885 |
| ZIP directory entries | 10,163 |
| Archive size | 98,807,621 bytes |
| SHA-256 | `219fed0da2923ba7510fdd4e9d4c93d2687c42181ac51f1b723ef7f2c22ddf29` |

## G105 external-reference correction

v2.11 repairs the G105-03 positive duplicate-mover fixture so the externally referenced UFO Project folder has its canonical renamer name *before* execution. `ExternalConsumer.designspace` and the fixture contract both refer to that exact folder; the reference remains resolvable through renaming and duplicate moving. The original folder members and original changed JSON/XML records are retained under `Tools/Corpus Contamination Finder/Changed Renamed or Removed Corpus Files/G105_External_Reference_Repair_v2_11/Originals/`. No other active fixtures were changed. Group 13 remains unchanged and intentionally excluded from routine converter runs.

## Contents and use

The ZIP root contains `TestCorpus/` (test groups, font specimens, and related sidecars/packages), `Tools/` (corpus maintenance and validators), and 20 guide, manifest, catalog, and summary files at the root alongside those two directories.

1. Download the **original** ZIP from the matching versioned Release. Do not recompress, extract-and-repackage, rename members, normalize paths, or filter unconventional binary fixtures.
2. Compare SHA-256 against `checksums/v2.14.sha256` using PowerShell `Get-FileHash xFontGauntlet_v2.14.zip -Algorithm SHA256` or `sha256sum xFontGauntlet_v2.14.zip`.
3. Read `00_CURRENT_CORPUS_GUIDE.txt` and `Tools/README_START_HERE.txt` **inside the archive** for detailed organization, groups, expectations and validators.
4. Stage tests in **disposable workspaces** with the included tools when a scenario requires a normal filesystem. Some ZIP paths are intentionally unusual or invalid after extraction on particular filesystems; do not alter the authoritative ZIP to accommodate them.
5. Test the Font Finder/Copier's discovery and sidecar/package preservation, the Converter's outputs, skipping and recovery behavior, the Renamer's identity/duplicate marking, and the movers' atomicity, sidecar ownership, cancellation and rollback. Use the expected results for each case.

The complete v2.14 release preserves every v2.13 font/test fixture, including the corrected G105 designspace and earlier positive UFO3 repairs. It adds 18 G206 cases: five x01 v2.14 metadata-signature probe eligibility scenarios; ten x02 v2.15 native Unicode cmap mapped/unmapped scalar checks, validated against the current production parser; and three x02 observed-run contracts for the valid-content-route OTB, malformed format-8 batch continuation, and Type3/UFO output classification issues. Parser-only positive cmap cases explicitly do not claim successful full conversion. x03 and x04 coverage is retained unchanged.

Three regenerated root manifest/lock/catalog records have byte-identical originals under `Tools/Corpus Contamination Finder/Changed Renamed or Removed Corpus Files/G206_Post_v2_13_Coverage/Originals/`. All 22,109 Group 13 entries are unchanged, with Group 13 still excluded from routine x02 converter runs. Both v2.13 and v2.14 report the same six inherited historical integrity-validator failures, with zero new failures; see `RELEASE_NOTES_v2.14.md`. Windows application-level regression execution remains outside this corpus packaging verification.

v2.14 preserves v2.13's root directory layout, casefold uniqueness and earlier immutable release assets.

## Repository policy

This repository stores documentation, integrity records, and release automation, **not an extracted corpus or historical binary ZIPs in Git history**. The release asset is the source of truth. Each future approved/verified version gets its own immutable release ZIP and matching Git tag. Preserve all historical artifacts and retired/changed corpus-file records. Never silently remove, regenerate, rename, normalize, transform, or replace test fixtures.

## Release

See [v2.14 release](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.14) and `RELEASE_NOTES_v2.14.md`. The published v2.14 ZIP is independently re-downloaded and SHA-256 verified by the release workflow. Historical validators and real production-tool runs remain separate from this integrity check. A release must not be considered published or authoritative until its uploaded ZIP is independently downloaded and its complete SHA-256 verified.
