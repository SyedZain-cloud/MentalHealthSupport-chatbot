$bundle = Split-Path -Parent $MyInvocation.MyCommand.Path
$failed = $false
Get-Content -LiteralPath (Join-Path $bundle 'CHECKSUMS.sha256') | ForEach-Object {
    if ($_ -match '^([0-9a-f]{64})  (.+)$') {
        $expected = $matches[1]
        $relative = $matches[2]
        $actual = (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $bundle $relative)).Hash.ToLower()
        if ($actual -ne $expected) {
            Write-Error "FAILED: $relative"
            $failed = $true
        } else {
            Write-Output "OK: $relative"
        }
    }
}
if ($failed) { exit 1 }
