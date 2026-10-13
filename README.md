# xFontGauntlet

**Current font test corpus — v2.1 (G197 lineage)**

xFontGauntlet is a regression corpus for the Font Renamer, Font Converter, Font Finder/Copier, and their associated movers. It includes real, synthetic, unusual, and intentionally malformed fonts; package and folder structures; sidecars and companions; manifests; expected results; and corpus management/validation tools.

## Authoritative distribution

**The complete `xFontGauntlet_v2.1.zip` on the tagged [GitHub Release](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.1) is the current corpus**, not an extracted Git checkout. Intentional ZIP entry spellings, invalid/edge-case path structures, and empty directory records cannot all be represented faithfully in normal Git.

| Property | v2.1 |
| --- | --- |
| Historical baseline | G197 (G196 plus 22 cases) |
| Groups | 196 |
| Declared logical cases | 2,790 |
| Files within archive | 43,321 |
| ZIP directory entries | 9,982 |
| Archive size | 66,636,450 bytes |
| SHA-256 | `618278f1eca218bdd3b0221ce95883c54b16e2794f1a7452ed3ccadb4791c1f3` |

## Contents and use

The archive contains `TestCorpus/` (test groups, font specimens, related sidecars/package members, expected-results definitions, and catalogs) and `Tools/` (corpus maintenance, staging, manifests, and verification utilities).

1. Download the **original** ZIP from the matching versioned Release. Do not recompress, extract-and-repackage, rename members, normalize paths, or filter unconventional binary fixtures.
2. Compare SHA-256 against `checksums/v2.1.sha256` using PowerShell `Get-FileHash xFontGauntlet_v2.1.zip -Algorithm SHA256` or `sha256sum xFontGauntlet_v2.1.zip`.
3. Read `TestCorpus/00_CURRENT_CORPUS_GUIDE.txt` and `Tools/README_START_HERE.txt` **inside the archive** for detailed organization, groups, expectations and validators.
4. Stage tests in **disposable workspaces** with the included tools when a scenario requires a normal filesystem. Some ZIP paths are intentionally unusual or invalid after extraction on particular filesystems; do not alter the authoritative ZIP to accommodate them.
5. Test the Font Finder/Copier's discovery and sidecar/package preservation, the Converter's outputs, skipping and recovery behavior, the Renamer's identity/duplicate marking, and the movers' atomicity, sidecar ownership, cancellation and rollback. Use the expected results for each case.

The v2.1 release adds 22 G197 regression assertions to the unchanged G196 baseline; see the group's EXPECTED_RESULTS.json inside the ZIP. The previously bundled 78 historical validators have not been rerun against v2.1. Static corpus-integrity/fixture validation and production-tool runtime acceptance are **different checks**. Packaging a release does not certify that production tools pass all scenarios.

## Repository policy

This repository stores documentation, integrity records, and release automation, **not an extracted corpus or historical binary ZIPs in Git history**. The release asset is the source of truth. Each future approved/verified version gets its own immutable release ZIP and matching Git tag. Preserve all historical artifacts and retired/changed corpus-file records. Never silently remove, regenerate, rename, normalize, transform, or replace test fixtures.

## Release

See [v2.1 release](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.1) and `RELEASE_NOTES_v2.1.md`. The published v2.1 ZIP passed an independent re-download and full-file SHA-256 verification. Historical validators and real production-tool runs remain separate from this integrity check. A release must not be considered published or authoritative until its uploaded ZIP is independently downloaded and its complete SHA-256 verified.
