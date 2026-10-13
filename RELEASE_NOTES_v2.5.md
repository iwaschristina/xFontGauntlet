# xFontGauntlet v2.5 (G198)

Complete corpus ZIP preserving the G198 test coverage, with the 20 guide, manifest, catalog, and summary files moved from `TestCorpus/` directly into the ZIP root beside `TestCorpus/` and `Tools/`, matching the requested Windows Explorer layout.

- **197 test groups; 2,810 declared test cases**
- **43,354 files and 10,003 directory entries** (53,357 ZIP entries)
- **Archive:** `xFontGauntlet_v2.5.zip`
- **Size:** 66,663,855 bytes
- **SHA-256:** `0a6c76c3c158f8dd05aae78b15e227afa7c16c919659364fdfcaa7a571a159f9`

**Difference from v2.3:** Exactly 20 top-level `TestCorpus/` metadata files were relocated to the ZIP root. No other ZIP path, original compressed payload, or file content was changed by that relocation.

**Difference from v2.4:** Two active tool scripts were updated to read their manifests from the new ZIP root: `Tools/Invoke-CorpusValidation.ps1` and `Tools/Validate-Group134-Fixtures.py`. No font fixture or other corpus case was changed. The older historical scenario records and historical releases remain preserved, rather than silently rewriting original test records.

**Verification:** A checksum-gated GitHub Actions build checked all 53,357 ZIP member names and the content SHA-256 and metadata of every unchanged member. A separate independent job re-downloaded the published v2.5 asset and v2.4 reference, verified the full archive SHA, 20 root filenames, the two targeted tool changes, and preservation of every other member. Both jobs passed.

Static ZIP integrity is not the same as certifying the legacy 78-validator suite or executing production x01–x04 tests. Group 13 remains excluded from routine converter runs.

[v2.5 release](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.5) · [Download complete ZIP](https://github.com/iwaschristina/xFontGauntlet/releases/download/v2.5/xFontGauntlet_v2.5.zip)
