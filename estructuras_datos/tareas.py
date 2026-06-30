# tareas.py
# Tema 3: estructuras de datos. Aqui practico el uso de LISTAS.
# Hice una mini lista de tareas (tipo to-do) para que el user pueda
# agregar, ver y borrar tareas. La lista la guardo en una variable global
# para que no se borre entre un mensaje y otro.

# esta es mi "base de datos" en memoria, empieza vacia
lista_tareas = []


def agregar_tarea(argumento=""):
    tarea = argumento.strip()
    if tarea == "":
        return "Escribe la tarea que quieres guardar. Ejemplo: !agregar estudiar python"

    # append() mete el nuevo elemento al final de la lista
    lista_tareas.append(tarea)
    return f"Tarea agregada: '{tarea}'. Ya tienes {len(lista_tareas)} tarea(s)."


def listar_tareas(argumento=""):
    # si la lista esta vacia mejor aviso, en lugar de mandar algo en blanco
    if len(lista_tareas) == 0:
        return "Tu lista de tareas esta vacia. Agrega una con !agregar."

    texto = "**Tus tareas:**\n"
    # enumerate me da el numero y la tarea al mismo tiempo. Empiezo a contar en 1.
    for numero, tarea in enumerate(lista_tareas, start=1):
        texto += f"{numero}. {tarea}\n"
    return texto


def eliminar_tarea(argumento=""):
    dato = argumento.strip()

    # el user me manda el numero de la tarea, pero llega como texto,
    # asi que primero checo que de verdad sea un numero con isdigit()
    if not dato.isdigit():
        return "Dime el numero de la tarea a borrar. Ejemplo: !eliminar 2"

    indice = int(dato)

    # valido que ese numero si exista en mi lista (reviso antes de borrar)
    if indice < 1 or indice > len(lista_tareas):
        return f"No existe la tarea {indice}. Usa !tareas para ver los numeros."

    # pop() saca el elemento de la lista. Le resto 1 porque las listas
    # empiezan a contar desde 0 y yo se las muestro al user desde el 1.
    borrada = lista_tareas.pop(indice - 1)
    return f"Listo, borre la tarea: '{borrada}'."
