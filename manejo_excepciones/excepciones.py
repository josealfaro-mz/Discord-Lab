# Tema 4: manejo de excepciones con try-except.
# Estas funciones hacen operaciones con los numeros que escribe el usuario.
# Lo importante aqui es que si el usuario escribe algo que no es numero, el bot de discord
# NO se rompe: el try-except atrapa el error y le regreso un mensaje.


def ejecutar_suma(argumento=""):
    # espero que el usuario mande dos numeros, por ejemplo: "10 5"
    try:
        partes = argumento.split()      # separo el texto por espacios
        a = float(partes[0])            # float() truena si no es un numero
        b = float(partes[1])            # partes[1] truena si solo mando uno
        resultado = a + b
        return f"La suma de {a} + {b} = {resultado}"
    except (ValueError, IndexError):
        # ValueError = lo que mando no era numero
        # IndexError = falto uno de los dos numeros
        return "Para sumar mandame dos numeros. Ejemplo: !sumar 10 5"


def ejecutar_multiplicacion(argumento=""):
    # es casi igual a la suma pero multiplicando
    try:
        partes = argumento.split()
        a = float(partes[0])
        b = float(partes[1])
        resultado = a * b
        return f"La multiplicacion de {a} * {b} = {resultado}"
    except (ValueError, IndexError):
        return "Para multiplicar mandame dos numeros. Ejemplo: !multiplicar 4 2"
