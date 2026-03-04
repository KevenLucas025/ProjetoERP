$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $projectRoot

$distPath = "$env:USERPROFILE\Desktop"
$systemFolder = Join-Path $distPath "Sistema de Gerenciamento"


python -m PyInstaller --noconfirm --clean --onedir --windowed `
  --collect-all pandas `
  --collect-all numpy `
  --add-data "imagens;imagens" `
  --icon "imagens/favicon.ico" `
  --name "Sistema de Gerenciamento" `
  --distpath $distPath `
  main.py

pyinstaller --noconfirm --clean --onefile --noconsole `
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
}

Write-Host "Build finalizado!"