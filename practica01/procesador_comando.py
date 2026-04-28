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

def iniciar_agente():

def main():

if __name__ == "__main__":
    main()