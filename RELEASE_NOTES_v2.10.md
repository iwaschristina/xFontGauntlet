# xFontGauntlet v2.10 — G203 converter regression coverage

**Latest authoritative full corpus**, built from the exact SHA-256-verified xFontGauntlet v2.9 (G202) ZIP. [Download the full v2.10 archive](https://github.com/iwaschristina/xFontGauntlet/releases/download/v2.10/xFontGauntlet_v2.10.zip).

## Distribution and integrity

- **201 groups**, **2,884 declared logical test cases**
- **53,785 ZIP members:** 43,687 files and 10,098 explicit directory entries
- **Size:** 82,556,899 bytes
- **SHA-256:** `c9e7cbe19e60690594464dd4e51fd119c3a34d7f5bb9e03a98d6c41a15130636`
- Same **20 root-level** metadata/guide files alongside `TestCorpus/` and `Tools/`.
- Earlier immutable release assets remain intact.

## G203 additions

New group `TestCorpus/201_G203_Type3_Dependency_And_Unicode_Recovery/` contains exactly **17** new regression cases (`G203-001` through `G203-017`), derived from xFontMorph versions **2.9–2.13**.

**PostScript Type 3 (10 cases):** literal `run` dependencies separated by comments and newlines; ignoring `run` tokens inside comments; recursive linked dependencies; references in linked programs absent from the primary font; collisions between source dependency names `render.ps` / `glyph-001.pbm` and Ghostscript-generated wrapper/raster outputs; missing files, traversal and cycles; and octal-escaped names with spaces. Source dependency staging must preserve hashes, isolate real source dependencies under `dependencies/` and avoid overwriting generated temporary assets. These are PostScript input/source fixtures plus specific runtime expectations, not a claim of completed Ghostscript conversion.

**UFO3 Unicode fidelity (5 cases):** valid unmapped `.notdef`; invalid Unicode assignment to `.notdef`; valid distinct A/B mappings; conflicting U+0041 glyph assignments; invalid surrogate U+D800. Each has a physical UFO3 package, including layer maps, contents plist and GLIF records. Positive cases remain positive; semantic loss must be refused rather than silently accepted.

**Type 1 embedded recovery (2 cases):** finite/integer versus fractional metrics, and ambiguous AGL glyph names mapping to one Unicode code point. The metric and conflict inputs are explicit scenario contracts; any copied legacy Type 1 fixture retains its original source data.

No new x01, x03 or x04 processing defects were confirmed beyond existing G197–G202 cases, and those cases are preserved unchanged.

## Preservation and tests

The release adds **90 ZIP members**. All **53,695 original v2.9 members** preserve their original paths and order. The only three pre-existing members whose contents changed are the current `CURRENT_CORPUS_MANIFEST.json`, `CORPUS_COVERAGE_LOCK.json`, and `CORPUS_CATALOG.json`; exact byte-for-byte copies of their former versions are retained under `Tools/Corpus Contamination Finder/Changed Renamed or Removed Corpus Files/G203_Post_v2_9_Coverage/Originals/`.

All **22,109 Group 13 entries** remain untouched; that group remains intentionally excluded from routine x02 converter runs. The three previously repaired G197/G198 positive UFO3 rename cases are also unchanged.

Build and independent release-download SHA-256 verification **PASS**. All 17 G203 fixture declarations and SHA hashes, package structure, full ZIP CRC, original ZIP member preservation and current manifest/lock/catalog coherence were verified. G203 PostScript dependency fixtures were also exercised against an exact snapshot of the current xFontMorph 2.13 dependency-scanner functions, including correct negative-case exceptions.

The historical PowerShell integrity suite was run on complete v2.9 and v2.10 separately. Both returned the **same five inherited failures**: G80, G83, G109, G116 and missing `Get-Sha256`. There were **zero new** failures, but **the overall historical suite is not passing**. Live production Windows conversion, Ghostscript, and full cross-tool integration tests were **not executed** as part of this corpus release.

[View release](https://github.com/iwaschristina/xFontGauntlet/releases/tag/v2.10).
