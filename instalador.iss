[Setup]
AppName=Sistema de Gerenciamento
AppVersion=1.0.0
DefaultDirName={autopf}\Sistema de Gerenciamento
DefaultGroupName=Sistema de Gerenciamento
OutputBaseFilename=Instalador_Sistema
Compression=lzma
SolidCompression=yes
DisableProgramGroupPage=yes

[Files]
Source: "C:\Users\keven\Desktop\SistemadeGerenciamento.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\keven\OneDrive\Área de Trabalho\Python Work\Projeto ERP\banco_de_dados.db"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\keven\OneDrive\Área de Trabalho\Python Work\Projeto ERP\imagens\*"; DestDir: "{app}\imagens"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Sistema de Gerenciamento"; Filename: "{app}\SistemadeGerenciamento.exe"
Name: "{commondesktop}\SistemadeGerenciamento"; Filename: "{app}\SistemadeGerenciamento.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Criar atalho na Área de Trabalho"; GroupDescription: "Atalhos:"

[Run]
Filename: "{app}\SistemadeGerenciamento.exe"; Description: "Executar Sistema de Gerenciamento"; Flags: nowait postinstall skipifsilent
