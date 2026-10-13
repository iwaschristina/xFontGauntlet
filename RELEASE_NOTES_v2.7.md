# xFontGauntlet v2.7 — G200 UFO 3 fixture repair

**Current full corpus release** built from exact published xFontGauntlet v2.6/G199 (SHA-256 `198e90e427f7b18088d1d7cfcc23a1853db8a8bb885510fba6d21738d8378377`).

**Download:** [xFontGauntlet_v2.7.zip](https://github.com/iwaschristina/xFontGauntlet/releases/download/v2.7/xFontGauntlet_v2.7.zip)

- 198 test groups and 2,822 declared regression cases (no case IDs changed).
- 53,539 ZIP entries (43,518 files and 10,021 explicit directory entries).
- 70,623,043 bytes.
- SHA-256: `5c1bfd53b65b8e29d228fb5142c6f813b2e16fb3075f896d896822712e5e89da`.
- Root still contains the 20 guide, manifest, and catalog files alongside `TestCorpus/` and `Tools/`.

## Targeted repairs

The following **positive** x01 UFO renaming fixtures now have a valid UFO format 3 `layercontents.plist` containing the default layer mapping `[["public.default", "glyphs"]]`:

| Test ID | Package | Expected behavior |
| --- | --- | --- |
| G197-001 | `Opaque_Source.ufo` | Successful package rename |
| G197-019 | `Finder_Copied_Set.ufo` | Successful Finder-copied package rename |
| G198-002 | `NestedFinderSet.ufo` | Successful atomic nested UFO rename, including the intended 248-character boundary |

The G198-002 declaration was tightened: early refusal is **not** accepted as success. All three packages were parsed using `fontTools.ufoLib.UFOReader`; their UFO3 version, glyph directory, `contents.plist`, and referenced `A.glif` are valid. Original glyph bytes, `metainfo.plist`, `fontinfo.plist`, family identities and folder relationships are unchanged.

Updated dependent G197/G198 expected-results records, the current `CURRENT_CORPUS_MANIFEST.json`, the `CORPUS_COVERAGE_LOCK.json` integrity lock, and `CORPUS_CATALOG.json`.

Original byte-for-byte copies of **all five replaced metadata files** are preserved in the corpus's designated archive:
`Tools/Corpus Contamination Finder/Changed Renamed or Removed Corpus Files/G200_Repaired_Positive_UFO3/Originals/`.
The same folder contains the repair log and the UFO structural validation record.

## Verification result and limits

**PASS**: Full ZIP integrity and independent GitHub re-download SHA-256; three UFO3 structural validations; exact G197/G198 positive expectation records; all unrelated ZIP member contents and metadata preserved; Group 13 unchanged (22,109 original entries); active manifest and lock records coherent.

**NOT PASSING**: The historical PowerShell integrity suite was executed but returned five separate legacy failures: G80 mixed-root check, G83 renamer version sync, G109 SFDir header control, G116 index-generation target, and undefined `Get-Sha256`. These do not identify a change to one of the three target UFO packages. The original v2.6 runner already failed due to its stale coverage-lock schema. Broader historical Python validators also cannot all be independently certified using a uniform invocation; they have heterogeneous legacy contracts.

**NOT EXECUTED**: The native Windows xFontIdentity v2.2 Renamer workflow, so the positive rename runtime outcome remains to be confirmed by the next actual run. The corpus packaging and structural PASS is not a runtime certification.

Group 13 remains excluded from routine converter test runs as previously required.

[View full release](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.7).
