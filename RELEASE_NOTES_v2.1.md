# xFontGauntlet v2.1 (G197)

Complete successor to the immutable v2.0/G196 corpus, incorporating the October 11–13 review of x01 Rename Fonts, x02 Convert Fonts, x03 Font Finder/Copier, and x04 mover workflows.

- **196 groups**: all 195 existing groups plus `196_Recent_X01_X04_Regression_Cases_20261013`.
- **2,790 declared test cases**: previous 2,768 plus 22 G197 cases.
- **43,321 files** and **9,982 explicit directory entries** (53,303 ZIP entries in total).
- **File:** `xFontGauntlet_v2.1.zip`
- **Size:** 66,636,450 bytes
- **SHA-256:** `618278f1eca218bdd3b0221ce95883c54b16e2794f1a7452ed3ccadb4791c1f3`

G197 adds test cases for directory-backed UFO renaming and null-drive behavior; nested duplicates and [MAC] paths; long same-volume moves; malformed CFF face-count handling; WOFF trailing line endings; partial, stale and zero-byte converter outputs; Finder-to-Renamer package atomicity; and assertions for existing Type 3, large PCF and performance-stage scenarios.

**Integrity verification:** An automated builder independently checked the exact published v2.0 input SHA-256, all 53,241 original ZIP members' metadata and uncompressed SHA-256 contents, the G197 payload hash, 22 case IDs and fixtures, and full merged ZIP CRCs. A separate GitHub Actions job then downloaded the published v2.1 ZIP and verified its full SHA-256 and entry structure. Both jobs passed.

**Scope:** These checks verify release integrity and new static fixtures, not the x01–x04 production tools' behavior. The legacy 78 corpus validators were not rerun against the merged v2.1 ZIP. Group 13 remains excluded from routine converter runs as requested.

[Full v2.1 ZIP](https://github.com/iwaschristina/xFontGauntlet/releases/download/v2.1/xFontGauntlet_v2.1.zip) · [GitHub Release](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.1)
