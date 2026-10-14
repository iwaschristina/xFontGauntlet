# xFontGauntlet v2.13 (G205) — xFontMedic format-boundary controls

**Authoritative complete ZIP:** [xFontGauntlet_v2.13.zip](https://github.com/iwaschristina/xFontGauntlet/releases/download/v2.13/xFontGauntlet_v2.13.zip). Built from the exact, SHA-256-verified, independently published **v2.12/G204** baseline, not an extracted Git checkout.

## Release accounting

- **203 groups**, **2,920 declared logical cases**, including **four new G205 cases**.
- **54,003 ZIP entries**: 43,846 files and 10,157 directory records.
- **ZIP size:** 94,827,527 bytes.
- **SHA-256:** `881d5886f52e9b27fa78370ad09cd617c1473946c510f84c3e19291e29d67df1`.
- Outer root layout unchanged: twenty root-level metadata/guide files beside `TestCorpus/` and `Tools/`.

## Newly isolated regression gaps

All four cases are under `TestCorpus/203_G205_Auditor_Format_Boundary_Positive_Negative/` and target x04 xFontMedic v2.0.17.

- **G205-001 — incorrect UFO3 layer ownership.** Both a physical directory UFO and a corresponding UFOZ include valid glyph data in both `glyphs/` and `glyphs.other/`. However, `public.default` owns `glyphs.other` and the alternate layer owns `glyphs`. **Expected CORRUPT** for both forms; test is not conflated with missing glyph files.
- **G205-002 — multiple well-formed UFOZ roots.** Two independently valid roots (`FirstContainer/` and `SecondContainer/`) occur in one UFOZ. **Expected CORRUPT** because the package must contain exactly one root, even though the root may have any valid name. The positive arbitrary-root counterexample remains in G204.
- **G205-003 — positive native PFM/SFNT signature collision.** The file is a 131072-byte PFM 1.0 whose first four bytes are `00 01 00 00` (also the TrueType SFNT signature), with a bounded face-name pointer at offset 100000. **Expected VALID native PFM**, not TrueType.
- **G205-004 — out-of-range PFM name pointer.** Identical native-looking PFM header with a face-name pointer of `0xffffffff`, beyond the physical file length. **Expected CORRUPT** with bounded validation.

These cases are based on specific xFontMedic v2.0.6–v2.0.17 regression rules not separately isolated in G202/G204. x01 xFontIdentity v2.12, x02 xFontMorph v2.14, and x03 xFontHound v2.1 had no newer confirmed processing changes beyond the already-published G204 coverage, and their complete prior cases remain unchanged.

## Preservation

- The complete ZIP preserves **all 53,976 original v2.12 ZIP entries** with identical paths, ordering and member metadata. The only three earlier entries with regenerated data are `CURRENT_CORPUS_MANIFEST.json`, `CORPUS_COVERAGE_LOCK.json`, and `CORPUS_CATALOG.json`.
- Exact byte originals of the three regenerated records are archived under `Tools/Corpus Contamination Finder/Changed Renamed or Removed Corpus Files/G205_Post_v2_12_Coverage/Originals/`.
- The G105 corrected positive external designspace fixture, all G197/G198 repaired positive UFO fixtures, and every earlier positive/negative expected result remain intact.
- **All 22,109 Group 13 ZIP entries are unchanged.** Group 13 remains excluded from routine x02 converter runs.

## Verification status

The full archive passes ZIP CRC, declared fixture SHA-256, strict outer ZIP case-fold uniqueness, metadata/coverage-lock coherence, G205 physical-format checks, and deterministic SHA-256 rebuild. The published release was then **independently re-downloaded**, its SHA-256 verified, and every old ZIP member compared; all three original metadata records were verified in their archive locations.

The existing PowerShell historical integrity suite was run against complete v2.12 and v2.13. Both report **the same six inherited failures**, including the G105 legacy-expected-reference check, G80, G83, G109, G116 and missing `Get-Sha256`. After normalizing only different extraction-root paths, **zero new failures** were introduced. Thus the historical integrity suite as a whole does **not pass**.

Live x01–x04 Windows applications were not executed as part of this corpus packaging; adding expected-positive or expected-negative fixtures does not independently certify production-tool behavior.

[GitHub Release](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.13).
