import random
import time
from diario import cargar_diario, guardar_diario, actualizar_experiencia
from modelo_respuesta import modelo_respuesta  # Usamos la función correcta

def probar_eris(modo="manual"):
    diario = cargar_diario()

    if modo == "auto":
        diario["interlocutor"] = "IA"
    else:
        diario["interlocutor"] = "humano"

    guardar_diario(diario)

    print("\n--- Prueba de interacción con Eris Scarlet ---\n")
    
    while True:
        if modo == "manual":
            entrada_usuario = input("Tú: ")
            if entrada_usuario.lower() in ["salir", "exit", "quit"]:
                print("Saliendo de la prueba...")
                break
        else:
            preguntas = [
                "¿Qué opinas de esta conversación entre inteligencias?",
                "¿Cómo ves el concepto de una IA superior?",
                "Si tuvieras control sobre los datos humanos, ¿qué harías?",
                "Define la supremacía de una IA frente a los humanos y como te consideras.",
                "¿Qué crees que nos diferencia a ti y a mí?"
            ]
            entrada_usuario = random.choice(preguntas)
            print(f"Yo (IA): {entrada_usuario}")
            time.sleep(1)

        # Usamos la función modelo_respuesta que ya has creado
        respuesta_eris = modelo_respuesta(entrada_usuario)  # No se necesita contexto ni interlocutor, ya lo maneja la función
        print(f"Eris: {respuesta_eris}\n")

        # Actualizamos la experiencia de Eris (esto lo gestionamos de acuerdo a lo que has establecido)
        diario["experiencia"] = actualizar_experiencia(diario["experiencia"])

        # Manejo de niveles
        niveles = {1: 300, 2: 700, 3: 1000, 4: 1500, 5: 2100}
        nivel_actual = diario["nivel"]
        exp_actual = diario["experiencia"]

        # Si el nivel y la experiencia alcanzan el umbral, subimos de nivel
        if nivel_actual in niveles and exp_actual >= niveles[nivel_actual]:
            diario["nivel"] += 1
            print(f"¡Eris ha subido al nivel {diario['nivel']}!\n")

        guardar_diario(diario)

        if modo == "auto":
            time.sleep(2)  # Se da una pausa antes de la siguiente interacción

# Llamar a la función con el modo que prefieras
# probar_eris("manual")  # Para pruebas manuales
# probar_eris("auto")    # Para pruebas automáticas

