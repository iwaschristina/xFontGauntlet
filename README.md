# xFontGauntlet

**Current font test corpus — v2.11 (G105-03 external-reference fixture repair atop G203)**

xFontGauntlet is a regression corpus for the Font Renamer (x01), Font Converter (x02), Font Finder/Copier (x03), xFontMedic Font Audit/Repair (x04), and associated movers. It includes real, synthetic, unusual, and intentionally malformed fonts; package and folder structures; sidecars and companions; manifests; expected results; and corpus management/validation tools.

## Authoritative distribution

**The complete `xFontGauntlet_v2.11.zip` on the tagged [GitHub Release](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.11) is the current corpus**, not an extracted Git checkout. Intentional ZIP entry spellings, invalid/edge-case path structures, and empty directory records cannot all be represented faithfully in normal Git.

| Property | v2.11 |
| --- | --- |
| Historical baseline | G203 appended to preserved G202 |
| Groups | 201 |
| Declared logical cases | 2,884 |
| Files within archive | 43,687 |
| ZIP directory entries | 10,098 |
| Archive size | 86,898,934 bytes |
| SHA-256 | `53abe5fcfbceb4db22d56ee38baecc90d159c196e879704ccf43f1058fde18f3` |

## G105 external-reference correction

v2.11 repairs the G105-03 positive duplicate-mover fixture so the externally referenced UFO Project folder has its canonical renamer name *before* execution. `ExternalConsumer.designspace` and the fixture contract both refer to that exact folder; the reference remains resolvable through renaming and duplicate moving. The original folder members and original changed JSON/XML records are retained under `Tools/Corpus Contamination Finder/Changed Renamed or Removed Corpus Files/G105_External_Reference_Repair_v2_11/Originals/`. No other active fixtures were changed. Group 13 remains unchanged and intentionally excluded from routine converter runs.

## Contents and use

The ZIP root contains `TestCorpus/` (test groups, font specimens, and related sidecars/packages), `Tools/` (corpus maintenance and validators), and 20 guide, manifest, catalog, and summary files at the root alongside those two directories.

1. Download the **original** ZIP from the matching versioned Release. Do not recompress, extract-and-repackage, rename members, normalize paths, or filter unconventional binary fixtures.
2. Compare SHA-256 against `checksums/v2.11.sha256` using PowerShell `Get-FileHash xFontGauntlet_v2.11.zip -Algorithm SHA256` or `sha256sum xFontGauntlet_v2.11.zip`.
3. Read `00_CURRENT_CORPUS_GUIDE.txt` and `Tools/README_START_HERE.txt` **inside the archive** for detailed organization, groups, expectations and validators.
4. Stage tests in **disposable workspaces** with the included tools when a scenario requires a normal filesystem. Some ZIP paths are intentionally unusual or invalid after extraction on particular filesystems; do not alter the authoritative ZIP to accommodate them.
5. Test the Font Finder/Copier's discovery and sidecar/package preservation, the Converter's outputs, skipping and recovery behavior, the Renamer's identity/duplicate marking, and the movers' atomicity, sidecar ownership, cancellation and rollback. Use the expected results for each case.

The v2.11 release retains all earlier G200–G203 fixtures and retains 17 G203 x02 converter cases from xFontMorph 2.9–2.13: linked/comment-separated Type3 literal-run dependencies; wrapper/raster filename collisions; unsafe dependency traversal and cycles; UFO3 .notdef/Unicode integrity; and Type1 recovery metrics and ambiguous cmap mappings. x01, x03 and x04 functional coverage remains intact. Original root manifest, lock and catalog records are archived at Tools/Corpus Contamination Finder/Changed Renamed or Removed Corpus Files/G203_Post_v2_9_Coverage/Originals/. Group 13 remains unchanged and excluded from routine converter runs. The legacy PowerShell suite still has the same five inherited failures, with zero new failures; see RELEASE_NOTES_v2.11.md. Static corpus-integrity/fixture validation and production-tool runtime acceptance are **different checks**. Packaging a release does not certify that production tools pass all scenarios.

v2.11 preserves the verified v2.10 root layout, all original font fixtures and every Group 13 entry. All earlier releases remain available for historical use.

## Repository policy

This repository stores documentation, integrity records, and release automation, **not an extracted corpus or historical binary ZIPs in Git history**. The release asset is the source of truth. Each future approved/verified version gets its own immutable release ZIP and matching Git tag. Preserve all historical artifacts and retired/changed corpus-file records. Never silently remove, regenerate, rename, normalize, transform, or replace test fixtures.

## Release

See [v2.11 release](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.11) and `RELEASE_NOTES_v2.11.md`. The published v2.11 ZIP is independently re-downloaded and SHA-256 verified by the release workflow. Historical validators and real production-tool runs remain separate from this integrity check. A release must not be considered published or authoritative until its uploaded ZIP is independently downloaded and its complete SHA-256 verified.
