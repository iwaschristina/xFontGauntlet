# xFontGauntlet v2.12 — G204 cross-project regression coverage

**Current authoritative complete release:** [Download xFontGauntlet_v2.12.zip](https://github.com/iwaschristina/xFontGauntlet/releases/download/v2.12/xFontGauntlet_v2.12.zip).

Built directly from the immutable, checksum-verified **v2.11**, retaining its corrected G105-03 external designspace reference and every previous corpus case.

## Full distribution

- **202 groups**, **2,916 declared cases** (32 new)
- **53,976 ZIP entries:** 43,828 files and 10,148 explicit directory entries
- **Archive size:** 90,867,436 bytes
- **SHA-256:** `adb26da2fc0942cd65c31cdbb747755a3c7a0c845d58504f42f53592bc3b25b0`
- The same **20 root metadata/guide files** alongside `TestCorpus/` and `Tools/`.

## New group G204

`TestCorpus/202_G204_Recent_Mover_Converter_Auditor_Regressions/` with IDs `G204-001` through `G204-032`.

**x01 xFontIdentity v2.12 — eight scenarios.** Six duplicate-mover file pairs exercise preservation of physical casing in `.PcF.gZ`, `.OtF.dFoNt`, `.SyM.tTf`, `.CiD.cFf`, `.CiD.t42`, and `.TtF`. A valid unrelated designspace tests safe traversal to the filesystem root without blanket protection. A case-only twin pair exercises ambiguous on-disk name resolution; because the outer corpus disallows case-fold-colliding entries, that pair is preserved in `CaseOnlyTwins.owned.zip` for staging on a case-sensitive filesystem. Files that serve only as mover markers are **not** claimed to be parseable source fonts. The G105-03 positive fixture corrected in v2.11 is unchanged.

**x02 xFontMorph v2.14 — three scenarios.** One physical SFNT with an empty format-10 cmap tests fail-closed semantic validation; a batch of 27 independently parseable positive TTF controls tests per-source terminal-state reconciliation; and an expected-results contract reruns G203's two valid and three invalid UFO mapping cases against the pre-FontForge validation gate. Group 13 remains excluded from routine converter runs.

**x03 xFontHound v2.1.** No newer confirmed font-processing defect; all original Finder/Copier and cross-tool fixtures are retained unchanged.

**x04 xFontMedic v2.0.17 — 21 scenarios.** Positive/negative paired UFO/UFOZ package variants cover optional fontinfo, custom default layer, case-sensitive glyph names, arbitrary UFOZ package root, duplicate glyph keys, shared GLIF filenames, case collisions, invalid glyph value types, and Unicode control characters in glyph/layer names. The intentional case-colliding GLIF pair is UFOZ-only so the authoritative outer ZIP remains casefold unique. New physical PCF tables cover invalid bitmap and encoding offsets; native FNT/FON fixtures cover terminated/unterminated face names and TrueType signature collisions; feature-file sources cover comments, active and include-only references, comment braces, and CR-only line endings.

All new cases have explicit expectations and fixture SHA-256 records. Scenario-driven Windows mover, converter and audit tool runs remain separate acceptance work.

## Preservation and verification

- All **53,807 original v2.11 entries** retain their original ZIP names, order, content and metadata, except three regenerated root records: `CURRENT_CORPUS_MANIFEST.json`, `CORPUS_COVERAGE_LOCK.json`, and `CORPUS_CATALOG.json`.
- The exact originals of those three modified records are archived under `Tools/Corpus Contamination Finder/Changed Renamed or Removed Corpus Files/G204_Post_v2_11_Coverage/Originals/`.
- All **22,109 Group 13 entries** are unchanged. The existing G105 fix and prior positive UFO3 fixtures are also preserved.
- ZIP CRC, physical fixtures, source cases, and current manifest/lock/catalog checks **PASS**.
- The fully published asset was **independently re-downloaded** and SHA-256 verified. Every unchanged earlier member was compared by metadata and hash.
- The existing historical PowerShell integrity validator was run against both v2.11 and v2.12. **Both have the same six pre-existing failures**: G105 (legacy validator's designspace expectation), G80, G83, G109, G116, and unavailable `Get-Sha256`. After normalizing only version-specific staging directories in the diagnostic, **no new failures** occurred. The full historical validator suite therefore still does **not** pass.
- Full production Windows x01–x04 execution has **not** been performed in this packaging run.

[Release details](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.12).
