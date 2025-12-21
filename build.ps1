# Caminho onde serão gerados os arquivos
$distPath = "$env:USERPROFILE\Desktop"
$systemFolder = Join-Path $distPath "SistemadeGerenciamento"

# ------------------------------
# Build do SISTEMA PRINCIPAL
# ------------------------------
pyinstaller --noconfirm --clean --onedir --windowed `
  --collect-all pandas `
  --collect-all numpy `
  --add-data "imagens;imagens" `
  --icon "imagens/favicon.ico" `
  --name "SistemadeGerenciamento" `
  --distpath $distPath `
  main.py

# ------------------------------
# Build do ATUALIZADOR
# ------------------------------
pyinstaller --noconfirm --clean --onefile `
  --name "Atualizador" `
  --distpath $distPath `
  atualizador.py

# ------------------------------
# Move o Atualizador.exe para dentro da pasta do sistema
# ------------------------------
$atualizadorExe = Join-Path $distPath "Atualizador.exe"
$destinoAtualizador = Join-Path $systemFolder "Atualizador.exe"

if (Test-Path $atualizadorExe) {
    Move-Item -Force $atualizadorExe $destinoAtualizador
    Write-Host "Atualizador movido para a pasta do sistema."
} else {
    Write-Host "ERRO: Atualizador.exe não encontrado!"
}

Write-Host "Build finalizado!"
