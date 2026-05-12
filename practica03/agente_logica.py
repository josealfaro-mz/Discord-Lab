import datetime


# Variable global para almacenar el historial de la sesión
historial_comandos = []

def ejecutar_suma(argumento):
    """
    Procesa la suma de dos números recibidos como texto.
    Demuestra la Unidad 2.2.3 (Tipos de datos simples).
    """
    try:
        nums = argumento.split(" ")
        n1 = float(nums[0])
        n2 = float(nums[1])
        return f"La suma de {n1} + {n2} es: {n1 + n2}"
    except:
        return "Uso correcto: '!sumar 10 5'"

def buscar_en_diccionario(termino):
    if not termino: return " ¿Qué término buscas?"
    
    conocimiento = {
        "variable": "Espacio en memoria para datos.",
        "lista": "Arreglo dinámico de elementos.",
        "tupla": "Arreglo inmutable."
    }

    return conocimiento.get(termino, f" No encontré '{termino}'.")

def validar_variable(nombre):
    if not nombre: return "Indica el nombre."
    if nombre[0].isdigit(): return "No puede empezar con número."
    if not nombre.isidentifier(): return "Caracteres no permitidos."
    return f"{nombre} es válido."


def ejecutar_multiplicacion(argumento):
    """
    Procesa la multiplicación de dos números recibidos como texto.
    """
    try:
        nums = argumento.split(" ")
        n1 = float(nums[0])
        n2 = float(nums[1])
        return f"La multiplicación de {n1} x {n2} es: {n1 * n2}"
    except:
        return "Uso correcto: '!multiplicar 10 5'"

# --- FUNCIÓN EXTRA: Fecha y hora completa ---
def obtener_fecha_completa():
    """
    Devuelve la fecha y hora actual en formato completo.
    """
    ahora = datetime.datetime.now()
    return ahora.strftime("%A, %d de %B de %Y, %H:%M:%S")


def analizar_comando(entrada_usuario):
    mensaje = entrada_usuario.lower().strip()
    
    if mensaje.startswith("!"):
        partes = mensaje.split(" ", 1)
        comando = partes[0]
        argumento = partes[1] if len(partes) > 1 else None
        
        # Registrar en el historial (Máximo 5 elementos)
        if len(historial_comandos) >= 5:
            historial_comandos.pop(0)
        historial_comandos.append(comando)

        # --- UNIDAD 3: ESTRUCTURAS DE SELECCIÓN ---
        if comando == "!definir":
            return buscar_en_diccionario(argumento)
        
        elif comando == "!validar":
            return validar_variable(argumento)
            
        elif comando == "!hora":
            ahora = datetime.datetime.now().strftime("%H:%M:%S")
            return f" Hora actual: {ahora}"
        
        elif comando == "!historial":
            # UNIDAD 3.2: Estructuras de repetición
            res = "Últimos comandos:\n"
            for i, cmd in enumerate(historial_comandos, 1):
                res += f"{i}. {cmd}\n"
            return res

        elif comando == "!sumar":
            # UNIDAD 4.3: Parámetros de entrada
            return ejecutar_suma(argumento)
        
        elif comando == "!fecha":
            return obtener_fecha_completa()
        
        elif comando == "!multiplicar":
            return ejecutar_multiplicacion(argumento)
            
        elif comando == "!ayuda":
            return (" **Comandos V2:**\n"
                    "!definir, !validar, !hora, !historial, !sumar <n1> <n2>, !multiplicar <n1> <n2>, !fecha")
        
        else:
            return f"El comando '{comando}' no existe."
            
    return " Usa '!' para comandos."



if __name__ == "__main__":
    print("--- Agente de Lógica Estructurada V2 ---")
    while True:
        user_input = input("Alumno >> ")
        if user_input.lower() in ["salir", "exit"]: break
        print(f"Bot >> {analizar_comando(user_input)}\n")