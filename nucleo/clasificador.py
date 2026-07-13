"""
Este es el "cerebro" que decide que quiere el user (Paso 2 del diagrama).
Recibe el texto que se escribe y viendo la primera palabra (el comando),
regresa el nombre de la intencion. Asi el agente sabe que herramienta usar.
"""


def clasificar_intencion(texto):
    texto = texto.strip().lower()

    # NUEVO: si el mensaje trae texto libre pidiendo un cuestionario/quiz/examen
    # (no necesariamente al inicio del mensaje, ej. "hazme un cuestionario de listas"),
    # lo mando directo a esa intencion antes de revisar el comando de la primera palabra.
    palabras_cuestionario = ["cuestionario", "quiz", "examen", "preguntas de", "preguntas sobre"]
    for palabra in palabras_cuestionario:
        if palabra in texto:
            return "generar_cuestionario"

    # me quedo solo con la primera palabra, que es el comando (ej: "!validar")
    comando = texto.split(" ")[0]

    # le quito el "!" del inicio por si lo trae, para comparar mas facil
    comando = comando.replace("!", "")

    print(f"clasificar_intencion: comando = {comando}")

    """
    aqui relaciono lo que escribe el usuario con el nombre de la intencion.
    pongo varias palabras parecidas para que no tenga que escribir exacto.
    """
    if comando in ["palabras", "reservadas"]:
        return "palabras_reservadas"
    elif comando in ["identificadores", "identificador"]:
        return "identificadores"
    elif comando in ["tipos", "datos"]:
        return "tipos_datos"
    elif comando in ["validar", "variable"]:
        return "validar_variable"
    elif comando in ["for"]:
        return "evaluar_ciclo_for"
    elif comando in ["while"]:
        return "evaluar_ciclo_while"
    elif comando in ["condicional", "if"]:
        return "evaluar_condicional"
    elif comando in ["agregar", "tarea"]:
        return "agregar_tarea"
    elif comando in ["tareas", "listar"]:
        return "listar_tareas"
    elif comando in ["eliminar", "borrar"]:
        return "eliminar_tarea"
    elif comando in ["sumar", "suma"]:
        return "ejecutar_suma"
    elif comando in ["multiplicar", "multiplicacion"]:
        return "ejecutar_multiplicacion"
    elif comando in ["ayuda", "menu", "comandos"]:
        return "menu"
    else:
        # si no se reconoce el comando, regresa "desconocida"
        return "desconocida"
