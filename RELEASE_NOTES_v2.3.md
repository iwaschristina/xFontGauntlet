# xFontGauntlet v2.3 (G198)

Current complete corpus, correcting the packaging of v2.2 while preserving the original v2.1/G197 corpus contents unchanged.

- **197 groups**
- **2,810 declared regression cases**
- **43,354 files and 10,003 explicit directory entries** (53,357 ZIP entries)
- ZIP size **66,664,667 bytes**
- SHA-256: `49c20f39458d2b4da018418e3e888733928084c78d8c1ec7ddd138def4ba5e6c`

This full archive includes 20 new G198 scenarios across x01 Rename Fonts, x02 Convert Fonts, x03 Font Finder/Copier and x04 xFontMedic Font Audit/Repair.

**x01:** input path below 248 chars with derived destination beyond 248; folder package atomicity, rollback, lossless representative recovery and shorter-destination controls.

**x02:** valid TTF comparison pair differing solely in volatile `head.modified`; negative controls differing in `glyf` outlines or `name` identity; stale output isolation.

**x03:** Finder-to-xFontMedic handoff of WOFF2 and AppleDouble/TTF package companions with exact hash preservation.

**x04:** AppleDouble bounded parsing and corruption diagnostics, corrupt CFF/PFB handling, valid WOFF2 with and without Brotli decoder, and idempotent report-only/no-op repair behavior.

The manifest and fixture digests are inside `TestCorpus/197_Recent_X01_X04_Regression_Cases_20261013/EXPECTED_RESULTS.json`.

## Integrity and history
The published v2.1 ZIP (53,303 entries) was downloaded by the builder, SHA-verified, and every earlier ZIP member was checked for unchanged contents and metadata. Exactly **54** group-specific entries were appended; no unrelated or duplicate directory member was added. An independent job downloads v2.3 and compares it again against v2.1.

v2.3 **supersedes v2.2**, whose initial package had an unnecessary duplicate `TestCorpus/` directory entry. Both earlier releases remain available for historical traceability.

Historical 78-validator suite and live x01–x04 runtime acceptance checks have not been rerun for this release. Group 13 remains intentionally excluded from routine converter testing.
