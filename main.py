import time


def check_progress():
    print("--- 🚀 FULL STACK DEV TRACKER ---")

    tech_stack = ["Python 3.13", "Docker", "Git", "SQL", "Frontend (HTML/CSS)"]
    puntos = 0

    print(f"Analizando entorno de desarrollo...")
    time.sleep(1)

    for tech in tech_stack:
        respuesta = input(f"¿Has practicado '{tech}' hoy? (s/n): ").lower()
        if respuesta == 's':
            puntos += 20
            print(f"¡Buen trabajo! +20 XP en {tech}")
        else:
            print(f"No pasa nada, {tech} te espera mañana.")

    print("\n" + "=" * 30)
    print(f"TU NIVEL DE CARGA: {puntos}%")

    if puntos == 100:
        print("Nivel de rendimiento digno de una RTX 5070 Ti. ¡Estás volando!")
    elif puntos >= 60:
        print("Buen ritmo. Estás más cerca de ese perfil Full Stack.")
    else:
        print("Día tranquilo. Mañana se le da más duro al código.")
    print("=" * 30)


if __name__ == "__main__":
    check_progress()