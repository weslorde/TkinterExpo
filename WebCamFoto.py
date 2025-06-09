import cv2

# Inicia a webcam (0 = padrão)
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Erro ao acessar a webcam.")
    exit()

print("Pressione ESPAÇO para tirar a foto, ou ESC para sair.")

while True:
    ret, frame = camera.read()
    if not ret:
        print("Erro ao capturar o vídeo.")
        break

    # Mostra a imagem ao vivo
    cv2.imshow("Webcam - Pressione ESPAÇO para capturar", frame)

    # Espera por tecla
    key = cv2.waitKey(1)

    if key == 27:  # ESC
        print("Saindo sem salvar.")
        break
    elif key == 32:  # ESPAÇO
        cv2.imwrite("foto_tirada.jpg", frame)
        print("Foto salva como 'foto_tirada.jpg'")
        break

# Libera os recursos
camera.release()
cv2.destroyAllWindows()
