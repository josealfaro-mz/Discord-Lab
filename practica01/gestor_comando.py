import datetime
"""
Segunda fase del Agente: Procesamiento de comandos y logica dinamica.
Aqui el alumno aprende a separar la 'accion' de los 'datos'.
"""
def analizar_comando(entrada_usuario):
    """
    Segunda fase del Agente: Procesamiento de comandos y lógica dinámica.    
    """
    mensaje = entrada_usuario.lower().strip()
    
    # Simulación de comandos prefijados (como se usan en Discord: !ayuda, !ejemplo)
    if mensaje.startswith("!"):
        partes = mensaje.split(" ", 1)
        comando = partes[0]
        argumento = partes[1] if len(partes) > 1 else None
        
        # Lógica de Comandos
        if comando == "!definir":
            return buscar_en_diccionario(argumento)
        
        elif comando == "!validar":
            return validar_variable(argumento)
            
        elif comando == "!hora":
            ahora = datetime.datetime.now().strftime("%H:%M:%S")
            return f" La hora actual del servidor es: {ahora}"
            
        elif comando == "!ayuda":
            return (" Comandos disponibles:\n"
                    "1. '!definir <termino>' - Busca conceptos de Python.\n"
                    "2. '!validar <nombre>' - Revisa si un nombre de variable es válido.\n"
                    "3. '!hora' - Muestra la hora del sistema.")
        
        else:
            return f" El comando '{comando}' no existe. Usa '!ayuda'."
            
    return " Recuerda usar el prefijo '!' para darme órdenes, o pregunta algo directamente."

def buscar_en_diccionario(termino):
    if not termino:
        return "Debes escribir qué término quieres definir. Ej: '!definir list'"
    
    # Base de datos simplificada (puedes reutilizar la de la práctica anterior)
    conocimiento = {
        "variable": "Un espacio en memoria para almacenar datos.",
        "lista": "Colección mutable de elementos.",
        "tupla": "Colección inmutable de elementos (no se puede cambiar)."
    }
    return conocimiento.get(termino, f" No encontré '{termino}' en mi base de datos.")

def validar_variable(nombre):
    """
    Lógica pedagógica: Enseña a los alumnos las reglas de nombrado en Python.
    """
    if not nombre:
        return " Indica el nombre a validar. Ej: `!validar mi_variable`"
    
    # Reglas básicas de Python
    if nombre[0].isdigit():
        return f" '{nombre}' no es válido: ¡No puede empezar con un número!"
    if " " in nombre:
        return f" '{nombre}' no es válido: No puede contener espacios."
    if not nombre.isidentifier():
        return f" '{nombre}' contiene caracteres no permitidos (solo letras, números y _)."
        
    return f" '{nombre}' es un nombre de variable válido en Python."

# --- Simulación de ejecución ---
if __name__ == "__main__":
    print("--- Agente de Lógica: Fase de Comandos ---")
    print("Prueba comandos como: !validar 123hola o !definir lista\n")
    
    while True:
        user_input = input("Alumno >> ")
        if user_input.lower() in ["salir", "exit"]: break
        
        respuesta = analizar_comando(user_input)
        print(f"Bot >> {respuesta}\n")