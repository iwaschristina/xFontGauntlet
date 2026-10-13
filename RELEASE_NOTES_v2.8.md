# xFontGauntlet v2.8 — G201 cross-project coverage

The complete authoritative v2.7/G200 corpus was retained and expanded using confirmed October 13 findings from x01 Rename Fonts, x02 Convert Fonts, x03 Font Finder/Copier and x04 xFontMedic Font Audit/Repair.

## Complete ZIP

- **Release:** [xFontGauntlet v2.8](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.8)
- **Download:** [xFontGauntlet_v2.8.zip](https://github.com/iwaschristina/xFontGauntlet/releases/download/v2.8/xFontGauntlet_v2.8.zip)
- **Groups:** 199 (prior 198 plus Group 199/G201)
- **Declared cases:** 2,844 (prior 2,822 plus 22)
- **ZIP entries:** 53,602 (43,561 files, 10,041 directories)
- **Archive size:** 74,597,059 bytes
- **SHA-256:** `3b8b27fb6242ee14f92bf41a0e1490577040198171184384e200a51f33b172ac`
- **Root layout:** the same 20 guide, manifest and catalog files alongside `TestCorpus/` and `Tools/`

## New regression group

`TestCorpus/199_G201_LongPath_Discovery_Recovery_And_Headless_Audit/`

**x01 xFontIdentity (7 cases).** Extended-vs-ordinary path representation for deeply nested included and excluded source files; package-aware and unrecognized extension handling; valid UFO3 packages in deeply nested directories; package-descendant basename/path length budgeting (v2.4); self/target duplicate-representative alias suppression and unrelated representative rejection.

**x02 xFontMorph (9 cases).** Previously confirmed G198 long-path positive-font rejection patterns, now covered by additional parseable TTF/OTF and WOFF2 fixtures; deep drive-letter/UNC metadata and SHA-256, missing-file Win32 2/3 handling, host webfont recovery, valid-output provenance, output changes between compare and publish, safe extended path copy/move/replace, truncated output rejection and reparse-point safety. Test stage requires measuring the actual absolute Windows path between 260 and 495 characters.

**x03 xFontHound.** The newest changes concerned GitHub packaging and source organization rather than a new font-processing defect. Earlier Finder, package and cross-tool regression cases are retained without duplicate new cases.

**x04 xFontMedic (6 cases).** Headless `-NoGui` operation on empty and corrupt roots, seven reports and COMPLETE state without auto-opening a report, valid TTF idempotence, and optional Python 3 interpreter selection after rejecting nonworking aliases, Python 2 and timed-out executables. The run matrix is a synthetic regression contract, not a claim that native executable shims or runtime tests have executed.

The G201 manifest contains test IDs `G201-001` through `G201-022`, explicit expected outcomes and fixture SHA-256 hashes. All new parseable fonts and the valid UFO3 fixture passed static parsing.

## Preservation and verification

- All 53,539 v2.7 ZIP entries are preserved in order with exact paths and metadata; only the three dependent root metadata files changed.
- Original `CURRENT_CORPUS_MANIFEST.json`, `CORPUS_COVERAGE_LOCK.json` and `CORPUS_CATALOG.json` are archived unchanged at `Tools/Corpus Contamination Finder/Changed Renamed or Removed Corpus Files/G201_Post_v2_7_Coverage/Originals/`.
- Current manifest and coverage lock were regenerated for the added group.
- All 22,109 Group 13 ZIP entries are unchanged. Group 13 remains intentionally excluded from routine x02 converter testing.
- The full published v2.8 ZIP passed an independent GitHub re-download, complete SHA-256 and ZIP CRC verification, original-entry comparison and new fixture manifest/hash checks.
- The existing PowerShell integrity suite was executed against both complete v2.7 and v2.8. Both report the **same five inherited failures** (G80, G83, G109, G116, and undefined `Get-Sha256`); **zero new legacy validation failures** were introduced. The suite as a whole does **not pass**.
- Full Windows production x01–x04 tests and all other historical validators were **not** executed as part of this packaging verification.

The G201 fixtures are intended to be staged into disposable Windows workspaces under the `TestCorpus/` test root, not the ZIP extraction parent. Historical versions and earlier release assets remain available unchanged.
