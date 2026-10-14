# xFontGauntlet v2.11 — G105 external-reference fixture repair

Built directly from the immutable, SHA-256-verified **v2.10 corpus release**.

## Repair
G105-03 previously referenced `Referenced Duplicate [UFO Project]/Regular.ufo` in `ExternalConsumer.designspace`, although xFontIdentity renamed that referenced folder to `CR UFO Valid [Version 1.000] [PS CRUFOValid-Regular] [UFO Project]`. The input fixture now uses the canonical folder name and the designspace and test contract point to it. The external reference remains valid before and after renaming, permitting the mover to leave the referenced folder in place while moving its independent duplicate controls.

The ten original project directory/package entries and ten original changed files, including the three former root integrity metadata files, are preserved inside the established changed/renamed/removed corpus file archive. All other original ZIP entries retain their names, ordering, and uncompressed contents; Group 13 is untouched.

## Verification
- **Input baseline:** v2.10 — SHA-256 `c9e7cbe19e60690594464dd4e51fd119c3a34d7f5bb9e03a98d6c41a15130636`
- **New baseline:** v2.11 — SHA-256 `53abe5fcfbceb4db22d56ee38baecc90d159c196e879704ccf43f1058fde18f3`
- **ZIP size:** 86,898,934 bytes
- **Active TestCorpus files:** 43,508
- **Active TestCorpus directories:** 10,056
- **Updated active fixture files:** 2 (designspace XML and G105 contract)
- **Renamed G105 package directory entries:** 10
- **Corpus SHA-256 tree:** `22cab2dad44d2f21109fb26334bdc53397b5d661a9db3903a470ced71a7b2355`

CI independently re-read, hashed and matched every TestCorpus file and directory against updated current manifest and coverage lock; ZIP integrity passed. Full xFontIdentity→mover runtime execution **has not been rerun** with the corrected v2.11 corpus. The G64-12 near-duplicate AFM remains an expected safety refusal; Group 13 remains intentionally excluded from fast runs.

[Download the full corpus ZIP](https://github.com/iwaschristina/xFontGauntlet/releases/download/v2.11/xFontGauntlet_v2.11.zip).
