import os
from dotenv import load_dotenv      # para leer mi token desde el archivo .env
import discord

from nucleo.clasificador import clasificar_intencion
from nucleo.toolkit import TOOLKIT


def procesar_mensaje(texto_usuario):
    # PASO 1: limpio el mensaje que llego (le quito espacios de sobra)
    texto_limpio = texto_usuario.strip()

    # separo el comando del argumento. split(" ", 1) parte solo en el primer
    # espacio, asi el argumento se queda completo aunque tenga varios espacios.
    partes = texto_limpio.split(" ", 1)
    if len(partes) > 1:
        argumento = partes[1]   # lo que va despues del comando
    else:
        argumento = ""          # si solo escribio el comando, no hay argumento

    # PASO 2: el nucleo decide que quiere el usuario
    intencion = clasificar_intencion(texto_limpio)

    # caso especial: si pidio ayuda, le muestro el menu
    if intencion == "menu":
        return mostrar_menu()

    # PASO 3: busco la intencion en mi caja de herramientas (TOOLKIT)
    if intencion in TOOLKIT:
        herramienta = TOOLKIT[intencion]["funcion"]
        # PASO 4: ejecuto la funcion y le paso el argumento que escribio el user
        resultado = herramienta(argumento)
        return resultado

    # si no reconoci el comando, le aviso y le sugiero el menu
    return "No reconoci ese comando. Escribe !ayuda para ver lo que puedo hacer."


def mostrar_menu():
    # este texto es la lista de comandos que el bot sabe hacer
    menu = (
        "**Soy tu bot tutor de Python**\n"
        "Estos son mis comandos:\n"
        "palabras - palabras reservadas\n"
        "identificadores - reglas de los nombres\n"
        "tipos - tipos de datos\n"
        "validar <nombre> - reviso si un nombre de variable sirve\n"
        "for <codigo> - reviso un ciclo for\n"
        "while <codigo> - reviso un ciclo while\n"
        "condicional <codigo> - reviso un if\n"
        "agregar <tarea> - guardo una tarea\n"
        "tareas - veo mis tareas\n"
        "eliminar <numero> - borro una tarea\n"
        "sumar <a> <b> - sumo dos numeros\n"
        "multiplicar <a> <b> - multiplico dos numeros"
    )
    return menu


# ---------- De aqui para abajo es la conexion con Discord ----------

load_dotenv()                          # carga lo que tengo en el archivo .env
TOKEN = os.getenv("DISCORD_TOKEN")     # saco mi token secreto del .env

# los intents son los permisos del bot. Necesito message_content para poder
# leer lo que la gente escribe en el canal.
intents = discord.Intents.default()
intents.message_content = True

cliente = discord.Client(intents=intents)


@cliente.event
async def on_ready():
    # esto se ejecuta una sola vez, cuando el bot ya se conecto
    print(f"El bot ya esta listo. Se conecto como {cliente.user}")


@cliente.event
async def on_message(mensaje):
    # si el mensaje lo mando el mismo bot, lo ignoro (si no, se contesta solo)
    if mensaje.author == cliente.user:
        return

    # solo respondo si el mensaje empieza con "!", asi no contesta a todo
    
    if mensaje.content == "hola":
        await mensaje.channel.send("Hola! Soy tu bot tutor de Python. Escribe menu para ver lo que puedo hacer.")
        return
    elif mensaje.content == "menu":
        await mensaje.channel.send(mostrar_menu())
    else:
        respuesta = procesar_mensaje(mensaje.content)   # Pasos 1 al 4
        await mensaje.channel.send(respuesta)           # PASO 5: le contesto


# por ultimo enciendo el bot con mi token
if __name__ == "__main__":
    if TOKEN is None:
        print("ERROR: no encontre el DISCORD_TOKEN. Revisa tu archivo .env")
    else:
        cliente.run(TOKEN)
