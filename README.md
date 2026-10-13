# xFontGauntlet

**Current font test corpus — v2.6 (G199 lineage)**

xFontGauntlet is a regression corpus for the Font Renamer (x01), Font Converter (x02), Font Finder/Copier (x03), xFontMedic Font Audit/Repair (x04), and associated movers. It includes real, synthetic, unusual, and intentionally malformed fonts; package and folder structures; sidecars and companions; manifests; expected results; and corpus management/validation tools.

## Authoritative distribution

**The complete `xFontGauntlet_v2.6.zip` on the tagged [GitHub Release](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.6) is the current corpus**, not an extracted Git checkout. Intentional ZIP entry spellings, invalid/edge-case path structures, and empty directory records cannot all be represented faithfully in normal Git.

| Property | v2.6 |
| --- | --- |
| Historical baseline | G199 (G198 plus 12 cases) |
| Groups | 198 |
| Declared logical cases | 2,822 |
| Files within archive | 43,508 |
| ZIP directory entries | 10,016 |
| Archive size | 66,755,932 bytes |
| SHA-256 | `198e90e427f7b18088d1d7cfcc23a1853db8a8bb885510fba6d21738d8378377` |

## Contents and use

The ZIP root contains `TestCorpus/` (test groups, font specimens, and related sidecars/packages), `Tools/` (corpus maintenance and validators), and 20 guide, manifest, catalog, and summary files at the root alongside those two directories.

1. Download the **original** ZIP from the matching versioned Release. Do not recompress, extract-and-repackage, rename members, normalize paths, or filter unconventional binary fixtures.
2. Compare SHA-256 against `checksums/v2.6.sha256` using PowerShell `Get-FileHash xFontGauntlet_v2.6.zip -Algorithm SHA256` or `sha256sum xFontGauntlet_v2.6.zip`.
3. Read `00_CURRENT_CORPUS_GUIDE.txt` and `Tools/README_START_HERE.txt` **inside the archive** for detailed organization, groups, expectations and validators.
4. Stage tests in **disposable workspaces** with the included tools when a scenario requires a normal filesystem. Some ZIP paths are intentionally unusual or invalid after extraction on particular filesystems; do not alter the authoritative ZIP to accommodate them.
5. Test the Font Finder/Copier's discovery and sidecar/package preservation, the Converter's outputs, skipping and recovery behavior, the Renamer's identity/duplicate marking, and the movers' atomicity, sidecar ownership, cancellation and rollback. Use the expected results for each case.

The v2.6 release retains all G197/G198 cases and the v2.5 root layout while adding 12 G199 regression scenarios for x01 Renamer scaling/diagnostics and x02 Converter run-state/output consistency. See TestCorpus/198_G199_Run_Diagnostics_Subset_Scaling_And_Conversion_Lifecycle/EXPECTED_RESULTS.json. Group 13 remains excluded from routine x02 tests. The 78 historical validators have not been rerun against v2.6. Static corpus-integrity/fixture validation and production-tool runtime acceptance are **different checks**. Packaging a release does not certify that production tools pass all scenarios.

v2.6 preserves the verified v2.5 root layout and every original ZIP entry. All earlier releases remain available for historical use.

## Repository policy

This repository stores documentation, integrity records, and release automation, **not an extracted corpus or historical binary ZIPs in Git history**. The release asset is the source of truth. Each future approved/verified version gets its own immutable release ZIP and matching Git tag. Preserve all historical artifacts and retired/changed corpus-file records. Never silently remove, regenerate, rename, normalize, transform, or replace test fixtures.

## Release

See [v2.6 release](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.6) and `RELEASE_NOTES_v2.6.md`. The published v2.6 ZIP passed an independent re-download and full-file SHA-256 verification. Historical validators and real production-tool runs remain separate from this integrity check. A release must not be considered published or authoritative until its uploaded ZIP is independently downloaded and its complete SHA-256 verified.
