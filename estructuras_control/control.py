# control.py
# Tema 2: estructuras de control (ciclos y condicionales).
# La idea de estas funciones es que el usuario mande un pedacito de codigo
# y el agente lo revisa para decirle si lo escribio bien o que le falta. Uso el
# modulo re (expresiones regulares) para buscar las partes importantes.

import re


def evaluar_ciclo_for(argumento=""):
    codigo = argumento.strip()
    if codigo == "":
        return "Mandame tu ciclo for para revisarlo. Ejemplo: !for for i in range(5):"

    # un for bien hecho en Python lleva la palabra 'in', con este patron la busco.
    # \w+ es cualquier palabra (la variable) y \s+ son los espacios.
    patron = r"for\s+\w+\s+in\s+"

    if not re.search(patron, codigo):
        return ("Ojo: en Python el for se escribe 'for variable in ...'. "
                "No se usan parentesis ni punto y coma como en Java o C.")

    # acuerdo importante: para repetir un numero de veces se usa range()
    if "range(" not in codigo:
        return ("Tu for tiene buena estructura, pero para repetir N veces "
                "normalmente se usa range(). Ejemplo: for i in range(5):")

    return "Bien! Tu ciclo for tiene la estructura correcta de Python."


def evaluar_ciclo_while(argumento=""):
    codigo = argumento.strip()
    if codigo == "":
        return "Mandame tu ciclo while. Ejemplo: !while while x < 10:"

    if not codigo.startswith("while"):
        return "Un ciclo while empieza con la palabra 'while' y luego una condicion."

    # reviso que termine con dos puntos, que es lo que mas se nos olvida
    if not codigo.rstrip().endswith(":"):
        return "Casi! Te falto poner los dos puntos (:) al final de la condicion."

    return ("Bien! Solo no olvides que adentro del while algo tiene que cambiar, "
            "si no se queda en un ciclo infinito.")


def evaluar_condicional(argumento=""):
    codigo = argumento.strip()
    if codigo == "":
        return "Mandame tu condicional. Ejemplo: !condicional if edad >= 18:"

    # reviso que de menos use 'if'
    if "if" not in codigo:
        return "Un condicional siempre empieza con 'if' y una condicion."

    if not codigo.rstrip().endswith(":"):
        return "Te falto el ':' al final del if. Sin eso Python marca error."

    return "Bien! Tu condicional esta bien armado. Acuerdate de indentar lo de adentro."
