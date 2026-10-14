# xFontGauntlet

**Current font test corpus — v2.16 (G207 retained; Group 13 optional archive)**

xFontGauntlet is a regression corpus for the Font Renamer (x01), Font Converter (x02), Font Finder/Copier (x03), xFontMedic Font Audit/Repair (x04), and associated movers. It includes real, synthetic, unusual, and intentionally malformed fonts; package and folder structures; sidecars and companions; manifests; expected results; and corpus management/validation tools.

## Authoritative distribution

**The complete `xFontGauntlet_v2.16.zip` on the tagged [GitHub Release](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.16) is the current corpus**, not an extracted Git checkout. Intentional ZIP entry spellings, invalid/edge-case path structures, and empty directory records cannot all be represented faithfully in normal Git.

| Property | v2.16 |
| --- | --- |
| Historical baseline | G207 v2.15 preserved; Group 13 nested for optional use |
| Groups | 205 (including optional Group 13) |
| Declared logical cases | 2,969 |
| Files within archive | 22,516 |
| ZIP directory entries | 9,994 |
| Archive size | 98,917,857 bytes |
| SHA-256 | `0ec01f19b126e33a4abb4cb028a3ead38900c5348376685cc2e742ba30e84665` |

## G105 external-reference correction

v2.11 repairs the G105-03 positive duplicate-mover fixture so the externally referenced UFO Project folder has its canonical renamer name *before* execution. `ExternalConsumer.designspace` and the fixture contract both refer to that exact folder; the reference remains resolvable through renaming and duplicate moving. The original folder members and original changed JSON/XML records are retained under `Tools/Corpus Contamination Finder/Changed Renamed or Removed Corpus Files/G105_External_Reference_Repair_v2_11/Originals/`. No other active fixtures were changed. Group 13 remains unchanged and intentionally excluded from routine converter runs.

## Contents and use

The ZIP root contains `TestCorpus/` (test groups, font specimens, and related sidecars/packages), `Tools/` (corpus maintenance and validators), and 20 guide, manifest, catalog, and summary files at the root alongside those two directories.

1. Download the **original** ZIP from the matching versioned Release. Do not recompress, extract-and-repackage, rename members, normalize paths, or filter unconventional binary fixtures.
2. Compare SHA-256 against `checksums/v2.16.sha256` using PowerShell `Get-FileHash xFontGauntlet_v2.16.zip -Algorithm SHA256` or `sha256sum xFontGauntlet_v2.16.zip`.
3. Read `00_CURRENT_CORPUS_GUIDE.txt` and `Tools/README_START_HERE.txt` **inside the archive** for detailed organization, groups, expectations and validators.
4. Stage tests in **disposable workspaces** with the included tools when a scenario requires a normal filesystem. Some ZIP paths are intentionally unusual or invalid after extraction on particular filesystems; do not alter the authoritative ZIP to accommodate them.
5. Test the Font Finder/Copier's discovery and sidecar/package preservation, the Converter's outputs, skipping and recovery behavior, the Renamer's identity/duplicate marking, and the movers' atomicity, sidecar ownership, cancellation and rollback. Use the expected results for each case.

v2.16 preserves every x01–x04 case from the published v2.15 (G207) release: **205 groups and 2,969 declared logical cases**. The latest 31 G207 cases cover xFontMorph native source preservation, xFontHound's three observed BDF false positives, and xFontMedic's new structural and streaming boundaries. All previous fixture bytes and expected results remain unchanged.

### Optional Group 13 — normal tests are faster to extract and scan

**Group 13 is not unpacked by default.** All **21,633** entries of `TestCorpus/13_Corruption_Matrix_All_Font_Types/` are preserved in a nested ZIP:

`Tools/Optional Test Groups/Group13_Corruption_Matrix_All_Font_Types.zip`

To test Group 13, extract the full v2.16 ZIP as normal, then extract that nested ZIP **into the extracted `TestCorpus/` directory**. It recreates the original `13_Corruption_Matrix_All_Font_Types/` folder. See `Tools/Optional Test Groups/README_Group13.txt` inside the archive for the same instructions.

The old 22,109 count included **476 entries from other groups** whose nested folder names start with `13_`; those 476 remain in the outer ZIP. Only the actual Group 13 directory was archived. The inner ZIP's 21,633 members have been individually verified against the published v2.15 corpus, preserving paths, bytes, CRC, timestamps and file attributes.

Three root metadata records were regenerated for the default-extracted corpus and their exact originals archived at `Tools/Corpus Contamination Finder/Changed Renamed or Removed Corpus Files/G208_Post_v2_15_Group13_Archive/Originals/`. The active manifest and integrity lock exclude optional Group 13; the catalog continues to list it as a separately extractable group. Both v2.15 and v2.16 have the same six pre-existing PowerShell integrity-validator failures, with zero new failures. The updated outer ZIP was independently downloaded and SHA-256 verified. See `RELEASE_NOTES_v2.16.md`.

Full Windows application regression runs were not performed as part of this packaging-only change.

## Repository policy

This repository stores documentation, integrity records, and release automation, **not an extracted corpus or historical binary ZIPs in Git history**. The release asset is the source of truth. Each future approved/verified version gets its own immutable release ZIP and matching Git tag. Preserve all historical artifacts and retired/changed corpus-file records. Never silently remove, regenerate, rename, normalize, transform, or replace test fixtures.

## Release

See [v2.16 release](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.16) and `RELEASE_NOTES_v2.16.md`. The published v2.16 ZIP is independently re-downloaded and SHA-256 verified by the release workflow. Historical validators and real production-tool runs remain separate from this integrity check. A release must not be considered published or authoritative until its uploaded ZIP is independently downloaded and its complete SHA-256 verified.
