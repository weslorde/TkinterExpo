import cv2
import tkinter as tk
from PIL import Image, ImageTk


import google.generativeai as genai
import PIL.Image


################################
####      GEMINI Funcao     ####
################################

# Configurar sua chave de API do Gemini
genai.configure(api_key="AIzaSyCqN2F-KV49jzUfdl1_kkzpJiPT3eUNVcI")

# Define a função para identificar a peça
def identificar_peca():
    caminho_imagem = "foto_capturada.jpg"
    try:
        imagem = PIL.Image.open(caminho_imagem)
        modelo = genai.GenerativeModel("gemini-2.0-flash")
        
        resposta = modelo.generate_content([
            imagem,
            "Qual a peça de computador/notebook/celular dessa imagem? Preciso da resposta somente com o nome da peça e nada mais, sem ponto final e nada da forma mais direta em portugues."
        ])
        
        return resposta.text.strip()
    except Exception as e:
        return f"Erro ao identificar a peça: {e}"
    

################################
####   Aplicativo Funcoes   ####
################################

# Inicia a janela em tela cheia
janela = tk.Tk()
janela.title("Visor de Foto com Webcam")
janela.attributes("-fullscreen", True)

# Obtém resolução da tela
screen_width = janela.winfo_screenwidth()
screen_height = janela.winfo_screenheight()

# === WEBCAM ===
camera = cv2.VideoCapture(0)
largura_webcam = 240 
altura_webcam = 180

# Label da imagem de fundo
label_fundo = tk.Label(janela)
label_fundo.place(x=0, y=0, relwidth=1, relheight=1) # Posição da imagem de fundo

# Label da webcam
label_webcam = tk.Label(janela)
label_webcam.place(x=screen_width - largura_webcam - 20, y=20) # Posição da webcam

# === FUNÇÃO: Mudar imagem de fundo dinamicamente ===
def mudar_fundo(caminho_imagem):
    # Coloca a extensão no nome da imagem
    caminho_imagem = caminho_imagem + ".jpg"
    global imgtk_fundo
    try:
        # Tenta abrir a imagem e redimensioná-la para o tamanho da tela
        imagem = Image.open(caminho_imagem).resize((screen_width, screen_height))
        imgtk_fundo = ImageTk.PhotoImage(imagem)
        label_fundo.configure(image=imgtk_fundo)
        #Se der erro, mostra uma mensagem
    except Exception as e:
        print(f"Erro ao mudar imagem de fundo: {e}")

# === FUNÇÃO: Atualizar webcam ===
def atualizar_webcam():
    ret, frame = camera.read()
    if ret:
        frame = cv2.resize(frame, (largura_webcam, altura_webcam))
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        imgtk = ImageTk.PhotoImage(img)
        label_webcam.imgtk = imgtk
        label_webcam.configure(image=imgtk)
    label_webcam.after(10, atualizar_webcam)

# === FUNÇÃO: Tirar foto com a webcam ===
def tirar_foto(event=None):
    ret, frame = camera.read()
    if ret:
        cv2.imwrite("foto_capturada.jpg", frame)
        print("📸 Foto salva como 'foto_capturada.jpg'")
        resposta = identificar_peca()
        mudar_fundo(resposta)
    
    
# === FUNÇÃO: Fechar janela ===
def fechar_janela(event=None):
    camera.release()
    janela.destroy()

# Ligações de teclas
janela.bind("<space>", tirar_foto)
janela.bind("<Escape>", fechar_janela)

# Começa com uma imagem padrão
mudar_fundo("img1")  # Coloque o nome do arquivo de imagem inicial

# Inicia a câmera
atualizar_webcam()
janela.mainloop()



