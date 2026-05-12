import datetime

# --- Funciones de Lógica de Datos ---

def agregar_tarea(lista_tareas, descripcion):
    """
    Agrega una tarea a la lista si cumple con los requisitos.
    Recibe la lista (paso por referencia) y la cadena de descripción.
    """
    if len(descripcion) < 3:
        return " Error: La descripción es muy corta (mínimo 3 caracteres)."
    
    # Creamos un formato de cadena simple para la tarea
    fecha = datetime.datetime.now().strftime("%H:%M")
    nueva_tarea = f"[{fecha}] {descripcion}"
    lista_tareas.append(nueva_tarea)
    return f" Tarea añadida con éxito."

def listar_tareas(lista_tareas):
    """
    Formatea la lista de tareas para su visualización.
    """
    if not lista_tareas:
        return " No hay tareas pendientes en la lista."
    
    resultado = " Listado de Tareas:\n"
    for i, tarea in enumerate(lista_tareas, start=1):
        resultado += f"  {i}. {tarea}\n"
    return resultado

def eliminar_tarea(lista_tareas, indice_str):
    """
    Elimina una tarea por su número de índice.
    Realiza validaciones de tipo de dato y rango.
    """
    if not indice_str.isdigit():
        return "Error: Debes ingresar el número de la tarea (ej: !borrar 1)."
    
    indice = int(indice_str) - 1
    
    if 0 <= indice < len(lista_tareas):
        tarea_eliminada = lista_tareas.pop(indice)
        return f"🗑️ Tarea eliminada: {tarea_eliminada}"
    else:
        return " Error: El número de tarea no existe en la lista."

# --- Función de Control Principal ---

def main():
    tareas = []  # Nuestra "base de datos" en memoria (lista)
    PREFIJO = "!"
    
    print("=== Bot de Gestión de Tareas (Modo Estructurado) ===")
    print("Comandos: !add [texto], !list, !del [numero], !exit\n")
    
    activa = True
    while activa:
        entrada = input(">> ").strip()
        
        if not entrada.startswith(PREFIJO):
            if entrada: print("Recuerda usar '!' para comandos.")
            continue
            
        # Procesamiento de la entrada
        cuerpo = entrada[len(PREFIJO):].split(maxsplit=1)
        comando = cuerpo[0].lower()
        argumento = cuerpo[1] if len(cuerpo) > 1 else ""
        
        # Selección de acción (Estructura de control)
        if comando == "exit":
            print("Saliendo del gestor...")
            activa = False
            
        elif comando == "add":
            print(agregar_tarea(tareas, argumento))
            
        elif comando == "list":
            print(listar_tareas(tareas))
            
        elif comando == "del":
            print(eliminar_tarea(tareas, argumento))
            
        else:
            print(f" Error: Comando '!{comando}' no reconocido.")
        
        print("-" * 20)

if __name__ == "__main__":
    main()