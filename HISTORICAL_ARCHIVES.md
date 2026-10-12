# Historical corpus ZIP archive

The authoritative xFontGauntlet v2.0 corpus is the unchanged `xFontGauntlet_v2.0.zip` asset on the **v2.0** GitHub Release, once that asset has been uploaded and independently verified.

Older G-series and pre-versioned corpus archives are stored **as original ZIP assets**, not extracted Git files or reconstructed directories. The dedicated historical Release tag is `archive-pre-v2.0`.

## Archival rules

- Preserve every baseline's original ZIP filename and exact bytes. Never unzip/repack, normalize unusual paths, or omit binary files and empty ZIP directory entries.
- Before upload, calculate each ZIP's SHA-256 and size. Store a local archive manifest.
- Upload each original ZIP to the historical GitHub Release; **do not use `--clobber`** to replace assets silently.
- Download **each** published asset again, compare its SHA-256 and size with the source, and record the verified result in a per-file report.
- If a remote asset exists with conflicting bytes, stop rather than overwrite.
- Only after the GitHub Release is published and every intended item is individually verified should those **same verified** copies be considered eligible for deletion from ChatGPT Library. No deletion is automatic.
- Do not confuse the current v2.0 Release with the historical archive Release.

## Existing inventory

The Library inspection of October 12, 2026 found **107** G-series ZIP records under `x05 Font Test Corpus`, representing **84** distinct G numbers (and multiple deliberate filename variants). Earlier corpus ZIPs also exist under the separate `Font Test Corpus` Library folder.

The 35 original G162–G196 ZIPs available for local verification amount to **2,268,832,688 bytes**. Their complete original-filename SHA-256 inventory is bundled with the historical archive publisher. Additional historical Library files must be downloaded locally before they can be independently published and verified.

## Publication status

Documentation and an archive-upload helper have been prepared, but **no historical ZIP release assets have been uploaded or verified by this repository setup**. The current v2.0 Release asset also requires publication and verification. Do not delete Library copies based on inventory or local checks alone.

## Running the publisher

Use the `xFontGauntlet_Historical_Archive_Uploader.zip` handoff package from the corpus ChatGPT discussion. Extract the small publisher package, but keep all corpus baseline ZIPs unmodified. Put the original old ZIPs downloaded from Library in a local folder, then run:

```powershell
py .\Publish-HistoricalBaselines.py --source 'C:\CorpusArchiveInputs'
py .\Publish-HistoricalBaselines.py --source 'C:\CorpusArchiveInputs' --publish
```

The tool uses Python 3 and an authenticated GitHub CLI (`gh auth login`). It scans the original ZIP files, verifies known G162–G196 hashes, uploads/resumes without overwriting conflicts, downloads each asset to verify SHA-256, and writes `historical-upload-results.csv` with per-file `github_verified` status.

**Only `github_verified=YES` plus a publicly published historical Release makes a specific ZIP eligible for Library deletion.** If it is not listed or fails verification, retain it.
