# importo todas las funciones de los otros modulos (uno por cada tema)
from sintaxis_basica.sintaxis import (
    mostrar_palabras_reservadas,
    mostrar_identificadores,
    mostrar_tipos_datos,
    validar_variable,
)
from estructuras_control.control import (
    evaluar_ciclo_for,
    evaluar_ciclo_while,
    evaluar_condicional,
)
from estructuras_datos.tareas import (
    agregar_tarea,
    listar_tareas,
    eliminar_tarea,
)
from manejo_excepciones.excepciones import (
    ejecutar_suma,
    ejecutar_multiplicacion,
)
from nucleo.generador_cuestionario import generar_cuestionario


"""
cada llave es una intencion, y guarda la funcion que se ejecuta
mas una descripcion corta de lo que hace.
"""

TOOLKIT = {
    "palabras_reservadas": {
        "funcion": mostrar_palabras_reservadas,
        "descripcion": "Muestra las palabras reservadas de Python.",
    },
    "identificadores": {
        "funcion": mostrar_identificadores,
        "descripcion": "Explica las reglas de los identificadores.",
    },
    "tipos_datos": {
        "funcion": mostrar_tipos_datos,
        "descripcion": "Muestra los tipos de datos de Python.",
    },
    "validar_variable": {
        "funcion": validar_variable,
        "descripcion": "Revisa si un nombre de variable es valido.",
    },
    "evaluar_ciclo_for": {
        "funcion": evaluar_ciclo_for,
        "descripcion": "Revisa un ciclo for.",
    },
    "evaluar_ciclo_while": {
        "funcion": evaluar_ciclo_while,
        "descripcion": "Revisa un ciclo while.",
    },
    "evaluar_condicional": {
        "funcion": evaluar_condicional,
        "descripcion": "Revisa un condicional if.",
    },
    "agregar_tarea": {
        "funcion": agregar_tarea,
        "descripcion": "Agrega una tarea a la lista.",
    },
    "listar_tareas": {
        "funcion": listar_tareas,
        "descripcion": "Muestra la lista de tareas.",
    },
    "eliminar_tarea": {
        "funcion": eliminar_tarea,
        "descripcion": "Borra una tarea por su numero.",
    },
    "ejecutar_suma": {
        "funcion": ejecutar_suma,
        "descripcion": "Suma dos numeros (con manejo de errores).",
    },
    "ejecutar_multiplicacion": {
        "funcion": ejecutar_multiplicacion,
        "descripcion": "Multiplica dos numeros (con manejo de errores).",
    },
    "generar_cuestionario": {
        "funcion": generar_cuestionario,
        "descripcion": "Arma un cuestionario de texto libre sobre el tema que pidas.",
    },
}
