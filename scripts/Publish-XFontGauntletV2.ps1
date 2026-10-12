# Publishes the original xFontGauntlet v2.0 ZIP without extracting or modifying it.
[CmdletBinding()]
param(
    [string]$Archive = (Join-Path $PSScriptRoot 'xFontGauntlet_v2.0.zip'),
    [string]$Repository = 'iwaschristina/xFontGauntlet'
)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$Tag = 'v2.0'
$AssetName = 'xFontGauntlet_v2.0.zip'
$ExpectedSize = 66605229L
$ExpectedSHA256 = '0431b543e0d133f1018520e4b53591b0f0079fc6b0b29b8ae6885289aaed1379'
function Assert-Gh([string]$Step) {
    if ($LASTEXITCODE -ne 0) { throw "$Step failed. GitHub CLI exit code: $LASTEXITCODE" }
}
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) { throw 'Install GitHub CLI from https://cli.github.com/ then run gh auth login.' }
& gh auth status
Assert-Gh 'Authentication'
$Archive = (Resolve-Path -LiteralPath $Archive).Path
if ([IO.Path]::GetFileName($Archive) -cne $AssetName) { throw "Archive must retain original name $AssetName" }
if ((Get-Item -LiteralPath $Archive).Length -ne $ExpectedSize) { throw 'Original ZIP size mismatch; stopping.' }
$ActualHash = (Get-FileHash -LiteralPath $Archive -Algorithm SHA256).Hash.ToLowerInvariant()
if ($ActualHash -cne $ExpectedSHA256) { throw "Original ZIP hash mismatch: $ActualHash" }
$Head = (& gh api "repos/$Repository/git/ref/heads/main" --jq '.object.sha')
Assert-Gh 'Read main branch'
$Head = ([string]$Head).Trim()
if ($Head -notmatch '^[0-9a-fA-F]{40}$') { throw 'Invalid branch SHA.' }
$TagSha = (& gh api "repos/$Repository/git/ref/tags/$Tag" --jq '.object.sha' 2>$null)
if ($LASTEXITCODE -eq 0) {
    if (([string]$TagSha).Trim() -cne $Head) { throw 'Existing v2.0 tag does not point to main HEAD; stopping.' }
} else {
    & gh api -X POST "repos/$Repository/git/refs" -f "ref=refs/tags/$Tag" -f "sha=$Head" --silent
    Assert-Gh 'Create v2.0 tag'
}
$Release = (& gh release view $Tag --repo $Repository --json url --jq '.url' 2>$null)
if ($LASTEXITCODE -eq 0) {
    $Assets = @(& gh release view $Tag --repo $Repository --json assets --jq '.assets[].name')
    Assert-Gh 'Inspect release'
    if ($Assets -cnotcontains $AssetName) {
        & gh release upload $Tag $Archive --repo $Repository
        Assert-Gh 'Upload original ZIP'
    }
} else {
    $Notes = Join-Path $PSScriptRoot 'RELEASE_NOTES_v2.0.md'
    & gh release create $Tag $Archive --repo $Repository --verify-tag --title 'xFontGauntlet 2.0' --notes-file $Notes
    Assert-Gh 'Create release and upload ZIP'
}
$Temporary = Join-Path ([IO.Path]::GetTempPath()) ('xfontgauntlet-verify-' + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $Temporary | Out-Null
try {
    & gh release download $Tag --repo $Repository --pattern $AssetName --dir $Temporary
    Assert-Gh 'Download uploaded ZIP'
    $Published = Join-Path $Temporary $AssetName
    if ((Get-Item -LiteralPath $Published).Length -ne $ExpectedSize) { throw 'Published ZIP size differs.' }
    $PublishedHash = (Get-FileHash -LiteralPath $Published -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($PublishedHash -cne $ExpectedSHA256) { throw "Published ZIP SHA-256 differs: $PublishedHash" }
} finally { Remove-Item -LiteralPath $Temporary -Recurse -Force -ErrorAction SilentlyContinue }
Write-Host "VERIFICATION RESULT: PASS"
Write-Host "Commit: $Head"
Write-Host "Tag: $Tag"
Write-Host "Published SHA-256: $ExpectedSHA256"
Write-Host "Release: https://github.com/$Repository/releases/tag/$Tag"
