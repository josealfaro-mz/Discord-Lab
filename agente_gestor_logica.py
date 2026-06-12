"""
Checkpoint 02 - Agente Discord: Gestor de Logica
================================================
Este archivo implementa los comandos del bot utilizando el framework
`discord.ext.commands`. La logica NO vive aqui: cada comando delega
su trabajo al archivo base `practica03/agente_logica.py`, manteniendo
separada la capa de interfaz (Discord) de la capa de logica.
"""

import os
import sys

import discord
from discord.ext import commands
from dotenv import load_dotenv

# Permite importar los paquetes del proyecto sin importar desde donde
# se ejecute el script (mismo truco usado en practica05/inicio.py).
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Archivo base con la logica de los comandos
from practica03 import agente_logica
from practica03.agente_logica import (
    analizar_comando,
    buscar_en_diccionario,
    ejecutar_multiplicacion,
    ejecutar_suma,
    obtener_fecha_completa,
    validar_variable,
)

# --- CONFIGURACION DEL BOT ---

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # Necesario para leer el contenido de los mensajes

# command_prefix="!" -> el framework detecta y enruta los comandos por nosotros.
# help_command=None  -> desactivamos el !help por defecto para usar nuestro !ayuda.
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)


def registrar_en_historial(comando):
    """
    Registra el comando en el historial del archivo base (maximo 5),
    replicando la regla de `analizar_comando`. Asi, aunque llamemos a
    las funciones directamente, el comando `!historial` sigue funcionando.
    """
    if len(agente_logica.historial_comandos) >= 5:
        agente_logica.historial_comandos.pop(0)
    agente_logica.historial_comandos.append(comando)


@bot.event
async def on_ready():
    print(f"Sincronizado como {bot.user} (ID: {bot.user.id})")
    print("------")


# --- IMPLEMENTACION DE COMANDOS ---
# Cada comando llama a la funcion correspondiente del archivo base.

@bot.command(name="definir")
async def definir(ctx, *, termino: str = None):
    """!definir <termino> -> busca el concepto en el diccionario."""
    registrar_en_historial("!definir")
    argumento = termino.lower().strip() if termino else None
    respuesta = buscar_en_diccionario(argumento)
    await ctx.send(f"**Bot Logica:** {respuesta}")


@bot.command(name="validar")
async def validar(ctx, *, nombre: str = None):
    """!validar <nombre> -> revisa si el nombre de variable es valido."""
    registrar_en_historial("!validar")
    argumento = nombre.strip() if nombre else None
    respuesta = validar_variable(argumento)
    await ctx.send(f"**Bot Logica:** {respuesta}")


@bot.command(name="sumar")
async def sumar(ctx, *, numeros: str = None):
    """!sumar <n1> <n2> -> suma dos numeros."""
    registrar_en_historial("!sumar")
    respuesta = ejecutar_suma(numeros if numeros else "")
    await ctx.send(f"**Bot Logica:** {respuesta}")


@bot.command(name="multiplicar")
async def multiplicar(ctx, *, numeros: str = None):
    """!multiplicar <n1> <n2> -> multiplica dos numeros."""
    registrar_en_historial("!multiplicar")
    respuesta = ejecutar_multiplicacion(numeros if numeros else "")
    await ctx.send(f"**Bot Logica:** {respuesta}")


@bot.command(name="fecha")
async def fecha(ctx):
    """!fecha -> muestra la fecha y hora completa del servidor."""
    registrar_en_historial("!fecha")
    respuesta = obtener_fecha_completa()
    await ctx.send(f"**Bot Logica:** {respuesta}")


# Los siguientes comandos se delegan a `analizar_comando`, que ya
# registra el historial por si misma (por eso no llamamos al helper).

@bot.command(name="hora")
async def hora(ctx):
    """!hora -> muestra la hora actual del servidor."""
    respuesta = analizar_comando("!hora")
    await ctx.send(f"**Bot Logica:** {respuesta}")


@bot.command(name="historial")
async def historial(ctx):
    """!historial -> muestra los ultimos 5 comandos ejecutados."""
    respuesta = analizar_comando("!historial")
    await ctx.send(f"**Bot Logica:** {respuesta}")


@bot.command(name="ayuda")
async def ayuda(ctx):
    """!ayuda -> lista los comandos disponibles."""
    respuesta = analizar_comando("!ayuda")
    await ctx.send(f"**Bot Logica:** {respuesta}")


# --- MANEJO DE ERRORES ---

@bot.event
async def on_command_error(ctx, error):
    """Si el comando no existe, reutilizamos la respuesta del gestor base."""
    if isinstance(error, commands.CommandNotFound):
        respuesta = analizar_comando(ctx.message.content)
        await ctx.send(f"**Bot Logica:** {respuesta}")
    else:
        # Cualquier otro error se reporta en consola para depurarlo
        print(f"Error en comando '{ctx.message.content}': {error}")
        await ctx.send("**Bot Logica:** Ocurrio un error al procesar el comando.")


# --- EJECUCION DEL BOT ---

if __name__ == "__main__":
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("ERROR: No se encontro el TOKEN en el archivo .env")
