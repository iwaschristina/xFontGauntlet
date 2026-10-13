# xFontGauntlet v2.2 (G198)

Complete release built from the exact, independently verified xFontGauntlet v2.1 (G197) ZIP, adding Group 197 with 20 cases found in the most recent x01–x04 project review.

## Contents
- Groups: **197**
- Declared logical cases: **2,810**
- Files in ZIP: **43,354** (33 more than v2.1)
- Directory entries: **10,004** (22 more)
- ZIP entries: **53,358**
- ZIP archive size: **66,664,778 bytes**
- File: `xFontGauntlet_v2.2.zip`
- SHA-256: `e4232cfab704d9a8aaf311372e39f8c67cd1737a949bdadd095f6c4560fe2535`

## New tests
- **x01 Renamer:** short input to over-248-character planned destination, extended path handling, same-volume renames, directory-backed UFO atomicity and representative recovery/rollback.
- **x02 Converter:** valid TTFs differing only in volatile `head.modified`; negative controls with actual glyph outline or name-table differences; output provenance and stale-output protection.
- **x03 Finder/Copier:** exact SHA preservation of copied WOFF2 and AppleDouble companions through Finder to xFontMedic handoff.
- **x04 xFontMedic Font Audit/Repair:** bounded AppleDouble headers, bad magic, truncated metadata, invalid entry offsets, corrupt CFF/PFB; valid WOFF2 decoder-present/decoder-absent behavior; audit no-op repair idempotence.

The 20 new case records and fixture hashes reside in `TestCorpus/197_Recent_X01_X04_Regression_Cases_20261013/EXPECTED_RESULTS.json`.

## Verification status
Full-file v2.1 SHA checked before build; every pre-existing one of 53,303 ZIP entries was checked to preserve metadata and uncompressed SHA-256; all added fixtures and merged archive CRCs passed. A separate workflow independently re-downloads the published v2.2 archive to compare it with v2.1.

**Limits:** Static integrity is not a substitute for executing each application's Windows/FontForge workflows or the complete historical 78-validator suite. Group 13 remains intentionally excluded from routine converter runs.

[Full release](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.2) · [Complete ZIP](https://github.com/iwaschristina/xFontGauntlet/releases/download/v2.2/xFontGauntlet_v2.2.zip)
