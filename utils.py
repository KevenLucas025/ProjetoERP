from PySide6.QtWidgets import (QLineEdit, QPushButton,QVBoxLayout,QLabel,QFrame,QApplication,QDialog,
                               QGraphicsScene,QGraphicsView,QGraphicsPixmapItem,QGraphicsItem,QFileDialog,QMessageBox,QGraphicsDropShadowEffect)
from PySide6.QtCore import Qt, QPropertyAnimation,Signal,QRectF,QPointF,QSize
from PySide6.QtGui import QIcon,QPixmap,QPainterPath,QPainter,QColor
import json
import os
import sys
from database import DataBase




class MostrarSenha:
    def __init__(self, main_window, line_edit: QLineEdit):
        self.line_edit = line_edit
        self._show_password = False
        self.botao_exibir_senha()
        self.main_window = main_window  
        self.atualizar_icone()
        

    def botao_exibir_senha(self):
        # Criar botão dentro do QLineEdit
        self.btn_mostrar_senha = QPushButton(self.line_edit)
        self.btn_mostrar_senha.setCursor(Qt.PointingHandCursor)
        self.btn_mostrar_senha.setContentsMargins(0,0,0,0)
        self.btn_mostrar_senha.setObjectName("btn_mostrar_senha")
        
        altura = self.line_edit.height() - 4
        self.btn_mostrar_senha.setFixedSize(altura, altura)
        self.btn_mostrar_senha.move(self.line_edit.width() - altura - 2, 2)


        # Conectar o clique para alternar mostrar/ocultar senha
        self.btn_mostrar_senha.clicked.connect(self.senha_visivel)

        # Definir modo password inicialmente
        self.line_edit.setEchoMode(QLineEdit.Password)

        # Ajustar o posicionamento caso o QLineEdit mude de tamanho (opcional)
        self.line_edit.resizeEvent = self._on_resize

    def _on_resize(self, event):
        altura = self.line_edit.height() - 4
        self.btn_mostrar_senha.setFixedSize(altura, altura)
        self.btn_mostrar_senha.move(self.line_edit.width() - altura - 2, 2)
        
    def atualizar_icone(self):
        tema = self.main_window.temas.config.get("tema", "classico")

        if tema == "escuro":
            icone = caminho_recurso("imagens/olho_branco.png")
        else:
            icone = caminho_recurso("imagens/olho_preto.png")

        self.btn_mostrar_senha.setIcon(QIcon(icone))
        self.btn_mostrar_senha.setIconSize(self.btn_mostrar_senha.size())

        self.btn_mostrar_senha.setStyleSheet("""
            QPushButton#btn_mostrar_senha {
                border: none;
                background: transparent;
                padding: 0px;
                qproperty-iconSize: 16px 16px;
            }

            QPushButton#btn_mostrar_senha:hover {
                background: transparent;
            }

            QPushButton#btn_mostrar_senha:pressed {
                background: transparent;
                padding-left: 1px;
                padding-top: 1px;
            }
        """)


        
    def animar_botao(self):
        rect = self.btn_mostrar_senha.geometry()
        # botão “afunda” 2 pixels para baixo e direita
        self.anim = QPropertyAnimation(self.btn_mostrar_senha, b"geometry")
        self.anim.setDuration(100)
        self.anim.setStartValue(rect)
        self.anim.setKeyValueAt(0.5, rect.adjusted(2, 2, 2, 2))
        self.anim.setEndValue(rect)
        self.anim.start()


    def senha_visivel(self):
        self.animar_botao()
        
        if self._show_password:
            self.line_edit.setEchoMode(QLineEdit.Password)
            self._show_password = False
        else:
            self.line_edit.setEchoMode(QLineEdit.Normal)
            self._show_password = True

    
    

def configurar_frame_valores(frame: QFrame, titulo: str, valor_monetario: bool = True) -> QLabel:
    layout = QVBoxLayout(frame)
    layout.setAlignment(Qt.AlignCenter)

    label_titulo = QLabel(titulo)
    label_titulo.setAlignment(Qt.AlignCenter)
    label_titulo.setObjectName("label_titulo")
    
    label_valor = QLabel("R$ 0,00" if valor_monetario else "")
    label_valor.setAlignment(Qt.AlignCenter)
    label_valor.setObjectName("label_valor")


    layout.addWidget(label_titulo)
    layout.addWidget(label_valor)

    return label_valor  # você salva essa referência depois para atualizar o texto

def rodando_como_exe() -> bool:
    return getattr(sys, "frozen",False)

def pasta_configuracao_app() -> str:
    """
    - EXE: %APPDATA%\\SistemaGerenciamento
    - Python: pasta atual do projeto
    """
    if rodando_como_exe():
        return os.path.join(os.getenv("APPDATA") or os.getcwd(), "SistemaGerenciamento")
    return os.getcwd()

def caminho_config_json() -> str:
    pasta = pasta_configuracao_app()
    os.makedirs(pasta, exist_ok=True)
    return os.path.join(pasta, "config.json")

def carregar_config() -> dict:
    path = caminho_config_json()
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            txt = f.read().strip()
            return json.loads(txt) if txt else {}
    except:
        return {}

def salvar_configs(cfg: dict) -> None:
    path = caminho_config_json()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=4, ensure_ascii=False)
        
def pegar_ultimo_diretorio(chave: str, default_dir: str = "") -> str:
    """
    Retorna a última pasta usada para uma chave (ex: "excel", "pdf").
    """
    cfg = carregar_config()
    ult = cfg.get("ultimos_diretorios", {})
    p = (ult.get(chave) or "").strip()

    if p and os.path.isdir(p):
        return p

    if default_dir and os.path.isdir(default_dir):
        return default_dir

    return ""

def obter_ultimo_diretorio(chave: str, caminho_arquivo: str) -> None:
    """
    Salva a pasta do arquivo escolhido como última pasta daquela chave.
    """
    pasta = os.path.dirname(caminho_arquivo) if caminho_arquivo else ""
    if not pasta or not os.path.isdir(pasta):
        return

    cfg = carregar_config()
    ult = cfg.get("ultimos_diretorios", {})
    ult[chave] = pasta
    cfg["ultimos_diretorios"] = ult
    salvar_configs(cfg)
    
def salvar_dialogo_memoria(parent, chave: str, titulo: str, nome_padrao: str, filtro: str, default_dir: str = "") -> str:
    """
    Abre o diálogo SALVAR lembrando a última pasta por chave.
    Ex:
        caminho = save_dialog_mem(self, "excel", "Salvar Excel", "Relatório Tabela Base.xlsx", "Excel (*.xlsx)")
    """
    last_dir = pegar_ultimo_diretorio(chave, default_dir=default_dir)

    sugestao = os.path.join(last_dir, nome_padrao) if last_dir else nome_padrao

    caminho, _ = QFileDialog.getSaveFileName(parent, titulo, sugestao, filtro)
    
    if not caminho:
        return ""

    obter_ultimo_diretorio(chave, caminho)
    return caminho

def abrir_dialogo_memoria(parent, chave: str, titulo: str, filtro: str, default_dir: str = "") -> str:
    """
    Abre o diálogo ABRIR lembrando a última pasta por chave.
    """
    last_dir = pegar_ultimo_diretorio(chave, default_dir=default_dir)

    caminho, _ = QFileDialog.getOpenFileName(parent, titulo, last_dir or "", filtro)
    if not caminho:
        return ""

    obter_ultimo_diretorio(chave, caminho)
    return caminho

def caminho_recurso(relativo):
        """
        Retorna o caminho correto para arquivos (imagens, ícones, gifs)
        Funciona no Python e no PyInstaller (onedir / onefile)
        """
        if getattr(sys, 'frozen', False):
            # EXE
            base_path = sys._MEIPASS if hasattr(sys, '_MEIPASS') else os.path.dirname(sys.executable)
        else:
            # Python
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relativo)
    
def salvar_imagem_otimizada(
    pixmap: QPixmap,
    caminho_destino: str,
    tamanho_max: int = 512,
    qualidade: int = 80
    ):
    """
    Salva uma imagem otimizada para avatar/perfil.

    - Redimensiona mantendo proporção
    - Converte para JPEG
    - Aplica compressão controlada
    """

    if pixmap.isNull():
        return False

    # QPixmap → QImage (melhor para processamento e salvamento)
    imagem = pixmap.toImage()

    imagem = imagem.scaled(
        tamanho_max,
        tamanho_max,
        Qt.KeepAspectRatio,
        Qt.SmoothTransformation
    )

    # Garante que o diretório exista
    os.makedirs(os.path.dirname(caminho_destino), exist_ok=True)

    # Salva como JPEG comprimido
    return imagem.save(caminho_destino, "JPEG", qualidade)

    
class VisaoRecorte(QGraphicsView):
    def __init__(self, scene):
        super().__init__(scene)
        self.proporcao_margem = 0.21
        self.setCursor(Qt.SizeAllCursor)
        
        # MELHORIA DE PERFORMANCE:
        # SmartViewportUpdate é mais eficiente que FullViewportUpdate
        self.setViewportUpdateMode(QGraphicsView.SmartViewportUpdate)
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.SmoothPixmapTransform)
        
        # Removemos mousePress/Move/Release daqui para não dar conflito

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.centerOn(0, 0)

    def diametro_recorte(self):
        viewport = self.viewport().rect()
        tamanho = min(viewport.width(), viewport.height())
        return tamanho * (1 - self.proporcao_margem)

    def drawForeground(self, painter, rect):
        # O desenho do overlay (a parte escura)
        painter.save()
        diametro = self.diametro_recorte()
        centro = QPointF(0, 0)

        path = QPainterPath()
        path.addRect(rect) # Fundo escuro total
        
        # "Fura" o círculo no meio
        path.addEllipse(centro, diametro/2, diametro/2)

        painter.setBrush(QColor(0, 0, 0, 170))
        painter.setPen(Qt.NoPen)
        painter.drawPath(path)
        painter.restore()


        
class ItemPixmapMovel(QGraphicsPixmapItem):
    def __init__(self, pixmap):
        super().__init__(pixmap)
        self.setFlag(QGraphicsItem.ItemSendsScenePositionChanges)
        # Ativamos a flag nativa de movimento, mas controlaremos o delta para precisão
        self.setFlag(QGraphicsItem.ItemIsMovable, False) 
        
        
        self._arrastando = False
        self._ultima_pos_mouse = QPointF()
        
    def wheelEvent(self, event):

        fator = 1.1 if event.delta() > 0 else 0.9
        escala_atual = self.scale()
        nova_escala = escala_atual * fator

        # View e limites
        view = self.scene().views()[0]
        diametro = view.diametro_recorte()
        br = self.boundingRect()

        escala_minima = max(
            diametro / br.width(),
            diametro / br.height()
        )

        if nova_escala < escala_minima:
            nova_escala = escala_minima
        elif nova_escala > 5.0:
            nova_escala = 5.0

        # 🎯 Centro fixo da cena
        centro_cena = QPointF(0, 0)
        
        ponto_na_imagem = self.mapFromScene(centro_cena)
        
        self.setScale(nova_escala)
        
        ponto_pos_zoom = self.mapToScene(ponto_na_imagem)
        
        delta = ponto_pos_zoom - centro_cena
        
        self.setPos(self.pos() - delta)
        
        self.setPos(self.pos())
        
        event.accept()


    def mousePressEvent(self, event):
        # Muda o cursor para "fechado" ao segurar (estilo grab)
        if event.button() == Qt.LeftButton:
            self.scene().views()[0].setCursor(Qt.SizeAllCursor)
            self._arrastando = True
            self._ultima_pos_mouse = event.scenePos()
            event.accept()
            
            

    def mouseMoveEvent(self, event):
        if self._arrastando:
            # Cálculo de delta direto na cena (mais rápido)
            pos_atual = event.scenePos()
            delta = pos_atual - self._ultima_pos_mouse
            
            self.setPos(self.pos() + delta)
            self._ultima_pos_mouse = pos_atual
            event.accept()

    def mouseReleaseEvent(self, event):
        self._arrastando = False
        self.scene().views()[0].setCursor(Qt.SizeAllCursor)
        event.accept()

    def itemChange(self, alteracao, valor):
        if alteracao == QGraphicsItem.ItemPositionChange and self.scene():
            return self.tratar_limites(valor)
        return super().itemChange(alteracao, valor)

    def tratar_limites(self, nova_pos):
        # Mantém a lógica de não deixar o fundo aparecer
        view = self.scene().views()[0]
        raio = view.diametro_recorte() / 2
        
        escala = self.scale()
        br = self.boundingRect()
        largura = br.width() * escala
        altura = br.height() * escala

        # Limites (ajustados para o centro 0,0)
        max_x = -raio
        min_x = raio - largura
        max_y = -raio
        min_y = raio - altura

        x = max(min(nova_pos.x(), max_x), min_x)
        y = max(min(nova_pos.y(), max_y), min_y)

        return QPointF(x, y)

 
class DialogoRecorteImagem(QDialog):
    def __init__(self, pixmap, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Recortar imagem")
        self.setFixedSize(520, 560)

        if parent and hasattr(parent, 'temas'):
            self.temas = parent.temas
        else:
            self.temas = Temas()

        self.temas = Temas()
        self.config = self.temas.config
        tema = self.config.get("tema", "classico")
        
        if tema == "escuro":
            botao_style = """
                QPushButton {
                border-radius: 28px;
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(60, 60, 60),   /* topo */
                    stop:1 rgb(100, 100, 100) /* base */
                );      
                min-height: 24px;  /* Adicione esta linha */
            }

            QPushButton:hover {
                background-color: #444444;
            }

            QPushButton:pressed {
                background-color: #555555;
                border: 2px solid #888888;
            }
            """
        elif tema == "claro":
            botao_style = """
            /* Botões gerais  */
            QPushButton {
                border-radius: 8px;
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(220, 220, 220),  /* topo */
                    stop:1 rgb(245, 245, 245)   /* base */
                );
                font-size: 14px;
                color: #000000; /* texto escuro */
            }

            QPushButton:hover {
                background-color: #e0e0e0;
            }

            QPushButton:pressed {
                background-color: #d0d0d0;
                border: 2px solid #aaaaaa;
            }
            """
        else:
            botao_style = """
            QPushButton{
                color: rgb(255, 255, 255);
                border-radius: 8px;
                font-size: 16px;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */
                border: 4px solid transparent;
            }
            
            QPushButton:hover{
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                stop:0 rgb(100, 180, 255), 
                stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */
                color: black;
            }
            
            """

        # 1. Setup da Cena e View
        self.cena = QGraphicsScene(self)
        self.visao = VisaoRecorte(self.cena)
        
        # 2. Layout Principal (para a View ocupar tudo)
        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(0, 0, 0, 0) # Sem bordas
        layout_principal.addWidget(self.visao)

        # Configurações da View
        self.visao.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        self.visao.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.visao.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.visao.setFrameShape(QFrame.NoFrame) # Remove a borda da moldura

        # 3. Configurações da Imagem
        self.item_imagem = ItemPixmapMovel(pixmap)
        self.cena.addItem(self.item_imagem)

        # 4. Cálculo da Escala (Usando o tamanho fixo do diálogo)
        # Como o diálogo é fixo 520x560, usamos isso para o cálculo inicial
        rect_visao_w = 520
        rect_visao_h = 520 # Usamos a parte quadrada para a imagem
        rect_item = self.item_imagem.boundingRect()

        escala = max(
            rect_visao_w / rect_item.width(),
            rect_visao_h / rect_item.height()
        )
        self.item_imagem.setScale(escala)

        # 5. Centralização
        centro = rect_item.center()
        self.item_imagem.setPos(
            -centro.x() * escala,
            -centro.y() * escala
        )

        self.cena.setSceneRect(-2000, -2000, 4000, 4000)
        self.visao.centerOn(0, 0)

        # --- Botão Confirmar (Flutuante) ---
        # Criamos o botão com 'self' como pai para ele flutuar sobre o layout
        self.botao_confirmar = QPushButton(self)
        self.botao_confirmar.setFixedSize(60, 60)
        self.botao_confirmar.clicked.connect(self.accept)
        
        icone = QIcon(caminho_recurso("imagens/verificado.png"))
        self.botao_confirmar.setIcon(icone)
        self.botao_confirmar.setIconSize(QSize(28, 28))
        self.botao_confirmar.setCursor(Qt.PointingHandCursor)

        self.botao_confirmar.setStyleSheet(botao_style)

        # Posicionamento absoluto do botão
        self.posicionar_botao()
        
        # Garante que o botão fique na frente de tudo
        self.botao_confirmar.raise_()
        
        self.item_imagem.moveBy(0.001, 0)
        self.item_imagem.moveBy(-0.001, 0)

    def posicionar_botao(self):
        # Move o botão para o canto inferior direito
        margem = 25
        x = self.width() - self.botao_confirmar.width() - margem
        y = self.height() - self.botao_confirmar.height() - margem
        self.botao_confirmar.move(x, y)

    # Caso a janela mude de tamanho (mesmo sendo Fixed, é uma boa prática)
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.posicionar_botao()


    #  Nome em PT-BR (método seu, não é virtual do Qt)
    def obter_pixmap_recortado(self):
        visao = self.visao
        diametro = visao.diametro_recorte()
        raio = diametro / 2

        # Área do recorte na cena (fixa no centro 0,0)
        retangulo_cena = QRectF(-raio, -raio, diametro, diametro)

        # Converter da cena para o sistema do item (imagem)
        poligono_item = self.item_imagem.mapFromScene(retangulo_cena)
        retangulo_item = poligono_item.boundingRect()

        # Recorte direto da imagem ORIGINAL (SEM círculo)
        pixmap_original = self.item_imagem.pixmap()
        pixmap_recortado = pixmap_original.copy(retangulo_item.toRect())

        #  Retornamos SOMENTE o quadrado
        return pixmap_recortado


class DialogoAvatar(QDialog):
    imagem_alterada = Signal(str)

    def __init__(self, parent, caminho_imagem):
        super().__init__(parent)

        self.janela_pai = parent
        self.caminho_imagem = caminho_imagem
        self.db = DataBase()

        self.setWindowTitle("Foto do usuário")
        self.setModal(True)
        self.setFixedSize(320, 360)

        layout_principal = QVBoxLayout(self)
        layout_principal.setAlignment(Qt.AlignCenter)
        layout_principal.setContentsMargins(20, 20, 20, 20)

        self.label_foto = QLabel()
        self.label_foto.setFixedSize(200, 200)
        self.label_foto.setAlignment(Qt.AlignCenter)

        if caminho_imagem and os.path.exists(caminho_imagem):
            self.atualizar_previa(caminho_imagem)
        else:
            self.mostrar_placeholder()

        self.botao_alterar = QPushButton("Alterar foto")
        self.botao_alterar.setFixedHeight(36)
        self.botao_alterar.clicked.connect(self.alterar_foto)
        self.botao_alterar.setCursor(Qt.PointingHandCursor)
        
        self.botao_mostrar_foto = QPushButton("Mostrar foto")
        self.botao_mostrar_foto.setFixedHeight(36)
        self.botao_mostrar_foto.clicked.connect(self.ver_foto)
        self.botao_mostrar_foto.setCursor(Qt.PointingHandCursor)
        
        self.botao_remover_foto = QPushButton("Remover foto")
        self.botao_remover_foto.setFixedHeight(36)
        self.botao_remover_foto.clicked.connect(self.remover_foto)
        self.botao_remover_foto.setCursor(Qt.PointingHandCursor)
        

        layout_principal.addWidget(self.label_foto)
        layout_principal.addSpacing(20)
        layout_principal.addWidget(self.botao_alterar)
        layout_principal.addWidget(self.botao_mostrar_foto)
        layout_principal.addWidget(self.botao_remover_foto)
        
        self.animar_entrada()
        
    def animar_entrada(self):
        self.setWindowOpacity(0)

        self.anim_opacity = QPropertyAnimation(self, b"windowOpacity")
        self.anim_opacity.setDuration(230)
        self.anim_opacity.setStartValue(0)
        self.anim_opacity.setEndValue(1)

        self.anim_opacity.start()

    def mostrar_placeholder(self):
        # Pega o nome do usuário pela janela principal
        nome = self.janela_pai.get_nome_completo_usuario() or "Usuário"
        iniciais = self.janela_pai.gerar_iniciais(nome)

        self.label_foto.setText(iniciais)
        self.label_foto.setAlignment(Qt.AlignCenter)
        self.label_foto.setStyleSheet("""
            QLabel {
                border-radius: 100px;
                background-color: #4f46e5;
                color: white;
                font-weight: bold;
                font-size: 48px;
            }
        """)

    def atualizar_previa(self, novo_caminho):
        if not novo_caminho or not os.path.exists(novo_caminho):
            self.mostrar_placeholder()
            return

        pixmap = QPixmap(novo_caminho)
        pixmap_circular = self.janela_pai.pixmap_circular(pixmap, 200)

        self.label_foto.setText("")
        self.label_foto.setPixmap(pixmap_circular)

        #  SOMBRA SUAVE
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(20)        # quão difusa é a sombra
        sombra.setOffset(0, 4)          # deslocamento (baixo)
        sombra.setColor(QColor(0, 0, 0, 120))  # preto translúcido

        self.label_foto.setGraphicsEffect(sombra)

        self.label_foto.setStyleSheet("background-color: transparent;")



    def alterar_foto(self):
        novo_caminho = self.janela_pai.alterar_foto_usuario(retornar_caminho=True)
        if novo_caminho:
            self.caminho_imagem = novo_caminho
            self.atualizar_previa(novo_caminho)
            
    def ver_foto(self):
        if not self.caminho_imagem or not os.path.exists(self.caminho_imagem):
            QMessageBox.warning(self,"Aviso","Não há uma imagem para ser exibida")
            return
            
        dialogo_visor = QDialog(self)
        dialogo_visor.setWindowTitle("Visualizar foto")
        dialogo_visor.setFixedSize(600, 600) # Forçamos a janela a ser 600x600
        
        layout = QVBoxLayout(dialogo_visor)
        layout.setContentsMargins(0, 0, 0, 0)
        
        label_visor = QLabel()
        label_visor.setAlignment(Qt.AlignCenter)
        
        pixmap_original = QPixmap(self.caminho_imagem)
        
        pixmap_grande = pixmap_original.scaled(
            600,600,
            Qt.KeepAspectRatioByExpanding,
            Qt.SmoothTransformation
        )
        
        pixmap_final = pixmap_grande.copy(
            (pixmap_grande.width() - 600) // 2,
            (pixmap_grande.height() - 600) // 2,
            600, 600
        )
        
        label_visor.setPixmap(pixmap_final)
        layout.addWidget(label_visor)
        
        dialogo_visor.exec()
        
    def remover_foto(self):
        usuario = self.janela_pai.get_usuario_logado() 

        if not usuario:
            return

        resposta = QMessageBox.question(
            self,
            "Remover foto",
            "Deseja realmente remover a foto do usuário?",
            QMessageBox.Yes | QMessageBox.No
        )

        if resposta != QMessageBox.Yes:
            return

        caminho = self.db.obter_imagem_usuario(usuario)

        # Remove arquivo físico
        if caminho and os.path.exists(caminho):
            try:
                os.remove(caminho)
            except Exception as e:
                QMessageBox.warning(
                    self,
                    "Erro",
                    f"Não foi possível remover a imagem:\n{e}"
                )
                return

        #  REMOVE DO BANCO
        self.db.salvar_imagem_usuario(usuario, None)

        # Atualiza estado global
        self.janela_pai.caminho_foto_usuario = None
        self.janela_pai.atualizar_avatar()

        # Atualiza preview do diálogo
        self.caminho_imagem = None
        self.mostrar_placeholder()




class Temas:
    def __init__(self):
        self._caminho_config = self._resolver_caminho_config()
        self.config = self.carregar_config_arquivo()

    def _resolver_caminho_config(self):
        if getattr(sys, "frozen", False):
            # EXE → AppData
            pasta = os.path.join(
                os.environ.get("APPDATA"),
                "SistemaGerenciamento"
            )
            os.makedirs(pasta, exist_ok=True)
            return os.path.join(pasta, "config.json")
        else:
            # Python → pasta do projeto
            return os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "config.json"
            )

    def carregar_config_padrao(self):
        return {
            "tema": "classico",
            "usuario": "",
            "senha": "",
            "mantem_conectado": False,
            "nao_mostrar_mensagem_boas_vindas": False,
            "nao_mostrar_aviso_irreversivel": False,
            "nao_mostrar_mensagem_arquivo_excel": False,
            "nao_mostrar_mensagem_arquivo_excel_fisicos": False,
            "historico_autocompletes": {}
        }

    def carregar_config_arquivo(self):
        caminho = self._caminho_config

        if not os.path.exists(caminho):
            self.salvar_config(self.carregar_config_padrao())
            return self.carregar_config_padrao()

        try:
            with open(caminho, "r", encoding="utf-8") as f:
                conteudo = f.read().strip()
                if not conteudo:
                    return self.carregar_config_padrao()
                return json.loads(conteudo)
        except Exception as e:
            print(f"Erro ao ler config.json: {e}")
            return self.carregar_config_padrao()

    def salvar_config(self, dados: dict):
        with open(self._caminho_config, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)



    def aplicar_tema_global(self,app: QApplication):
        tema = self.config.get("tema", "classico")
        
        if tema == "escuro":
            app.setStyleSheet("""
            QMainWindow, QStackedWidget {
                background-color: #2b2b2b;
                color: #ffffff;
            }
            QWidget{
                background-color: #2b2b2b;
                color: #ffffff;
            }
            /* Estiliza apenas o QTableView das tables abaixo */
            QTableView#table_ativos,
            QTableView#table_inativos,
            QTableView#table_base,
            QTableView#table_saida,
            QTableView#table_massa_usuarios,
            QTableView#table_massa_produtos,
            QTableView#table_clientes_juridicos,
            QTableView#table_clientes_fisicos {    
                gridline-color: white;
                border: 1px solid white;
                color: black;
                selection-color: white;
            }
            /* QTableView com seleção diferenciada */
            QTableView {
                background-color: #2b2b2b;
                color: black;
                gridline-color: #555555;
                selection-background-color: #7a7a7a;
                selection-color: white;
            }
            /* Coluna dos cabeçalhos */
            QHeaderView::section {
                background-color: #ffffff;
                color: black;
                border: 1px solid #aaaaaa;
                padding: 1px;
            }

            /* QTabWidget headers brancos */
            QTabWidget::pane {
                border: 1px solid #444444;
                background-color: #202124;
            }
            /* Estiliza a barra de rolagem horizontal */
            QTableView QScrollBar:horizontal {
                border: none;
                background-color: #ffffff;
                height: 12px;
                margin: 0px;
                border-radius: 5px;
            }

            /* Estiliza a barra de rolagem vertical */
            QTableView QScrollBar:vertical {
                border: none;
                background-color: #ffffff;  
                width: 12px;
                margin: 0px;
                border-radius: 5px;
            }
            
            /* Parte que você arrasta */
            QTableView QScrollBar::handle:vertical {
                background-color: #777777;  /* cinza médio */
                min-height: 22px;
                border-radius: 5px;
            }

            QTableView QScrollBar::handle:horizontal {
                background-color: #777777;
                min-width: 22px;
                border-radius: 5px;
            }

            /* Groove horizontal */
            QTableView QScrollBar::groove:horizontal {
                background-color: #3a3a3a;  /* faixa mais clara */
                border-radius: 5px;
                height: 15px;
                margin: 0px 10px 0px 10px;
            }

            /* Groove vertical */
            QTableView QScrollBar::groove:vertical {
                background-color: #3a3a3a;
                border-radius: 5px;
                width: 25px;
                margin: 10px 0px 10px 10px;
            }

            /* Estilo para item selecionado */
            QTableWidget::item:selected {
                background-color: #555555;  /* cinza de seleção */
                color: white;
            }
            QTabWidget#tab_clientes_todos::pane {
                border: none;
            }
            
            QTabBar::tab {
                background-color: #ffffff; /* fundo branco */
                color: black;
                padding: 6px 12px;
                border: 1px solid #888888;
                border-bottom: none;
            }

            QTabBar::tab:selected {
                background-color: #d6d6d6;   /* cinza médio para destacar */
                color: black;                /* texto bem visível */
                font-weight: bold;           /* destaque no selecionado */
            }

            QTabBar::tab:hover {
                background-color: #f5f5f5;
            }
            /* Botões gerais */
            QPushButton {
                border-radius: 8px;
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(60, 60, 60),   /* topo */
                    stop:1 rgb(100, 100, 100) /* base */
                );      
                min-height: 24px;  /* Adicione esta linha */
            }

            QPushButton:hover {
                background-color: #444444;
            }

            QPushButton:pressed {
                background-color: #555555;
                border: 2px solid #888888;
            }
            /* Botões de menu principal */
            QPushButton#btn_home,
            QPushButton#btn_verificar_estoque,
            QPushButton#btn_verificar_usuarios,
            QPushButton#btn_cadastrar_produto,
            QPushButton#btn_cadastrar_usuarios,
            QPushButton#btn_clientes {
                border-radius: 8px;
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(60, 60, 60),   /* topo */
                    stop:1 rgb(100, 100, 100) /* base */
                );
                color: #ffffff; /* texto branco */
                min-width: 130px;   /* largura mínima */
                min-height: 21px;   /* altura mínima */
            }

            QPushButton#btn_home:hover,
            QPushButton#btn_verificar_estoque:hover,
            QPushButton#btn_verificar_usuarios:hover,
            QPushButton#btn_cadastrar_produto:hover,
            QPushButton#btn_cadastrar_usuarios:hover,
            QPushButton#btn_clientes:hover{
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(90, 90, 90),
                    stop:1 rgb(130, 130, 130)
                );
            }

            QPushButton#btn_home:pressed,
            QPushButton#btn_verificar_estoque:pressed,
            QPushButton#btn_verificar_usuarios:pressed,
            QPushButton#btn_cadastrar_produto:pressed,
            QPushButton#btn_cadastrar_usuarios:pressed,
            QPushButton#btn_clientes:pressed{
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(50, 50, 50),
                    stop:1 rgb(80, 80, 80)
                );
            }
            /* Botão de login */
            QPushButton#btn_login {
                border-radius: 8px;
                width: 120px;   /* largura mínima */
                min-height: 21px;   /* altura mínima */
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(60, 60, 60),   /* topo */
                    stop:1 rgb(100, 100, 100) /* base */
                );
            }
            QPushButton#btn_login:hover{
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(90, 90, 90),
                    stop:1 rgb(130, 130, 130)
                );
            }

            /* Campos de entrada */
            QLineEdit#txt_senha,
            QLineEdit#txt_usuario {
                border: 2px solid #555555;      /* borda sutil em cinza escuro */
                border-radius: 5px;             /* bordas arredondadas */
                padding: 5px;                   /* espaçamento interno */
                background-color: #2e2e2e;      /* fundo escuro */
                color: #ffffff;                 /* texto branco */
            }
            /* Placeholder */
            QLineEdit#txt_usuario::placeholder,
            QLineEdit#txt_senha::placeholder {
                color: #bbbbbb;  /* placeholder cinza claro */
            }
            QLineEdit#line_excel_usuarios,
            QLineEdit#line_edit_massa_usuarios,
            QLineEdit#line_edit_massa_produtos,
            QLineEdit#line_excel,
            QLineEdit#line_excel_usuarios{
              color: #ffffff; /* texto branco */
                background-color: #2b2b2b; /* fundo escuro */
                border: 3px solid #ffffff; /* branco */
                border-radius: 13px; /* cantos arredondados */
                padding: 3px;
                selection-background-color: #3296fa; /* fundo da seleção */
                selection-color: #ffffff; /* texto da seleção */  
            }
            QLineEdit{
                color: #ffffff; /* texto branco */
                background-color: #2b2b2b; /* fundo escuro */
                border: 2px solid #ffffff; /* branco */
                border-radius: 6px; /* cantos arredondados */
                padding: 3px;
                selection-background-color: #3296fa; /* fundo da seleção */
                selection-color: #ffffff; /* texto da seleção */
            }

            QLineEdit::placeholderText {
                color: #bbbbbb; /* placeholder em cinza claro */
            }

            QComboBox#perfil_estado,
            QComboBox#perfil_usuarios{
                color: #f0f0f0;                 /* Texto claro */
                border: 2px solid #ffffff;      /* Borda branca */
                border-radius: 6px;
                padding: 4px 10px;
                background-color: #2b2b2b; /* Fundo do combobox */
            
            }
            QComboBox#perfil_estado QAbstractItemView::item:hover,
            QComboBox#perfil_usuarios QAbstractItemView::item:hover {
                background-color: #444444; /* Cor de fundo quando o mouse passa por cima */
                color: #f0f0f0;            /* Cor do texto quando o mouse passa por cima */
            }
            QComboBox#perfil_estado QAbstractItemView::item:selected,
            QComboBox#perfil_usuarios QAbstractItemView::item:selected {
                background-color: #696969; /* Fundo do item selecionado */
                color: #f0f0f0;            /* Texto do item selecionado */
            }


            /* Scroll dentro do menu suspenso */
            QComboBox#perfil_estado QAbstractItemView::item,
            QComboBox#perfil_usuarios QAbstractItemView::item {
                height: 24px; /* Altura de cada item */
            }

            /* Fundo da barra do  scroll */
            QComboBox#perfil_estado QScrollBar:vertical,
            QComboBox#perfil_usuarios QScrollBar:vertical {
                background: #ffffff;
                width: 12px;
                margin: 0px 0px 0px 0px;
                border-radius: 6px;
            }
            /* Barra do scroll na cor cinza */
            QComboBox#perfil_estado QScrollBar::handle:vertical,
            QComboBox#perfil_usuarios QScrollBar::handle:vertical {
                background: #555555;
                border-radius: 6px;
            }

            QToolButton{
                border-radius: 8px;
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(60, 60, 60),
                    stop:1 rgb(100, 100, 100)
                );
                color: #ffffff;
                min-width: 120px;
                min-height: 30px;      
            }
            QToolButton:hover{
                background: qlineargradient(
                x1:0, y1:0, x2:0, y2:1,
                stop:0 rgb(90, 90, 90),
                stop:1 rgb(130, 130, 130)
            );
            }
            QToolButton:pressed {
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(50, 50, 50),
                    stop:1 rgb(80, 80, 80)
                );
            }
            QToolButton#btn_opcoes_extras{
                border-radius: 10px;
                min-width: 21px;
                min-height: 21px;
            }
            QToolButton#btn_opcoes_extras::menu-indicator{
                image: none;
            }
    
            QMenu::item:selected {
                background-color: #696969;
                color: white;
            }

            /* Frames com valores */
            QFrame#frame_valor_total_produtos,
            QFrame#frame_valor_do_desconto,
            QFrame#frame_valor_com_desconto1,
            QFrame#frame_quantidade {
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 #3a3b3e,   /* topo mais claro */
                    stop:1 #2a2b2e    /* base mais escura */
                );
                color: #ffffff;
                border: 1px solid #444444;
                border-radius: 10px;
            }
            QLabel#label_status_progress {
                background: transparent;
                color: white;
            }

            QLabel#label_foto_sistema{
                border: none;
                background: transparent;
            }
            QLabel#label_titulo,
            QLabel#label_valor{
                font-size: 14px; color: white; 
                font-family: Arial; font-weight: normal;
                background: transparent;
            }
            QLabel#label_cadastramento_produtos,
            QLabel#label_cadastramento,
            QLabel#label_ativos,
            QLabel#label_inativos,
            QLabel#label_estoque,
            QLabel#label_saida{
                text-align: center; /* Centraliza o texto horizontalmente */
                vertical-align: middle; /* Centraliza o texto verticalmente */
                border: 3px solid white;
            }
            QMessageBox {
                background-color: #2b2b2b;   /* fundo escuro */
                color: #2b2b2b;              /* texto claro */
                border: 2px solid #555555;
                border-radius: 10px;
            }
            QMessageBox QLabel {
                color: #f0f0f0;              /* cor do texto */
                font-size: 14px;
                background: transparent;
            }
            QMessageBox QDialogButtonBox QPushButton {
                background-color: #444444;
                color: #ffffff;
                border-radius: 6px;
                padding: 4px 10px;
            }
            QMessageBox QDialogButtonBox QPushButton:hover {
                background-color: #666666;
            }
            QMessageBox QDialogButtonBox QPushButton:pressed {
                background-color: #888888;
            }

           QDialog{
                background-color: #2b2b2b;
           } 
           QLabel{
                background: transparent;
           }
           QDialog QPushButton {
                background-color: #444444;
                color: #ffffff;
                border-radius: 6px;
                padding: 4px 10px;
            }
            QDialog QPushButton:hover {
                background-color: #666666;    /* Hover do botão */
            }
            QDateEdit {
                color: white; 
                background-color: #3b3b3b;  /* fundo escuro */
                border: 2px solid #ffffff;
                border-radius: 5px;
                padding: 2px 5px;
            }

            QDateEdit QCalendarWidget {
                background-color: #2b2b2b;   /* fundo escuro do popup */
                border: 1px solid #555555;
            }

            QDateEdit QCalendarWidget QAbstractItemView:enabled {
                background-color: #2b2b2b;
                color: white;
                selection-background-color: #555555;
                selection-color: white;
            }

            QDateEdit QCalendarWidget QToolButton {
                color: white;   /* setas claras */
                min-width: 20px;     /* menor largura dos botões de navegação */
                min-height: 20px;    /* menor altura */
                padding: 1px;
                background: transparent;
            }

            QDateEdit QCalendarWidget QToolButton:hover {
                background: #444444;
            }

            QDateEdit QCalendarWidget QMenu {
                background-color: #3b3b3b;
                color: white;
            }

            QDateEdit QCalendarWidget QMenu::item:selected {
                background: #555555;
                color: white;
            }
            QDateEdit QCalendarWidget QToolButton::menu-indicator {
                image: none;   /* remove o ícone padrão */
                width: 0px;    /* remove o espaço reservado */
            }
            QProgressBar {
                color: white;
                border: 3px solid #ffffff;
                border-radius: 13px;
                background-color: #2b2b2b; 
                text-align: center;
                padding: 0px;         
            }

            QProgressBar::chunk {
                background-color: #4682b4;
                border-radius: 12px;
                margin: 0px;
            }
            QFrame#frame_page_verificar_usuarios,
            QFrame#frame_pag_estoque,
            QFrame#frame_pg_clientes,
            QFrame#frame_10,
            QFrame#frame_8{
                border: 2px solid white;
            }
            QFrame#frame_2 {
                border-radius: 12px;
                border: 2px solid qlineargradient(
                    spread:pad, 
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 #ff7f50;   /* laranja neon */
                    stop:1 #ffff00;   /* amarelo neon */
                );
            }
            
        """)
        elif tema == "claro":
            app.setStyleSheet("""
            QMainWindow, QStackedWidget,QFrame  {
                background-color: #ffffff;
                color: #000000;
            }
            
            /* QTableView com seleção diferenciada */
            QTableView {
                background-color: #ffffff;
                color: black;
                gridline-color: #cccccc;
                selection-background-color: #0078d7; /* azul Windows */
                selection-color: #ffffff;
                border: 1px solid #dddddd;
            }
            QTableView::item {
                color: black;
            }

            /* Cabeçalhos da tabela */
            QHeaderView::section {
                background-color: #f5f5f5;
                color: #000000;
                border: 1px solid #cccccc;
                padding: 4px;
            }

            /* Estilo para item selecionado */
            QTableWidget::item:selected {
                background-color: #0078d7; /* Azul moderno */
                color: #ffffff;
            }

            /* QTabWidget - modo claro */
            QTabWidget::pane {
                border: 1px solid #cccccc;
                background-color: #ffffff;
            }

            QTabWidget#tab_clientes_todos::pane {
                border: none;
            }

            /* Scrollbar horizontal */
            QTableView QScrollBar:horizontal {
                border: none;
                background-color: #f0f0f0;
                height: 12px;
                margin: 0px;
                border-radius: 5px;
            }

            /* Scrollbar vertical */
            QTableView QScrollBar:vertical {
                border: none;
                background-color: #f0f0f0;
                width: 12px;
                margin: 0px;
                border-radius: 5px;
            }

            /* Parte que você arrasta - Handle */
            QTableView QScrollBar::handle:vertical {
                background-color: #b0b0b0;  /* cinza claro */
                min-height: 22px;
                border-radius: 5px;
            }

            QTableView QScrollBar::handle:horizontal {
                background-color: #b0b0b0;
                min-width: 22px;
                border-radius: 5px;
            }

            /* Groove horizontal */
            QTableView QScrollBar::groove:horizontal {
                background-color: #e0e0e0;
                border-radius: 5px;
                height: 15px;
                margin: 0px 10px 0px 10px;
            }

            /* Groove vertical */
            QTableView QScrollBar::groove:vertical {
                background-color: #e0e0e0;
                border-radius: 5px;
                width: 15px;
                margin: 10px 0px 10px 0px;
            }
            QTableCornerButton::section {
                background-color: #f5f5f5;
                border: 1px solid #cccccc;
                padding: 2px;
            }


            QMessageBox {
                background: qlineargradient(
                    x1: 0, y1: 0,
                    x2: 0, y2: 1,
                    stop: 0 #ffffff,       /* branco puro no topo */
                    stop: 0.2 #f5f5f5,     /* branco acinzentado na faixa */
                    stop: 1 #c0c0c0       /* branco acinzentado no resto */
                );
                color: black;
            }
            QMessageBox QLabel{
                background: transparent;
                color: black
            }
            QMessageBox QPushButton {
                background-color: #ffffff;
                color: black;
                border: 1px solid #0078d7;
                padding: 2px 10px;
                border-radius: 6px;
                min-width: 40px;
                min-height: 10px; 
                font-size: 12px; 
            }
            
            QMessageBox QPushButton:hover {
                background-color: #e6f0fa;
            }

            QMessageBox QPushButton:pressed {
                background-color: #c7d7f9;
            }
            QPushButton {
                outline: none;
            }

            QPushButton:focus {
                outline: none;
            }

            QToolButton {
                outline: none;
            }

            QToolButton:focus {
                outline: none;
            }
            QPushButton {
                outline: none;
            }

            QPushButton:focus {
                outline: none;
            }

            QToolButton {
                outline: none;
            }

            QToolButton:focus {
                outline: none;
            }
            /* Botões gerais  */
            QPushButton {
                border-radius: 8px;
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(220, 220, 220),  /* topo */
                    stop:1 rgb(245, 245, 245)   /* base */
                );
                font-size: 14px;
                color: #000000; /* texto escuro */
            }

            QPushButton:hover {
                background-color: #e0e0e0;
            }

            QPushButton:pressed {
                background-color: #d0d0d0;
                border: 2px solid #aaaaaa;
            }
            QPushButton#btn_login {
                font-size: 16px;
                border: 3px solid transparent;
            }
            

            QMenu {
                background-color: white;
                color: black;
                border: 1px solid gray;
            }

            QMenu::item {
                background-color: white;
                color: black;
            }

            QMenu::item:selected {
                background-color: #0078d7; /* Azul para item selecionado */
                color: white;
            }
            QMenu::separator {
                height: 1px;
                background: gray;
                margin: 5px 10px;
            }
            
            QLineEdit#txt_usuario,
            QLineEdit#txt_senha{
                border: 2px solid #0078d4;  /* Cor da borda */
                border-radius: 5px;          /* Bordas arredondadas */
                padding: 5px;                /* Espaçamento interno */
                color: black
        
            }
            QLineEdit {
                color: #000000; /* texto preto */
                background-color: #ffffff; /* fundo branco */
                border: 2px solid #0078d4; /* azul moderno, como nos botões */
                border-radius: 6px;
                padding: 3px;
                selection-background-color: #cce4f7; /* azul claro na seleção */
                selection-color: #000000; /* texto preto na seleção */
            }

            QLineEdit::placeholderText {
                color: #888888; /* placeholder em cinza médio */
            }
            QLineEdit:focus {
                border: 2px solid #005a9e; /* Azul mais escuro ao focar */
                background-color: #f0f8ff; /* Leve destaque no fundo */
            }
            
            QLabel#label_titulo,
            QLabel#label_valor{
                font-size: 16px;
                background: transparent;
                color: black; 
                
            }
            QLabel#label_status_progress {
                background: transparent;
                color: black;
            }
            QLabel#label_foto_sistema{
                border: none;
                background: transparent;
            }
            QLabel#label_estoque,
            QLabel#label_saida,
            QLabel#label_ativos,
            QLabel#label_inativos,
            QLabel#label_cadastramento_produtos,
            QLabel#label_cadastramento{
                border: 3px solid  #cccccc;
            }
            QComboBox#perfil_estado,
            QComboBox#perfil_usuarios {
                color: #2b2b2b;                 /* Texto escuro */
                border: 2px solid #0078d4;      /* Borda cinza clara */
                border-radius: 6px;
                padding: 4px 10px;
                background-color: #ffffff;      /* Fundo branco */
            }

            /* Hover em itens do dropdown */
            QComboBox#perfil_estado QAbstractItemView::item:hover,
            QComboBox#perfil_usuarios QAbstractItemView::item:hover {
                background-color: #f0f0f0;      /* Cinza muito claro ao passar o mouse */
                color: #000000;                 /* Texto preto */
            }

            /* Item selecionado no dropdown */
            QComboBox#perfil_estado QAbstractItemView::item:selected,
            QComboBox#perfil_usuarios QAbstractItemView::item:selected {
                background-color: #d0d0d0;      /* Cinza médio claro */
                color: #000000;                 /* Texto preto */
            }

            /* Altura dos itens */
            QComboBox#perfil_estado QAbstractItemView::item,
            QComboBox#perfil_usuarios QAbstractItemView::item {
                height: 24px;
            }

            /* Fundo da barra de scroll */
            QComboBox#perfil_estado QScrollBar:vertical,
            QComboBox#perfil_usuarios QScrollBar:vertical {
                background: #f0f0f0;            /* Cor de fundo do scroll */
                width: 12px;
                margin: 0px;
                border-radius: 6px;
            }

            /* Parte que você arrasta (scroll handle) */
            QComboBox#perfil_estado QScrollBar::handle:vertical,
            QComboBox#perfil_usuarios QScrollBar::handle:vertical {
                background: #b0b0b0;            /* Cinza claro */
                border-radius: 6px;
            }
            QToolButton {
                border-radius: 8px;
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(220, 220, 220),  /* topo */
                    stop:1 rgb(245, 245, 245)   /* base */
                );
                color: #000000; /* texto escuro */
                min-width: 120px;
                min-height: 30px; 
        
            }
            QToolButton:hover {
                background-color: #e0e0e0;
            }

            QToolButton:pressed {
                background-color: #d0d0d0;
                border: 2px solid #aaaaaa;
            }
            QToolButton#btn_opcoes_extras{
                border-radius: 10px;
                min-width: 21px;
                min-height: 21px;
            }
            QToolButton#btn_opcoes_extras::menu-indicator{
                image: none;
            }
            QDateEdit {
                color: #2b2b2b;                     /* Texto escuro */
                background-color: #ffffff;         /* Fundo branco */
                border: 2px solid #0078d4;         /* Borda cinza clara */
                border-radius: 5px;
                padding: 2px 5px;
            }

            QDateEdit QCalendarWidget {
                background-color: #ffffff;         /* Fundo branco do calendário */
                border: 1px solid #cccccc;
            }

            QDateEdit QCalendarWidget QAbstractItemView:enabled {
                background-color: #ffffff;         /* Fundo branco da grade */
                color: #2b2b2b;                    /* Texto escuro */
                selection-background-color: #d0d0d0; /* Fundo do item selecionado */
                selection-color: #000000;          /* Texto do item selecionado */
            }

            QDateEdit QCalendarWidget QToolButton {
                color: #2b2b2b;                    /* Setas escuras */
                min-width: 20px;
                min-height: 20px;
                padding: 1px;
                background: transparent;
            }

            QDateEdit QCalendarWidget QToolButton:hover {
                background: #e0e0e0;               /* Hover em botão de navegação */
            }

            QDateEdit QCalendarWidget QMenu {
                background-color: #ffffff;         /* Fundo do menu */
                color: #2b2b2b;                    /* Texto do menu */
            }

            QDateEdit QCalendarWidget QMenu::item:selected {
                background: #d0d0d0;               /* Fundo item selecionado */
                color: #000000;                    /* Texto item selecionado */
            }
            QDateEdit QCalendarWidget QToolButton::menu-indicator {
                image: none;   /* remove o ícone padrão */
                width: 0px;    /* remove o espaço reservado */
            }
            QFrame#frame_valor_total_produtos,
            QFrame#frame_valor_do_desconto,
            QFrame#frame_valor_com_desconto1,
            QFrame#frame_quantidade{
                background-color: #d9d9d9;
                border-radius: 15px;
            
            }
            QProgressBar {
                color: black;
                border: 2px solid black;
                border-radius: 13px;
                background-color: #ffffff;
                text-align: center;
                padding: 0px;
            }

            QProgressBar::chunk {
                background-color: #4682b4;
                border-radius: 12px;
                margin: 0px;
            }
            QProgressBar#progress_massa_produtos,
            QProgressBar#progress_massa_usuarios{
                border-radius: 13px;
                text-align: center; /* centraliza o texto */
                font-size: 14px;
                color: #000000; /* texto escuro */
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(220, 220, 220),  /* topo */
                    stop:1 rgb(245, 245, 245)   /* base */
                );
            }
            /* Parte preenchida da barra */
            QProgressBar#progress_massa_produtos::chunk,
            QProgressBar#progress_massa_usuarios::chunk{
                border-radius: 13px;
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 #4caf50,  /* verde inicial */
                    stop:1 #81c784   /* verde mais claro no final */
                );
            }
            QFrame#frame_page_verificar_usuarios,
            QFrame#frame_pag_estoque,
            QFrame#frame_pg_clientes,
            QFrame#frame_10,
            QFrame#frame_8{
                border: 2px solid #eaeaea;
            }      
            QFrame#frame_2 {
                border-radius: 12px;
                border: 2px solid qlineargradient(
                    spread:pad,
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 #36d1dc,   /* turquesa */
                    stop:1 #5b86e5    /* azul claro */
                );
            }
            """) 
            
        else:  # clássico
            app.setStyleSheet("""
            QMainWindow, QStackedWidget,  QFrame {
                background-color: #005079;
                color: #ffffff;
            }
            QCheckBox#btn_manter_conectado{
                color: white;
            }
            QMessageBox {
                background: qlineargradient(
                    x1: 0, y1: 0,
                    x2: 0, y2: 1,
                    stop: 0 #ffffff,       /* branco puro no topo */
                    stop: 0.2 #f5f5f5,     /* branco acinzentado na faixa */
                    stop: 1 #c0c0c0       /* branco acinzentado no resto */
                );
                color: black;
            }
            QMessageBox QLabel{
                background-color: transparent;
                color: black;
            }
            QMessageBox QPushButton {
                background-color: #ffffff;
                color: black;
                border: 1px solid #0078d7;
                padding: 2px 10px;
                border-radius: 6px;
                min-width: 40px;
                min-height: 10px; 
                font-size: 12px; 
            }
            
            QMessageBox QPushButton:hover {
                background-color: #e6f0fa;
            }

            QMessageBox QPushButton:pressed {
                background-color: #c7d7f9;
            }
            QMenu {
                background-color: white;
                color: black;
                border: 1px solid gray;
            }

            QMenu::item {
                background-color: white;
                color: black;
            }

            QMenu::item:selected {
                background-color: #0078d7; /* Azul para item selecionado */
                color: white;
            }

            QMenu::separator {
                height: 1px;
                background: gray;
                margin: 5px 10px;
            }

            QPushButton#btn_incluir_produto_sistema{
                font-size: 12px;
            }
            QPushButton{
                color: rgb(255, 255, 255);
                border-radius: 8px;
                font-size: 16px;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(50, 150, 250), stop:1 rgb(100, 200, 255)); /* Gradiente de azul claro para azul mais claro */
                border: 4px solid transparent;
            }
            
            QPushButton:hover{
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                stop:0 rgb(100, 180, 255), 
                stop:1 rgb(150, 220, 255)); /* Gradiente de azul mais claro para azul ainda mais claro */
                color: black;
            }

            QPushButton#btn_opcoes_extras{
                color: rgb(255, 255, 255);
                border-radius: 10px;
                border:  transparent;
                background-color: rgb(100, 200, 255);
            }
            QPushButton#btn_login {
                font-size: 16px;
                border: 3px solid transparent;
            }
            QPushButton#btn_login:hover {
                color: black;
            }
            QPushButton {
                outline: none;
            }

            QPushButton:focus {
                outline: none;
            }

            QToolButton {
                outline: none;
            }

            QToolButton:focus {
                outline: none;
            }

            QLineEdit#txt_usuario,
            QLineEdit#txt_senha{
                border: 2px solid #0078d4;  /* Cor da borda */
                border-radius: 5px;          /* Bordas arredondadas */
                padding: 5px;                /* Espaçamento interno */
                background-color: #005079;      
        
            }
           
            QLineEdit#txt_usuario,
            QLineEdit#txt_senha{
                color: black;  /* Cor do placeholder */
            }
            
            QLineEdit#txt_nome,
            QLineEdit#txt_usuario_cadastro,
            QLineEdit#txt_senha_cadastro,
            QLineEdit#txt_confirmar_senha,
            QLineEdit#txt_cep,
            QLineEdit#txt_endereco,
            QLineEdit#txt_numero,
            QLineEdit#txt_cidade,
            QLineEdit#txt_bairro,
            QLineEdit#txt_complemento,
            QLineEdit#txt_telefone,
            QLineEdit#txt_email,
            QLineEdit#txt_data_nascimento,
            QLineEdit#txt_rg,
            QLineEdit#txt_cpf,
            QLineEdit#txt_cnpj,
            QLineEdit#txt_produto,
            QLineEdit#txt_quantidade,
            QLineEdit#txt_valor_produto_3,
            QLineEdit#txt_desconto_3,
            QLineEdit#txt_codigo_item,
            QLineEdit#txt_cliente_3,
            QLineEdit#txt_descricao_produto_3,
            QLineEdit#line_edit_massa_usuarios,
            QLineEdit#line_edit_massa_produtos,
            QLineEdit#line_excel_usuarios,
            QLineEdit#line_excel{
                color: black;
                background-color: rgb(240, 240, 240); /* Cor de fundo cinza claro */
                border: 2px solid rgb(50, 150, 250);  /* Borda azul */
                border-radius: 6px;                   /* Cantos arredondados */
                padding: 3px;                         /* Espaçamento interno */
            }

            QLineEdit#txt_nome::placeholderText,
            QLineEdit#txt_usuario_cadastro::placeholderText,
            QLineEdit#txt_senha_cadastro::placeholderText,
            QLineEdit#txt_confirmar_senha::placeholderText,
            QLineEdit#txt_cep::placeholderText,
            QLineEdit#txt_endereco::placeholderText,
            QLineEdit#txt_numero::placeholderText,
            QLineEdit#txt_cidade::placeholderText,
            QLineEdit#txt_bairro::placeholderText,
            QLineEdit#txt_complemento::placeholderText,
            QLineEdit#txt_telefone::placeholderText,
            QLineEdit#txt_email::placeholderText,
            QLineEdit#txt_data_nascimento::placeholderText,
            QLineEdit#txt_rg::placeholderText,
            QLineEdit#txt_cpf::placeholderText,
            QLineEdit#txt_cnpj::placeholderText,
            QLineEdit#txt_produto::placeholderText,
            QLineEdit#txt_quantidade::placeholderText,
            QLineEdit#txt_valor_produto_3::placeholderText,
            QLineEdit#txt_desconto_3::placeholderText,
            QLineEdit#txt_codigo_item::placeholderText,
            QLineEdit#txt_cliente_3::placeholderText,
            QLineEdit#line_edit_massa_usuarios::placeholderText,
            QLineEdit#line_edit_massa_produtos::placeholderText,
            QLineEdit#line_excel_usuarios::placeholderText,
            QLineEdit#line_excel::placeholderText,
            QLineEdit#txt_descricao_produto_3::placeholderText {
                color: black; /* Cor do texto do placeholder */
            }
                
            /* Estilo geral do QDateEdit */
            QDateEdit {
                color: black; 
                background-color: white; 
                border: 3px solid rgb(50,150,250);
                border-radius: 5px;
                padding: 2px 5px;
            }

            /* Remove o fundo das setas */
            QDateEdit::up-button, 
            QDateEdit::down-button {
                background: transparent;
                border: none;
            }

            /* Cor de fundo do calendário popup */
            QDateEdit QCalendarWidget {
                background-color: white;
                border: 1px solid rgb(150, 150, 150);
            }

            /* Dias normais */
            QDateEdit QCalendarWidget QAbstractItemView:enabled {
                background-color: white;
                color: black;
                selection-background-color: rgb(0, 120, 215); /* Azul no dia selecionado */
                selection-color: white;
            }
            /* Botões de navegação (setas) do calendário */
            QDateEdit QCalendarWidget QToolButton {
                background: transparent;   /* tira o fundo azul */
                color: black;              /* deixa as setas pretas */
                border: none;              /* sem borda */
                icon-size: 16px 16px;      /* ajusta o tamanho do ícone */
                padding: 2px;
            }
            QDateEdit QCalendarWidget QToolButton:hover {
                background: rgb(220, 220, 220); /* cinza claro no hover */
                border-radius: 4px;
            }
            /* Popup de meses/anos do calendário (QMenu) */
            QDateEdit QCalendarWidget QMenu {
                background-color: white;
                border: 1px solid #ccc;
                color: black;
            }

            QDateEdit QCalendarWidget QMenu::item {
                background: transparent;
                color: black;
                padding: 6px 16px;
            }

            QDateEdit QCalendarWidget QMenu::item:selected {
                background: rgb(0, 120, 215);
                color: white;
            }
            QDateEdit QCalendarWidget QToolButton::menu-indicator {
                image: none;   /* remove o ícone padrão */
                width: 0px;    /* remove o espaço reservado */
            }
                
            QComboBox { 
                background-color: white; 
                border:  2px solid rgb(50,150,250); 
                border-radius: 5px; 
                color: black; 
                padding: 5px;
            }
            QComboBox QAbstractItemView {
                background-color: white; 
                color: black; 
                border: 1px solid #ccc; 
                selection-background-color: #e5e5e5; 
                selection-color: black;
            }
            QComboBox QAbstractItemView QScrollBar:vertical {
                background: #f5f5f5; 
                width: 12px; 
                border: none;
            }
            QComboBox QAbstractItemView QScrollBar::handle:vertical {
                background: #cccccc; 
                min-height: 20px; 
                border-radius: 5px;
            }
            QComboBox QAbstractItemView QScrollBar::add-line:vertical, 
            QComboBox QAbstractItemView QScrollBar::sub-line:vertical {
                background: none;
                height: 0px;  /* Remove os botões de linha (setas de cima e baixo) */
            }
            QComboBox QAbstractItemView QScrollBar::add-page:vertical, 
            QComboBox QAbstractItemView QScrollBar::sub-page:vertical {
                background: none;
            }

            QTableView{
                gridline-color: black;
                color: black;
                selection-color: white;
                border: 2px solid white;
            }
            /* Cabeçalho das colunas */
            QHeaderView::section {
                color: black;
            }
            /* Estiliza a barra de rolagem horizontal */
            QTableView QScrollBar:horizontal {
                border: none;
                background-color: rgb(255, 255, 255);
                height: 10px;
                margin: 0px 10px 0px 10px;
            }
            QTableView QScrollBar::handle:horizontal{
                background-color: rgb(180,180,150);
                min-width: 10px;
                border-radius: 5px;
            }
            /* Estiliza a barra de rolagem vertical */
            QTableView QScrollBar:vertical {
                border: none;
                background-color: rgb(255, 255, 255); /* branco */
                width: 30px;
                margin: 0px 10px 0px 10px;
            }
            /* Parte que você arrasta */
            QTableView QScrollBar::handle:vertical {
                background-color: rgb(180, 180,150);  /* cinza */
                min-height: 26px;
                border-radius: 5px;
            }

            /* Remove os botões */
            QTableView QScrollBar::add-line:vertical,
            QTableView QScrollBar::sub-line:vertical {
                height: 0px;
                width: 0px;
                border: none;
                background: none;
            }

            QTableView QScrollBar::groove:horizontal{
                background-color: rgb(100,240,240);
                border-radius: 2px;
                height: 15px;
                margin: 0px 10px 0px 10px;
            }

            /* Estilo para item selecionado */
            QTableView::item:selected {
                background-color: rgb(0, 120, 215);
                color: white;
            }
            QTabBar::tab {
                color: black;  /* Cor do texto de todas as tabs */
                }
            QTabBar::tab:selected {
                color: black;
            }
            QTabBar#tb_base::tab {
                color: transparent; /* Esconde o texto */
                height: 1px;         /* Opcional: aba bem pequena */
                width: 1px;          /* Opcional: aba bem pequena */
            }
            QToolButton {
                background-color: rgb(50, 150, 250);
                color: white;
                border-radius: 5px;
                border: 2px solid rgb(50, 150, 250);
                padding: 5px 10px;
            }

            QToolButton:hover {
                background-color: rgb(100, 180, 255);
                border: 2px solid rgb(100, 180, 255);
            }
            

            /* Menu do btn_mais_opcoes */
            QToolButton#btn_mais_opcoes QMenu {
                background-color: white;     
                border: 1px solid #ccc;
                color: black;
            }

            /* Itens dentro desse menu */
            QToolButton#btn_mais_opcoes QMenu::item {
                background-color: transparent;
                color: black;
                padding: 6px 20px;
            }

            /* Item em hover/selecionado */
            QToolButton#btn_mais_opcoes QMenu::item:selected {
                background-color: rgb(0, 120, 215);
                color: white;
            }

            QFrame#frame_valor_total_produtos,
            QFrame#frame_valor_do_desconto,
            QFrame#frame_valor_com_desconto1,
            QFrame#frame_quantidade{
                background-color: rgb(100, 200, 100); 
                border-radius: 10px;
            }
            QLabel#label_status_progress {
                background: transparent;
                color: black;
            }
            QLabel#label_foto_sistema{
                border: none;
                background: transparent;
            }
            QLabel#label_titulo,
            QLabel#label_valor{
                font-size: 14px; color: white; 
                font-family: Arial; font-weight: normal;
                background: transparent;
            }
            QLabel#label_cadastramento_produtos,
            QLabel#label_cadastramento,
            QLabel#label_ativos,
            QLabel#label_inativos,
            QLabel#label_estoque,
            QLabel#label_saida{
                text-align: center; /* Centraliza o texto horizontalmente */
                vertical-align: middle; /* Centraliza o texto verticalmente */
                border: 3px solid white;
            }
            QProgressBar {
                color: black;
                border: 3px solid rgb(50,150,250);
                border-radius: 13px; 
                background-color: #f0f0f0;  
                min-height: 10px;
                text-align: center;
                padding: 0px;
            }

            QProgressBar::chunk {
                background-color: #4682b4;  
                border-radius: 12px;  
                margin: 0px;
            }
            QToolButton#btn_classe_atalhos{
                font-size: 14px;
            
            }
            QToolButton#btn_classe_tema,
            QToolButton#btn_classe_atualizacoes,
            QToolButton#btn_classe_hora,
            QToolButton#btn_classe_fonte,
            QToolButton#btn_classe_notificacoes{
                color: rgb(255, 255, 255);
                border-radius: 8px;
                font-size: 16px;
                width: 120px;
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(50, 150, 250),
                    stop:1 rgb(100, 200, 255)
                ); /* Gradiente de azul claro para azul mais claro */
                border: 4px solid transparent;
            }

            QToolButton#btn_classe_tema:hover,
            QToolButton#btn_classe_atualizacoes:hover,
            QToolButton#btn_classe_hora:hover,
            QToolButton#btn_classe_fonte:hover,
            QToolButton#btn_classe_notificacoes:hover,
            QToolButton#btn_classe_atalhos:hover {
                background: qlineargradient(
                    x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgb(100, 180, 255),
                    stop:1 rgb(150, 220, 255)
                ); /* Gradiente de azul mais claro para azul ainda mais claro */
                color: black;
            }
            QToolButton#btn_opcoes_extras{
                border: transparent;
                border-radius: 10px;
                max-width: 21px;
                max-height: 21px;
                }
            QToolButton#btn_opcoes_extras::menu-indicator{
                image: none;
            }  
            QMenu#menu_classe_tema,
            QMenu#menu_classe_atualizacoes,
            QMenu#menu_classe_hora,
            QMenu#menu_classe_fonte,
            QMenu#menu_classe_notificacoes,
            QMenu#menu_classe_atalhos {
                background-color: white;
                color: black;
                border: 1px solid gray;
            }

            QMenu#menu_classe_tema::item:selected,
            QMenu#menu_classe_atualizacoes::item:selected,
            QMenu#menu_classe_hora::item:selected,
            QMenu#menu_classe_fonte::item:selected,
            QMenu#menu_classe_notificacoes::item:selected,
            QMenu#menu_classe_atalhos::item:selected {
                background-color: #0078d7;
                color: white;
            }
            QFrame#frame_page_verificar_usuarios,
            QFrame#frame_pag_estoque,
            QFrame#frame_10,
            QFrame#frame_8{
                border: 2px solid white;
            }  
            QFrame#frame_2 {
                border-radius: 12px;
                border: 2px solid qlineargradient(
                    spread:pad, 
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 #1de9b6, 
                    stop:1 #0d47a1
                );
            } 
            
        """)


