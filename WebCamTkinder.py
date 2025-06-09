import cv2
import tkinter as tk
from PIL import Image, ImageTk

# Cria a janela principal do Tkinter
janela = tk.Tk()
janela.title("Webcam com Tkinter")

# Abre a webcam (0 = padrão)
camera = cv2.VideoCapture(0)

# Label para exibir a imagem da webcam
label_video = tk.Label(janela)
label_video.pack()

# Função que atualiza a imagem da webcam na interface
def atualizar_video():
    ret, frame = camera.read()
    if ret:
        # Converte o frame de BGR (OpenCV) para RGB (Tkinter)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        imgtk = ImageTk.PhotoImage(image=img)
        label_video.imgtk = imgtk
        label_video.configure(image=imgtk)
    # Chama a função novamente após 10ms
    label_video.after(10, atualizar_video)

# Função para capturar e salvar uma imagem
def tirar_foto():
    ret, frame = camera.read()
    if ret:
        cv2.imwrite("foto_tkinter.jpg", frame)
        print("Foto salva como 'foto_tkinter.jpg'")

# Botão para tirar a foto
botao_foto = tk.Button(janela, text="Tirar Foto", command=tirar_foto)
botao_foto.pack(pady=10)

# Inicia a atualização da imagem
atualizar_video()

# Fecha corretamente a câmera ao encerrar a janela
def ao_fechar():
    camera.release()
    janela.destroy()

janela.protocol("WM_DELETE_WINDOW", ao_fechar)
janela.mainloop()
