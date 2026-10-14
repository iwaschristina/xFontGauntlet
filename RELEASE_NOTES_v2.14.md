# xFontGauntlet v2.14 — G206 signature-probe and converter regression expansion

**Complete authoritative release:** [xFontGauntlet_v2.14.zip](https://github.com/iwaschristina/xFontGauntlet/releases/download/v2.14/xFontGauntlet_v2.14.zip).

Built from the exact independently verified **v2.13/G205** full ZIP, preserving every earlier fixture including the corrected G105 designspace, G197/G198 positive UFO3 fixtures, and all of Group 13.

## Complete distribution

- **204 groups** and **2,938 declared logical cases**, including **18 new G206 cases**.
- **54,048 ZIP entries:** 43,885 files and 10,163 explicit directories.
- **Archive size:** 98,807,621 bytes.
- **SHA-256:** `219fed0da2923ba7510fdd4e9d4c93d2687c42181ac51f1b723ef7f2c22ddf29`.
- The same 20 root guide/metadata files alongside `TestCorpus/` and `Tools/`.

## New G206 fixtures

The new group is `TestCorpus/204_G206_Signature_Probe_Cmap_And_Converter_Observed_Regressions/`.

**x01 — xFontIdentity v2.14 (5 scenarios):** no redundant extensionless signature probes for normal `.otf` and `.woff2` source files; SFNT+WOFF2 probe eligibility for true extensionless SFNT sources; only SFNT probe for a metadata-style `Family [Version 1.0]` apparent extension; and full probe tracing for known-extension fonts when detailed diagnostic mode is enabled. Source files are physically included, not merely named in expected-results lists.

**x02 — xFontMorph v2.15 (13 scenarios):** 10 real SFNT containers with controlled raw Unicode cmap subtables, testing formats 4, 6, 10, 12 and 13, mapped-surrogate rejection, glyph-zero unmapped-surrogate acceptance, and a genuine nonempty format-10 positive control. The ten physical cases were tested against exact copies of the **production xFontMorph v2.15 Unicode source-validation functions**, not only decoded by fontTools.

Three additional scenario contracts preserve the precise observed converter-run findings:
- `TestCorpus/01_Valid_By_Extension/otb/Valid_Content_Route_Probe.otb` was rejected despite nominally valid PostScript content. The original fixture is retained and a content-route-versus-worker diagnostic regression contract was added.
- `TestCorpus/116_Post_G115_X01_X04_Regressions_And_Converted_Lineage/Cases/08_MoveConverted_v87_v91_Cmap_Subtables/Outputs/TruncatedFormat8.ttf` previously terminated a batch prematurely. The expected behavior is per-source rejection and continued processing of subsequent inputs.
- Recent converter output contained seven G203 Type3 Ghostscript failures and unexpectedly published outputs for malformed UFO sources. New contracts require checking source renderability and worker diagnostics without silently changing positive expectations, and require semantic rejection of invalid UFOs before publication.

**Important distinction:** an accepted raw Unicode cmap preflight test is not automatically a valid full-conversion test. Synthetic fonts are explicitly marked `preflight-only` where appropriate, and application-level Windows conversion claims remain unverified.

**x03 and x04:** no new processing changes requiring additional cases since G205; all existing Finder and auditor coverage is retained.

## Preservation and verification

- All **54,003 previous v2.13 ZIP entries** retain their original names, order and metadata. Only `CURRENT_CORPUS_MANIFEST.json`, `CORPUS_COVERAGE_LOCK.json` and `CORPUS_CATALOG.json` were regenerated. Exact byte originals are stored under `Tools/Corpus Contamination Finder/Changed Renamed or Removed Corpus Files/G206_Post_v2_13_Coverage/Originals/`.
- All **22,109 Group 13 entries** are unchanged and Group 13 remains excluded from routine x02 converter runs.
- Full ZIP CRC and manifest/hash integrity, strict case-insensitive outer-path uniqueness, source cmap semantics against the current production v2.15 guard code, and byte-for-byte comparison of every unchanged prior ZIP member passed.
- The published v2.14 asset was independently re-downloaded; its SHA-256 matched the deterministic candidate exactly.
- The historical PowerShell integrity validator was run on both complete v2.13 and v2.14 ZIPs. Both have the **same six inherited failures**, with **zero new failures**. Therefore the historical suite does **not** pass overall.
- Native Windows x01–x04 production application runs were not part of this packaging verification.

[Release page](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.14).
