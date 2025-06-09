import google.generativeai as genai
import PIL.Image

# Configure sua API key
genai.configure(api_key="AIzaSyCqN2F-KV49jzUfdl1_kkzpJiPT3eUNVcI")

# Carregue a imagem com PIL (ou qualquer biblioteca compatível)
image = PIL.Image.open("C:/Users/WesPC/Desktop/TkinterExpo/foto_tkinter.jpg")

# Use o modelo multimodal
model = genai.GenerativeModel("gemini-2.0-flash")

# Gere resposta com imagem + prompt
response = model.generate_content(
    [ 
        image,
        "Qual a peça de computador/notebook/celular dessa imagem? Preciso da resposta somente com o nome da peça e nada mais."
    ]
)

print(response.text)
