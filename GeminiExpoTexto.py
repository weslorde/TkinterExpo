import google.generativeai as genai

# Substitua pela sua chave da API
genai.configure(api_key="AIzaSyCqN2F-KV49jzUfdl1_kkzpJiPT3eUNVcI")

# Crie o modelo de texto
model = genai.GenerativeModel("gemini-2.0-flash")

# Faça uma pergunta ou pedido
response = model.generate_content("Explique como funciona a fotossíntese de forma simples.")

# Mostre a resposta
print(response.text)
