# xFontGauntlet v2.9 (G202)

Authoritative **complete** ZIP successor to the exact published v2.8/G201 corpus. This release incorporates 23 new regression cases identified from the latest x01–x04 development and verification work.

## Distribution

- [Download complete v2.9 ZIP](https://github.com/iwaschristina/xFontGauntlet/releases/download/v2.9/xFontGauntlet_v2.9.zip)
- **200 groups; 2,867 declared logical cases**.
- **53,695 ZIP entries**: 43,623 files and 10,072 explicit directories.
- **Archive size:** 78,579,361 bytes.
- **SHA-256:** `6e0897b253c5df00b45822b113f679161ef9a547d4fd3c9c839456d2f55dc57b`.
- ZIP root continues to contain exactly the original 20 metadata and guide files beside `TestCorpus/` and `Tools/`.

## New test fixtures

Group `TestCorpus/200_G202_Mixed_Namespace_Subprocess_And_Auditor_Boundaries/`, with `G202-001` to `G202-023` in `EXPECTED_RESULTS.json`.

**x01 — xFontIdentity v2.8 (5 cases).** Tests pre-prefixed extended namespace and ordinary Windows path operands for short directory moves plus inverse rollback; mixed-namespace METAFONT locality; collision reservation identity; and subset retry locality. An explicit short-path mover case is distinct from existing long-source/long-target tests.

**x02 — xFontMorph v2.8 (5 cases).** Worker-safe Windows extended-path arguments for fontTools/TTX, EOT and FontForge; Ghostscript Type3 rendering dependencies staged in a short working directory rather than an unsupported long CreateProcessW cwd; deep-path METAFONT cache locks and dependency handling. Includes real parseable TTF and WOFF2 controls, staged SVGZ/PS and METAFONT sources, plus an EOT/SFD sample copied from prior corpus entries when available. Test contracts distinguish scenario inputs from actual production execution.

**x03 — xFontHound v2.1.** No new font-processing defect was confirmed in the latest changes, so all existing Finder/Copier package and dependency coverage is retained without redundant cases.

**x04 — xFontMedic v2.0.5 (13 cases).** Paired valid and malformed UFO3/UFOZ packages, covering valid default layer, missing default layer, duplicate layer, traversal in layer path, and GLIF path traversal. Physical PCF bytes exercise valid mandatory metrics/bitmap/encoding bodies, format mismatch, glyph-count mismatch, and header-only false positive. VF controls distinguish proper 248 postamble padding from invalid trailing bytes. PFM controls contain real large pointers to byte 100000 for bounded, NUL-terminated face-name validation. PCF/VF/PFM byte arrays reproduce cases from xFontMedic's Windows smoke regressions.

## Preservation

All 53,602 original v2.8 ZIP members retain their paths and metadata, and all original font/test fixture bytes are unchanged. Only `CURRENT_CORPUS_MANIFEST.json`, `CORPUS_COVERAGE_LOCK.json`, and `CORPUS_CATALOG.json` were regenerated. Exact originals of those three records are archived under:
`Tools/Corpus Contamination Finder/Changed Renamed or Removed Corpus Files/G202_Post_v2_8_Coverage/Originals/`.

The earlier positive G197/G198 UFO3 fixture repairs remain unchanged. Every one of the original **22,109 Group 13** ZIP entries remains unchanged; Group 13 continues to be excluded from routine x02 converter runs.

## Verification

G202's complete ZIP has passed a SHA-256-gated build, structural fixture checks, retained-member comparison, ZIP CRC checks, active manifest/lock regeneration, and verification that both directory UFOs and packaged UFOZs contain identical corresponding layer maps. The independent published-asset download verification is tracked in GitHub Actions.

The existing PowerShell integrity validation suite was run on **both** v2.8 and the v2.9 candidate: both reported the **same five inherited failures** (G80, G83, G109, G116 and missing `Get-Sha256`) with zero additional failures caused by G202. Thus **the historical validation suite is not passing**, although the regression comparison passed. Windows application-level x01–x04 execution is not certified by this corpus build.
