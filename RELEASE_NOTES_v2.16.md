# xFontGauntlet v2.16 — Optional Group 13 archive (G207 preserved)

**Authoritative complete ZIP:** [Download xFontGauntlet_v2.16.zip](https://github.com/iwaschristina/xFontGauntlet/releases/download/v2.16/xFontGauntlet_v2.16.zip).

This is a **storage-layout successor** to the independently published v2.15 (G207) ZIP. No cases were added or removed. All 31 new G207 regression cases from v2.15, and all earlier fixtures, remain unchanged.

## How to use Group 13

By default, extracting the complete v2.16 ZIP does **not** populate `TestCorpus/13_Corruption_Matrix_All_Font_Types/`. This is intentional: it reduces normal extraction and general regression scanning by 21,633 archive entries.

Group 13 is available inside the complete ZIP at:

`Tools/Optional Test Groups/Group13_Corruption_Matrix_All_Font_Types.zip`

**To run Group 13:** first extract the complete xFontGauntlet ZIP. Then extract the optional Group 13 ZIP **into that extracted `TestCorpus/` directory**. Its internal paths start with `13_Corruption_Matrix_All_Font_Types/`, so this recreates the exact original `TestCorpus/13_Corruption_Matrix_All_Font_Types/` folder structure. When finished, keep Group 13 out of the ordinary test workspace to maintain faster routine scans.

A copy of these instructions is also at `Tools/Optional Test Groups/README_Group13.txt` inside the full ZIP.

## Counts and integrity

| Property | Verified value |
| --- | ---: |
| Groups, including optional Group 13 | 205 |
| Declared logical cases | 2,969 |
| Outer ZIP entries | 32,510 |
| Outer files | 22,516 |
| Outer explicit directories | 9,994 |
| Extracted/default `TestCorpus/` file entries | 22,299 |
| Group 13 optional inner ZIP members | 21,633 |
| Outer archive size | 98,917,857 bytes |
| Outer archive SHA-256 | `0ec01f19b126e33a4abb4cb028a3ead38900c5348376685cc2e742ba30e84665` |

A previous loose regular-expression check counted 22,109 entries with an `13_`-prefixed directory **anywhere** in their paths. Exactly **21,633** belong to the top-level Group 13 folder; the remaining **476** belong to other groups and remain in the ordinary outer ZIP. They were not moved or altered.

The 21,633 inner ZIP entries preserve their original relative paths, uncompressed file bytes, CRCs, timestamps, and external file attributes. Each member was verified against the published v2.15 archive. The new inner container necessarily has its own compressed ZIP representation, but fixture bytes are unchanged.

All other v2.15 ZIP members remain at the same paths, with their ZIP metadata and fixture contents preserved, except three intentionally regenerated authoritative root metadata files:

- `CURRENT_CORPUS_MANIFEST.json`
- `CORPUS_COVERAGE_LOCK.json`
- `CORPUS_CATALOG.json`

Byte-exact originals are archived under `Tools/Corpus Contamination Finder/Changed Renamed or Removed Corpus Files/G208_Post_v2_15_Group13_Archive/Originals/`. The current manifest/lock now describe the **default-extracted active corpus**; the catalog retains Group 13 as an optional archived group with a link and SHA-256 for its inner ZIP.

## Verification results

- Full ZIP CRC and member checks **PASS**.
- Inner Group 13 21,633-member identity and source-byte comparisons **PASS**.
- Default extraction and opt-in Group 13 restoration **PASS**.
- All 476 similarly named but unrelated entries stay in the outer ZIP **PASS**.
- All G207 and earlier fixtures, expected outcomes, test IDs, and 205 group declarations retained **PASS**.
- Independently re-downloaded published v2.16 ZIP SHA-256 **PASS**.
- Existing historical PowerShell integrity suite run against both complete published v2.15 and candidate v2.16: **six inherited failures in each, zero additional failures**. The full historical suite does not yet pass.
- Actual native Windows x01–x04 application execution **not performed** during this packaging change.

The previous immutable v2.15 release remains available, including its fully expanded Group 13.

[Release details](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.16).
