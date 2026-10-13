# xFontGauntlet v2.6 (G199)

Current full corpus, preserving the exact published v2.5/G198 ZIP contents and root layout while appending one focused G199 regression group derived from the October 12–13 x01–x04 project reviews.

## Complete archive

- **198 groups**, **2,822 declared logical cases**.
- **43,508 files** and **10,016 explicit ZIP directory entries** (53,524 total ZIP entries).
- **167 new entries**, including 154 new files and 13 directory entries, with 12 new declared test cases.
- Filename: `xFontGauntlet_v2.6.zip`.
- Size: **66,755,932 bytes**.
- SHA-256: `198e90e427f7b18088d1d7cfcc23a1853db8a8bb885510fba6d21738d8378377`.
- Root still contains the same 20 guide/catalog/manifest files beside `TestCorpus/` and `Tools/`.

## New group

`TestCorpus/198_G199_Run_Diagnostics_Subset_Scaling_And_Conversion_Lifecycle/`

**x01 — six scenarios**: 16- and 64-file corrupt-font cohorts to measure diagnostic amplification, valid font pair comparison workloads of 8 and 32 inputs, mixed corrupt/valid planning continuity, and repeat-run stability. Error-volume and performance expectations are relative/instrumented, not fixed hardware-dependent runtimes.

**x02 — six scenarios**: a clean FontForge process exit without verified conversion completion, zero-length output despite nominal success, parseable stale output from an earlier run, two different sources targeting one output, interrupted/torn journal records, and mixed failed outputs after clean worker exit. Event JSONL files are synthetic adapter fixtures, not asserted to be native application logs.

**x03 / x04**: no new confirmed font-processing defects in the latest conversations beyond G197/G198, so their existing tests remain intact.

Group 13 remains intentionally **excluded from routine x02 Converter runs**. G199's x01 corruption stress cohorts are separate and explicitly scoped to the Renamer.

## Verification

The builder checked the exact published v2.5 SHA-256 and compared every one of its 53,357 ZIP members (metadata and uncompressed SHA-256). All earlier entries were preserved unchanged and 167 group-specific entries appended. A separate GitHub Actions job independently downloaded both published releases, checked the full SHA-256 and archive CRCs, verified all 12 case declarations and their fixtures, and confirmed the 20-file ZIP root layout. Both jobs passed.

This is a static corpus integrity result, not an x01–x04 Windows runtime acceptance certification. The bundled historical 78-validator suite has not been rerun in this packaging step.

[Download complete v2.6 corpus](https://github.com/iwaschristina/xFontGauntlet/releases/download/v2.6/xFontGauntlet_v2.6.zip).
