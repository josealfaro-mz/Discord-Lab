# generador_cuestionario.py
# Este modulo es el que me permite recibir texto libre, como "hazme un
# cuestionario de listas" o "quiero un quiz de excepciones", y regresar un
# cuestionario ya armado. Todo esto es LOCAL: no llamo a ninguna API de
# internet ni de inteligencia artificial, solo uso expresiones regulares (re)
# para sacar el tema de la frase, y un diccionario con preguntas que yo
# mismo redacte para los temas que doy en el curso.

import re

# Banco de preguntas para los temas que si cubro a fondo en el curso.
# Cada tema (llave) tiene su propia lista de preguntas ya escritas.
BANCO_PREGUNTAS = {
    "palabras_reservadas": [
        "1. ¿Que es una palabra reservada en Python?",
        "2. Menciona 3 ejemplos de palabras reservadas.",
        "3. ¿Por que 'class' no se puede usar como nombre de variable?",
        "4. ¿Que pasa si intento usar 'for' como nombre de una variable?",
    ],
    "identificadores": [
        "1. ¿Que es un identificador en Python?",
        "2. ¿Con que caracteres puede empezar un identificador?",
        "3. ¿Por que '2edad' no es un identificador valido?",
        "4. Da un ejemplo de un identificador valido y uno invalido.",
    ],
    "tipos_datos": [
        "1. ¿Cual es la diferencia entre int y float?",
        "2. Da un ejemplo de un dato de tipo str.",
        "3. ¿Que valores puede tener un dato de tipo bool?",
        "4. Menciona un tipo de dato compuesto (que no sea simple).",
    ],
    "ciclo_for": [
        "1. ¿Para que sirve la funcion range() dentro de un for?",
        "2. ¿Que palabra clave se usa junto con for para recorrer algo?",
        "3. Escribe un ciclo for que cuente del 1 al 5.",
        "4. ¿Un for en Python necesita parentesis como en Java? ¿Por que si o no?",
    ],
    "ciclo_while": [
        "1. ¿Cual es la diferencia entre un for y un while?",
        "2. ¿Que pasa si la condicion de un while nunca se vuelve falsa?",
        "3. ¿Que caracter no se me debe olvidar al final de la linea del while?",
        "4. Escribe un while que cuente del 0 al 3.",
    ],
    "condicionales": [
        "1. ¿Que hace la instruccion if en Python?",
        "2. ¿Para que sirve elif?",
        "3. ¿Que pasa si me falta el ':' al final del if?",
        "4. Escribe un if que revise si un numero es mayor a 10.",
    ],
    "listas": [
        "1. ¿Como se agrega un elemento al final de una lista?",
        "2. ¿Como se elimina un elemento de una lista por su posicion?",
        "3. ¿Desde que numero empiezan a contar los indices de una lista?",
        "4. ¿Que hace la funcion enumerate() sobre una lista?",
    ],
    "excepciones": [
        "1. ¿Para que sirve un bloque try-except?",
        "2. ¿Que tipo de error lanza Python si intento convertir 'hola' a numero?",
        "3. ¿Que pasa con el programa si nunca atrapo una excepcion?",
        "4. Escribe un try-except que evite que truene una division entre cero.",
    ],
    "variables": [
        "1. ¿Cual es la diferencia entre una variable y una constante?",
        "2. ¿Como se escriben normalmente las constantes en Python?",
        "3. Da un ejemplo de una asignacion de variable.",
        "4. ¿Puedo cambiar el valor de una variable despues de crearla?",
    ],
}

# Aqui relaciono palabras que el usuario podria escribir con la llave del
# banco de preguntas de arriba. Uso "in" para que no tenga que escribir exacto
# (ej. si escribe "bucles" tambien lo cacho como ciclo for/while).
ALIAS_TEMAS = {
    "palabras_reservadas": ["reservada", "reservadas", "palabra reservada"],
    "identificadores": ["identificador", "identificadores"],
    "tipos_datos": ["tipo de dato", "tipos de dato", "tipo de datos", "tipos de datos"],
    "ciclo_for": ["ciclo for", "bucle for", " for "],
    "ciclo_while": ["ciclo while", "bucle while", " while "],
    "condicionales": ["condicional", "condicionales", " if "],
    "listas": ["lista", "listas"],
    "excepciones": ["excepcion", "excepciones", "try", "except"],
    "variables": ["variable", "variables", "constante", "constantes"],
}


def _buscar_tema(texto_original):
    """Intento sacar el tema del cuestionario de la frase libre que escribio
    el usuario. Busco lo que sigue despues de palabras como 'de', 'sobre'
    o 'acerca de', usando expresiones regulares."""
    texto = " " + texto_original.lower().strip() + " "  # espacios de sobra ayudan al alias " for "

    patrones = [
        r"cuestionario\s+(?:de|sobre|acerca de)\s+(.+)",
        r"quiz\s+(?:de|sobre|acerca de)\s+(.+)",
        r"examen\s+(?:de|sobre|acerca de)\s+(.+)",
        r"preguntas\s+(?:de|sobre|acerca de)\s+(.+)",
    ]

    for patron in patrones:
        coincidencia = re.search(patron, texto)
        if coincidencia:
            tema = coincidencia.group(1).strip()
            tema = tema.strip(" .,!?")  # le quito signos que se le peguen al final
            return tema

    return ""  # si no encontre ningun patron, regreso vacio


def _identificar_tema_conocido(tema_libre):
    """Reviso si el tema que pidio el usuario corresponde a alguno de los
    temas que ya tengo preparados en mi banco de preguntas."""
    tema_con_espacios = " " + tema_libre + " "
    for llave, alias in ALIAS_TEMAS.items():
        for palabra in alias:
            if palabra in tema_con_espacios:
                return llave
    return None


def generar_cuestionario(texto_original):
    """Funcion principal: recibe el mensaje completo (texto libre) y regresa
    el cuestionario ya armado, listo para mandarse al canal de Discord."""
    tema_libre = _buscar_tema(texto_original)

    # si no logre sacar ningun tema del texto, le pido que sea mas especifico
    if tema_libre == "":
        return ("Dime de que tema quieres el cuestionario. Ejemplo: "
                "'hazme un cuestionario de listas' o 'quiero un quiz de excepciones'.")

    llave_conocida = _identificar_tema_conocido(tema_libre)

    if llave_conocida is not None:
        # ya tengo preguntas armadas para este tema, las regreso tal cual
        preguntas = BANCO_PREGUNTAS[llave_conocida]
        encabezado = f"**Cuestionario de {tema_libre}**\n"
        return encabezado + "\n".join(preguntas)

    # si el tema no esta en mi banco (ej. pidio de otra materia), armo un
    # cuestionario generico usando plantillas con el mismo texto que escribio.
    encabezado = f"**Cuestionario de {tema_libre}** (tema libre)\n"
    preguntas_genericas = [
        f"1. ¿Que es {tema_libre}?",
        f"2. ¿Para que se usa o para que sirve {tema_libre}?",
        f"3. Da un ejemplo relacionado con {tema_libre}.",
        f"4. ¿Que problema comun existe al usar o entender {tema_libre}?",
        f"5. Explica con tus palabras por que {tema_libre} es importante.",
    ]
    return encabezado + "\n".join(preguntas_genericas)
