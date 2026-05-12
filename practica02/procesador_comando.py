import datetime

def obtener_saludo(nombre_bot):
    """
    Retornar un saludo formateado
    """
    return f"Hola, soy {nombre_bot} y estoy listo para ayudarte."

def procesar_comando_recordar(comando):
    """
     Valida y procesa la accion de recordar un dato
    """
    if not comando:
        return "Error: falta el nombre. Uso !recordar [nombre]"
    
    return f"¡Enrendido! Recordare el nombre: {comando}"

def calcular_uptime(hora_inicio):
    """
     Calcula la diferencia de tiempo entre el inicio
     y el actual (mostrar actividad del boo)
    """
    ahora = datetime.datetime.now()
    diferencia = ahora - hora_inicio
    segundos = int(diferencia.total_seconds())
    return f"Tiempo de actividad: {segundos} segundos"

def mostrar_ayuda():
    """
    Comando disponibles para el usurio
    """
    return (
        "Comandos disponibles:\n"
        "!saludo - Muestra un saludo del bot\n"
        "!recordar [nombre] - El bot recordará el nombre proporcionado\n"
        "!uptime - Muestra el tiempo de actividad del bot\n"
        "!ayuda - Muestra esta lista de comandos\n"
        "!salir - Finaliza el programa"
    )
# funcion principal para probar las funciones
def iniciar_agente():
    NOMBRE_BOT = "BotiUX"
    PREFIJO ="!"
    hora_inicio = datetime.datetime.now()

    print(f"{obtener_saludo(NOMBRE_BOT)}")
    print("Escribe !ayuda para ver los comandos disponibles.")

    ejecutando = True
    while ejecutando:
        entrada = input(f"[{NOMBRE_BOT}] Ingrese comando: ").strip()

        if not entrada.startswith(PREFIJO):
            print("Comando no reconocido.")
            continue

        partes = entrada[len(PREFIJO):].split(maxsplit=1)
        comando = partes[0].lower()
        argumento = partes[1] if len(partes) > 1 else ""

        if comando == "saludo":
            print(obtener_saludo(NOMBRE_BOT))
        elif comando == "ayuda":
            print(mostrar_ayuda())
        elif comando == "salir":
            cerrar_proceso = input("¿Desea salir? (s/n): ").strip().lower()
            if cerrar_proceso == "s":
                ejecutando = False
                print("¡Hasta luego!")
        elif comando == "recordar" :
            print(procesar_comando_recordar(argumento))
        elif comando == "uptime":
            print(calcular_uptime(hora_inicio))
        else:
            print("Comando no reconocido.")


def main():
    iniciar_agente()

if __name__ == "__main__":
    main()