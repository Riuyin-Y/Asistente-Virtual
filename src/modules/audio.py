import requests
import os
from config import ELEVENLABS_API_KEY, AUDIO_SAVE_PATH

ELEVENLABS_VOICE_ID = "tu_voz_id"  # Reemplazar con el ID de voz de ElevenLabs

def generar_audio(texto, nombre_archivo="respuesta.mp3"):
    """Convierte el texto en audio usando ElevenLabs y lo guarda."""
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE_ID}"
    
    headers = {
        "Content-Type": "application/json",
        "xi-api-key": ELEVENLABS_API_KEY
    }

    data = {
        "text": texto,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.5}
    }

    respuesta = requests.post(url, json=data, headers=headers)

    if respuesta.status_code == 200:
        ruta_audio = os.path.join(AUDIO_SAVE_PATH, nombre_archivo)
        with open(ruta_audio, "wb") as archivo:
            archivo.write(respuesta.content)
        return ruta_audio
    else:
        return None
