"""
Checkpoint 01 - Agente Discord: Gestor de Comandos
==================================================
Este archivo implementa los comandos del bot utilizando el framework
`discord.ext.commands`. La logica de cada comando NO vive aqui: se
delega al archivo base `practica01/gestor_comando.py`, separando asi
la capa de interfaz (Discord) de la capa de logica (funciones).
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
from practica01.gestor_comando import (
    analizar_comando,
    buscar_en_diccionario,
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


@bot.event
async def on_ready():
    print(f"Sincronizado como {bot.user} (ID: {bot.user.id})")
    print("------")


# --- IMPLEMENTACION DE COMANDOS ---
# Cada comando llama a la funcion correspondiente del archivo base.

@bot.command(name="definir")
async def definir(ctx, *, termino: str = None):
    """!definir <termino> -> busca el concepto en el diccionario de Python."""
    argumento = termino.lower().strip() if termino else None
    respuesta = buscar_en_diccionario(argumento)
    await ctx.send(f"**Bot Gestor:** {respuesta}")


@bot.command(name="validar")
async def validar(ctx, *, nombre: str = None):
    """!validar <nombre> -> revisa si el nombre de variable es valido."""
    argumento = nombre.strip() if nombre else None
    respuesta = validar_variable(argumento)
    await ctx.send(f"**Bot Gestor:** {respuesta}")


@bot.command(name="hora")
async def hora(ctx):
    """!hora -> muestra la hora actual del servidor."""
    respuesta = analizar_comando("!hora")
    await ctx.send(f"**Bot Gestor:** {respuesta}")


@bot.command(name="ayuda")
async def ayuda(ctx):
    """!ayuda -> lista los comandos disponibles."""
    respuesta = analizar_comando("!ayuda")
    await ctx.send(f"**Bot Gestor:** {respuesta}")


# --- MANEJO DE ERRORES ---

@bot.event
async def on_command_error(ctx, error):
    """Si el comando no existe, reutilizamos la respuesta del gestor base."""
    if isinstance(error, commands.CommandNotFound):
        respuesta = analizar_comando(ctx.message.content)
        await ctx.send(f"**Bot Gestor:** {respuesta}")
    else:
        # Cualquier otro error se reporta en consola para depurarlo
        print(f"Error en comando '{ctx.message.content}': {error}")
        await ctx.send("**Bot Gestor:** Ocurrio un error al procesar el comando.")


# --- EJECUCION DEL BOT ---

if __name__ == "__main__":
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("ERROR: No se encontro el TOKEN en el archivo .env")
