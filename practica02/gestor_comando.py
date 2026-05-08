import datetime
"""
Segunda fase del Agente: Procesamiento de comandos y logica dinamica.
Aqui el alumno aprende a separar la 'accion' de los 'datos'.
"""
mensaje = entrada_usuario.lower().strip()

#Simulacion de comandos prefijados (como se usan en Discord: !ayuda, !ejemplo)
if mensaje.startswith("!"):
    partes = mensaje.split(" ", 1)
    comando = partes[0]
    argumento = partes[1] if len(partes) > 1 else None

    # Logica de Comandos
    if comando == "!definir":
        return buscar_en_diccionario(argumento)
    
    elif comando == "!validar":
        return validar_formato(argumento)
    
    elif comando == "!hora":
        ahora = datetime.datetime.now().strftime("%H:%M:%S")
        return f"La hora actual es: {ahora}"
    
    elif comando == "!ayuda":
        return ("**Comandos disponibles:**\n"
                "1. '!definir <termino' -)