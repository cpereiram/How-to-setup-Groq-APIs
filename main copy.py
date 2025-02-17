import os
import base64
from dotenv import load_dotenv
from groq import Groq

# Cargar variables de entorno
load_dotenv()
key = os.getenv('grok_key')

# Inicializar cliente
client = Groq(api_key=key)

# Estado del chat
chat_history = []

def encode_image(image_path):
    """Convierte una imagen a formato base64."""
    try:
        with open(image_path, 'rb') as image_file:
            byte_image = image_file.read()
            return base64.b64encode(byte_image).decode('utf-8')
    except FileNotFoundError:
        print("Error: No se encontró la imagen.")
        return None

def send_message(content):
    """Envía un mensaje al modelo y obtiene la respuesta."""
    global chat_history
    chat_history.append({"role": "user", "content": content})
    
    completion = client.chat.completions.create(
        model="llama-3.2-11b-vision-preview",
        messages=chat_history,
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )
    
    response = completion.choices[0].message
    chat_history.append(response)
    print("\n🤖 Respuesta:", response["content"], "\n")

def main():
    print("\n💬 Chat OCR con IA (Escribe 'adjuntar <imagen.jpg>', 'reset' o 'salir')\n")
    
    while True:
        user_input = input("👤 Tú: ")
        
        if user_input.lower() == "salir":
            print("👋 Saliendo del chat...")
            break
        
        elif user_input.lower() == "reset":
            global chat_history
            chat_history = []
            print("🔄 Chat reseteado.")
        
        elif user_input.startswith("adjuntar "):
            image_path = user_input.split(" ", 1)[1]
            encoded_image = encode_image(image_path)
            if encoded_image:
                send_message([
                    {"type": "text", "text": "Transcribe esta imagen en markdown:"},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}}
                ])
        
        else:
            send_message([{"type": "text", "text": user_input}])
            
if __name__ == "__main__":
    main()
