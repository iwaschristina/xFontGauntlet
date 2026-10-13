# xFontGauntlet

**Current font test corpus — v2.7 (G200 UFO3 repairs atop G199)**

xFontGauntlet is a regression corpus for the Font Renamer (x01), Font Converter (x02), Font Finder/Copier (x03), xFontMedic Font Audit/Repair (x04), and associated movers. It includes real, synthetic, unusual, and intentionally malformed fonts; package and folder structures; sidecars and companions; manifests; expected results; and corpus management/validation tools.

## Authoritative distribution

**The complete `xFontGauntlet_v2.7.zip` on the tagged [GitHub Release](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.7) is the current corpus**, not an extracted Git checkout. Intentional ZIP entry spellings, invalid/edge-case path structures, and empty directory records cannot all be represented faithfully in normal Git.

| Property | v2.7 |
| --- | --- |
| Historical baseline | G200 repair of G199 (case count unchanged) |
| Groups | 198 |
| Declared logical cases | 2,822 |
| Files within archive | 43,518 |
| ZIP directory entries | 10,021 |
| Archive size | 70,623,043 bytes |
| SHA-256 | `5c1bfd53b65b8e29d228fb5142c6f813b2e16fb3075f896d896822712e5e89da` |

## Contents and use

The ZIP root contains `TestCorpus/` (test groups, font specimens, and related sidecars/packages), `Tools/` (corpus maintenance and validators), and 20 guide, manifest, catalog, and summary files at the root alongside those two directories.

1. Download the **original** ZIP from the matching versioned Release. Do not recompress, extract-and-repackage, rename members, normalize paths, or filter unconventional binary fixtures.
2. Compare SHA-256 against `checksums/v2.7.sha256` using PowerShell `Get-FileHash xFontGauntlet_v2.7.zip -Algorithm SHA256` or `sha256sum xFontGauntlet_v2.7.zip`.
3. Read `00_CURRENT_CORPUS_GUIDE.txt` and `Tools/README_START_HERE.txt` **inside the archive** for detailed organization, groups, expectations and validators.
4. Stage tests in **disposable workspaces** with the included tools when a scenario requires a normal filesystem. Some ZIP paths are intentionally unusual or invalid after extraction on particular filesystems; do not alter the authoritative ZIP to accommodate them.
5. Test the Font Finder/Copier's discovery and sidecar/package preservation, the Converter's outputs, skipping and recovery behavior, the Renamer's identity/duplicate marking, and the movers' atomicity, sidecar ownership, cancellation and rollback. Use the expected results for each case.

The v2.7 release repairs three valid positive UFO3 rename cases (G197-001, G197-019, G198-002), adds their missing default layer declarations, and regenerates dependent current manifests, locks and expected results. Original replaced metadata is archived in Tools/Corpus Contamination Finder/Changed Renamed or Removed Corpus Files/G200_Repaired_Positive_UFO3/Originals/. Group 13 is preserved and remains excluded from routine x02 converter runs. The historical PowerShell integrity suite was run but still reports five unrelated legacy failures; see RELEASE_NOTES_v2.7.md. Static corpus-integrity/fixture validation and production-tool runtime acceptance are **different checks**. Packaging a release does not certify that production tools pass all scenarios.

v2.7 preserves the verified v2.6 root layout, all original font fixtures and every Group 13 entry. All earlier releases remain available for historical use.

## Repository policy

This repository stores documentation, integrity records, and release automation, **not an extracted corpus or historical binary ZIPs in Git history**. The release asset is the source of truth. Each future approved/verified version gets its own immutable release ZIP and matching Git tag. Preserve all historical artifacts and retired/changed corpus-file records. Never silently remove, regenerate, rename, normalize, transform, or replace test fixtures.

## Release

See [v2.7 release](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.7) and `RELEASE_NOTES_v2.7.md`. The published v2.7 ZIP passed an independent re-download and full-file SHA-256 verification. Historical validators and real production-tool runs remain separate from this integrity check. A release must not be considered published or authoritative until its uploaded ZIP is independently downloaded and its complete SHA-256 verified.
