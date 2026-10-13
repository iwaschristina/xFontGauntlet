# xFontGauntlet

**Current font test corpus — v2.5 (G198 lineage)**

xFontGauntlet is a regression corpus for the Font Renamer (x01), Font Converter (x02), Font Finder/Copier (x03), xFontMedic Font Audit/Repair (x04), and associated movers. It includes real, synthetic, unusual, and intentionally malformed fonts; package and folder structures; sidecars and companions; manifests; expected results; and corpus management/validation tools.

## Authoritative distribution

**The complete `xFontGauntlet_v2.5.zip` on the tagged [GitHub Release](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.5) is the current corpus**, not an extracted Git checkout. Intentional ZIP entry spellings, invalid/edge-case path structures, and empty directory records cannot all be represented faithfully in normal Git.

| Property | v2.5 |
| --- | --- |
| Historical baseline | G198 (G197 plus 20 cases) |
| Groups | 197 |
| Declared logical cases | 2,810 |
| Files within archive | 43,354 |
| ZIP directory entries | 10,003 |
| Archive size | 66,663,855 bytes |
| SHA-256 | `0a6c76c3c158f8dd05aae78b15e227afa7c16c919659364fdfcaa7a571a159f9` |

## Contents and use

The ZIP root contains `TestCorpus/` (test groups, font specimens, and related sidecars/packages), `Tools/` (corpus maintenance and validators), and 20 guide, manifest, catalog, and summary files at the root alongside those two directories.

1. Download the **original** ZIP from the matching versioned Release. Do not recompress, extract-and-repackage, rename members, normalize paths, or filter unconventional binary fixtures.
2. Compare SHA-256 against `checksums/v2.5.sha256` using PowerShell `Get-FileHash xFontGauntlet_v2.5.zip -Algorithm SHA256` or `sha256sum xFontGauntlet_v2.5.zip`.
3. Read `00_CURRENT_CORPUS_GUIDE.txt` and `Tools/README_START_HERE.txt` **inside the archive** for detailed organization, groups, expectations and validators.
4. Stage tests in **disposable workspaces** with the included tools when a scenario requires a normal filesystem. Some ZIP paths are intentionally unusual or invalid after extraction on particular filesystems; do not alter the authoritative ZIP to accommodate them.
5. Test the Font Finder/Copier's discovery and sidecar/package preservation, the Converter's outputs, skipping and recovery behavior, the Renamer's identity/duplicate marking, and the movers' atomicity, sidecar ownership, cancellation and rollback. Use the expected results for each case.

The v2.5 release retains all G197 and G198 regression cases. It relocates 20 metadata files from TestCorpus/ to the ZIP root and updates two validation scripts to find the relocated manifests; every font fixture remains unchanged. See TestCorpus/197_Recent_X01_X04_Regression_Cases_20261013/EXPECTED_RESULTS.json. The 78 historical validators have not been rerun against v2.5. Static corpus-integrity/fixture validation and production-tool runtime acceptance are **different checks**. Packaging a release does not certify that production tools pass all scenarios.

v2.5 supersedes v2.4 for its two validator lookup repairs, and preserves the same requested ZIP root layout. Earlier versions remain available as historical releases.

## Repository policy

This repository stores documentation, integrity records, and release automation, **not an extracted corpus or historical binary ZIPs in Git history**. The release asset is the source of truth. Each future approved/verified version gets its own immutable release ZIP and matching Git tag. Preserve all historical artifacts and retired/changed corpus-file records. Never silently remove, regenerate, rename, normalize, transform, or replace test fixtures.

## Release

See [v2.5 release](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.5) and `RELEASE_NOTES_v2.5.md`. The published v2.5 ZIP passed an independent re-download and full-file SHA-256 verification. Historical validators and real production-tool runs remain separate from this integrity check. A release must not be considered published or authoritative until its uploaded ZIP is independently downloaded and its complete SHA-256 verified.
