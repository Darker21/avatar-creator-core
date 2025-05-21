Get-ChildItem -Path dist | ForEach-Object {
    $file = $_
    if ($file.FullName -like '*.sha256') {
        return
    }
    $hash = Get-FileHash -Path $file.FullName -Algorithm SHA256
    $expectedHash = (Get-Content -Path "$($file.FullName).sha256").Split(' ')[0]

    if ($hash.Hash -ne $expectedHash) {
        Write-Host -ForegroundColor Red "Hash mismatch for file: $($file.FullName)"
    } else {
        Write-Host -ForegroundColor Green "Hash verified for file: $($file.FullName)"
    }
}