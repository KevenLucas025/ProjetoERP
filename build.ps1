$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $projectRoot

$distPath = "$env:USERPROFILE\Desktop"
$systemName = "Sistema de Gerenciamento"
$systemFolder = Join-Path $distPath $systemName
$zipPath = Join-Path $distPath "Sistema-de-Gerenciamento.zip"

Write-Host "Limpando builds antigos..."

if (Test-Path $systemFolder) {
    Remove-Item -Recurse -Force $systemFolder
}

if (Test-Path $zipPath) {
    Remove-Item -Force $zipPath
}

if (Test-Path (Join-Path $distPath "Atualizador.exe")) {
    Remove-Item -Force (Join-Path $distPath "Atualizador.exe")
}

Write-Host "Gerando sistema principal..."

python -m PyInstaller --noconfirm --clean --onedir --windowed `
  --collect-all pandas `
  --collect-all numpy `
  --add-data "imagens;imagens" `
  --icon "imagens/favicon.ico" `
  --name "$systemName" `
  --distpath $distPath `
  main.py

Write-Host "Gerando atualizador..."

python -m PyInstaller --noconfirm --clean --onefile --noconsole `
  --name "Atualizador" `
  --distpath $distPath `
  atualizador.py

$atualizadorExe = Join-Path $distPath "Atualizador.exe"
$destinoAtualizador = Join-Path $systemFolder "Atualizador.exe"

if (Test-Path $atualizadorExe) {
    Move-Item -Force $atualizadorExe $destinoAtualizador
    Write-Host "Atualizador movido para a pasta do sistema."
} else {
    Write-Host "ERRO: Atualizador.exe não encontrado!"
    exit 1
}

if (-not (Test-Path $systemFolder)) {
    Write-Host "ERRO: Pasta do sistema não foi criada."
    exit 1
}

Write-Host "Compactando pasta do sistema..."

Compress-Archive -Path $systemFolder -DestinationPath $zipPath -Force

if (Test-Path $zipPath) {
    Write-Host "ZIP criado com sucesso em: $zipPath"
} else {
    Write-Host "ERRO: Falha ao criar o arquivo ZIP."
    exit 1
}

Write-Host "Build finalizado com sucesso!"