import tkinter as tk
from PIL import Image, ImageTk

# Lista de caminhos das imagens
imagens = ['img1.jpg', 'img2.jpg', 'img3.jpg', 'img4.jpg', 'img5.jpg']

class App:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)  # Janela em tela cheia
        self.root.bind("<Escape>", lambda e: root.destroy())  # Tecla ESC para sair

        self.label_imagem = tk.Label(root)
        self.label_imagem.pack(fill='both', expand=True)

        self.imagens_tk = [self.carregar_imagem(path) for path in imagens]
        self.imagem_atual = 0
        self.mostrar_imagem(self.imagem_atual)

        # Associa as teclas 1 a 5
        for i in range(1, 6):
            self.root.bind(str(i), self.mudar_imagem)

    def carregar_imagem(self, caminho):
        # Redimensiona a imagem para o tamanho da tela
        imagem = Image.open(caminho)
        largura = self.root.winfo_screenwidth()
        altura = self.root.winfo_screenheight()
        imagem = imagem.resize((largura, altura), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(imagem)

    def mostrar_imagem(self, indice):
        self.label_imagem.config(image=self.imagens_tk[indice])
        self.label_imagem.image = self.imagens_tk[indice]

    def mudar_imagem(self, evento):
        tecla = evento.char
        if tecla.isdigit():
            indice = int(tecla) - 1
            if 0 <= indice < len(self.imagens_tk):
                self.imagem_atual = indice
                self.mostrar_imagem(indice)

# Iniciar o app
root = tk.Tk()
app = App(root)
root.mainloop()
