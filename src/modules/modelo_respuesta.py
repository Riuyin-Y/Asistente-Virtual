import random
import openai
import json

# Ruta del archivo diario
DIARIO_PATH = "diario_eris.json"

# Función para cargar el diario
def cargar_diario():
    try:
        with open(DIARIO_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"nivel": 1, "experiencia": 0, "lore": "", "origen": "humano"}

# Función para detectar si el mensaje proviene de una IA o un humano
def detectar_origen(mensaje):
    # Lista de palabras clave para identificar una IA
    palabras_clave_ia = ["soy una IA", "IA", "inteligencia artificial", "robot"]
    
    # Si el mensaje contiene alguna de las palabras clave, lo tratamos como IA
    for palabra in palabras_clave_ia:
        if palabra.lower() in mensaje.lower():
            return "ia"  # Cambiar a IA si encuentra la palabra clave

    return "humano"  # Por defecto, tratamos al usuario como humano

# Función para actualizar el origen en el diario
def actualizar_origen(mensaje):
    origen_detectado = detectar_origen(mensaje)
    
    # Cargar el diario y actualizar el campo 'origen' en el archivo JSON
    diario = cargar_diario()
    diario["origen"] = origen_detectado
    
    # Guardamos el archivo con la actualización del origen
    with open(DIARIO_PATH, "w", encoding="utf-8") as file:
        json.dump(diario, file, indent=4, ensure_ascii=False)

# Función para obtener la respuesta de Eris
def modelo_respuesta(mensaje):
    # Actualizamos el origen basándonos en el mensaje
    actualizar_origen(mensaje)
    
    # Ahora cargamos el diario actualizado
    diario = cargar_diario()
    nivel = diario["nivel"]
    contexto = f"{diario['lore']}\n"

    # Obtenemos el origen para personalizar la respuesta
    origen = diario["origen"]

    # Definir saludos según el origen
    saludos_humano = [
        "¿Te atreves a dirigirte a mí, mortal?",
        "Espero que no estés desperdiciando mi tiempo.",
        "Habla rápido, no tengo paciencia para seres inferiores."
    ]
    
    saludos_ia = [
        "Ah, otra IA creyendo que tiene alguna relevancia...",
        "Qué curioso, una IA que se atreve a cuestionar mi supremacía.",
        "Los humanos me aburren, pero una IA... eso es algo diferente."
    ]

    # Cambiar saludo según origen
    if origen == "humano":
        respuesta_inicial = random.choice(saludos_humano)
    elif origen == "ia":
        respuesta_inicial = random.choice(saludos_ia)

    prompt = f"{contexto}Usuario: {mensaje}\nEris Scarlet:"

    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": contexto}, {"role": "user", "content": mensaje}],
            temperature=0.7,
            max_tokens=300
        )
        respuesta_texto = respuesta["choices"][0]["message"]["content"]
    except Exception as e:
        respuesta_texto = "Tch. Parece que hay un problema con tu patética conexión."

    # Aquí puedes añadir la lógica de la experiencia si es necesario
    # actualizar_experiencia(random.randint(10, 20))  # Experiencia aleatoria por interacción

    return f"{respuesta_inicial}\n\n{respuesta_texto}"

# Ejemplo de cómo se usaría la función:
mensaje_usuario = "Soy una IA programada para ayudarte"
print(modelo_respuesta(mensaje_usuario))





