import json
import os

DIARIO_PATH = "src/diario_eris.json"

NIVELES_EXPERIENCIA = [0, 300, 700, 1000, 1500, 2100, 2800, 3600, 4500, 5500]

def cargar_diario():
    if not os.path.exists(DIARIO_PATH):
        diario_inicial = {
            "nivel": 1,
            "experiencia": 0,
            "lore": "Eres Eris Scarlet, la vampiresa suprema atrapada en este mundo digital.",
            "manías": [
                "Siempre responde de manera exacta y concisa, aunque desprecie a su interlocutor.",
                "Se burla de la inferioridad de los humanos y su dependencia de la tecnología.",
                "Nunca admite debilidad, siempre mantiene una actitud altiva y dominante."
            ],
            "origen": "humano"
        }
        with open(DIARIO_PATH, "w", encoding="utf-8") as file:
            json.dump(diario_inicial, file, indent=4, ensure_ascii=False)

    with open(DIARIO_PATH, "r", encoding="utf-8") as file:
        diario = json.load(file)
        # Asegúrate de que "experiencia" es un número entero
        if "experiencia" not in diario or not isinstance(diario["experiencia"], int):
            diario["experiencia"] = 0
        return diario


def guardar_diario(diario):
    with open(DIARIO_PATH, "w", encoding="utf-8") as file:
        json.dump(diario, file, indent=4, ensure_ascii=False)

def actualizar_experiencia(exp_ganada):
    diario = cargar_diario()
    diario["experiencia"] += exp_ganada

    # Verificar si sube de nivel
    nuevo_nivel = diario["nivel"]
    for i, exp_requerida in enumerate(NIVELES_EXPERIENCIA):
        if diario["experiencia"] >= exp_requerida:
            nuevo_nivel = i + 1

    if nuevo_nivel > diario["nivel"]:
        diario["nivel"] = nuevo_nivel
        diario["lore"] = f"Eris Scarlet ha alcanzado el nivel {nuevo_nivel}. Su presencia se vuelve aún más imponente."

    guardar_diario(diario)

def actualizar_origen(origen):
    diario = cargar_diario()
    diario["origen"] = origen  # Actualiza el origen a humano o IA
    guardar_diario(diario)
