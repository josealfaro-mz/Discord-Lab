# sintaxis.py
# Aqui puse todo lo del Tema 1: la sintaxis basica de Python.
# Son las funciones que le explican al usuario las palabras reservadas,
# los identificadores y los tipos de datos. Casi todas nomas regresan un
# texto ya armado, menos validar_variable que si revisa lo que escribe el user.

import keyword  # este modulo ya trae la lista de palabras reservadas de Python


def mostrar_palabras_reservadas(argumento=""):
    # junto la lista que me da keyword en un solo texto, separada por comas
    lista = ", ".join(keyword.kwlist)
    respuesta = (
        "**Palabras reservadas en Python**\n"
        "Son palabras que el lenguaje ya tiene apartadas, asi que no las puedo\n"
        "usar como nombre de mis variables. Por ejemplo: if, for, while, def...\n\n"
        "Lista completa:\n" + lista
    )
    return respuesta


def mostrar_identificadores(argumento=""):
    # aqui nomas regreso la explicacion de las reglas, no ocupo nada del user
    respuesta = (
        "**Identificadores en Python**\n"
        "Un identificador es el nombre que le pongo a una variable, funcion o clase.\n"
        "Reglas que tengo que respetar:\n"
        "- Empiezan con letra o con guion bajo (_), nunca con numero.\n"
        "- No pueden llevar espacios ni acentos.\n"
        "- No pueden ser una palabra reservada.\n"
        "Ejemplos validos: nombre, edad_1, _total\n"
        "Ejemplos invalidos: 2edad, mi variable, class"
    )
    return respuesta


def mostrar_tipos_datos(argumento=""):
    respuesta = (
        "**Tipos de datos en Python**\n"
        "- int: numeros enteros. Ejemplo: 10\n"
        "- float: numeros con decimales. Ejemplo: 3.14\n"
        "- str: texto entre comillas. Ejemplo: 'Hola'\n"
        "- bool: verdadero o falso. Ejemplo: True / False\n"
        "Tambien existen los compuestos como las listas, tuplas y diccionarios."
    )
    return respuesta


def validar_variable(argumento=""):
    # esta funcion si usa lo que escribio el user (el nombre que quiere revisar)
    nombre = argumento.strip()

    # primero checo que si haya escrito algo
    if nombre == "":
        return "Escribe el nombre que quieres revisar. Ejemplo: !validar mi_edad"

    # voy revisando regla por regla. Si rompe alguna, le digo cual y me salgo.
    if nombre in keyword.kwlist:
        return f"'{nombre}' NO sirve porque es una palabra reservada de Python."

    if nombre[0].isdigit():
        return f"'{nombre}' NO sirve porque empieza con un numero."

    if " " in nombre:
        return f"'{nombre}' NO sirve porque tiene espacios."

    # isidentifier() ya me dice si el nombre cumple las reglas de Python.
    # lo uso al final para cachar acentos o simbolos raros.
    if not nombre.isidentifier():
        return f"'{nombre}' NO sirve, tiene algun caracter raro (acentos o simbolos)."

    # si paso todas las revisiones de arriba, entonces si es valido
    return f"'{nombre}' SI es un nombre de variable valido."
