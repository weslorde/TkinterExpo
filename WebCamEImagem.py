import cv2
import tkinter as tk
from PIL import Image, ImageTk

# Caminho da imagem de fundo
CAMINHO_IMAGEM = "C:/Users/WesPC/Desktop/TkinterExpo/img1.jpg"  # <- troque pelo seu arquivo de imagem

# Inicia janela Tkinter em tela cheia
janela = tk.Tk()
janela.title("Imagem com Webcam")
janela.attributes('-fullscreen', True)

# Função para sair com tecla ESC
def sair(event=None):
    camera.release()
    janela.destroy()

janela.bind("<Escape>", sair)

# Carrega a imagem de fundo e ajusta à tela cheia
screen_width = janela.winfo_screenwidth()
screen_height = janela.winfo_screenheight()
imagem_fundo = Image.open(CAMINHO_IMAGEM).resize((screen_width, screen_height))
imgtk_fundo = ImageTk.PhotoImage(imagem_fundo)

# Label da imagem de fundo
label_fundo = tk.Label(janela, image=imgtk_fundo)
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

# Inicia a webcam
camera = cv2.VideoCapture(0)

# Tamanho da mini webcam
largura_webcam = 240
altura_webcam = 180

# Label da webcam
label_webcam = tk.Label(janela)
label_webcam.place(x=screen_width - largura_webcam - 20, y=20)  # Canto superior direito

# Atualiza webcam ao vivo
def atualizar_webcam():
    ret, frame = camera.read()
    if ret:
        frame = cv2.resize(frame, (largura_webcam, altura_webcam))
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        imgtk = ImageTk.PhotoImage(image=img)
        label_webcam.imgtk = imgtk
        label_webcam.configure(image=imgtk)
    label_webcam.after(10, atualizar_webcam)

# Captura foto ao pressionar ESPAÇO
def capturar_foto(event=None):
    ret, frame = camera.read()
    if ret:
        cv2.imwrite("foto_capturada.jpg", frame)
        print("📸 Foto salva como 'foto_capturada.jpg'")

# Ligações de teclas
janela.bind("<space>", capturar_foto)

# Inicia
atualizar_webcam()
janela.mainloop()
