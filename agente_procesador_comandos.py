"""
Checkpoint 03 - Agente Discord: Implementación Procesador Comandos
==================================================================
Este archivo implementa los comandos del bot utilizando el framework
`discord.ext.commands`. La lógica de cada comando NO vive aquí: se
delega al archivo base `practica02/procesador_comando.py`, separando
la capa de interfaz (Discord) de la capa de lógica (funciones).
"""

import os
import sys
import datetime

import discord
from discord.ext import commands
from dotenv import load_dotenv

# Permite importar los paquetes del proyecto sin importar desde donde
# se ejecute el script.
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Archivo base con la lógica de los comandos
from practica02.procesador_comando import (
    obtener_saludo,
    procesar_comando_recordar,
    calcular_uptime,
    mostrar_ayuda,
)

# --- CONFIGURACIÓN DEL BOT ---

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # Necesario para leer el contenido de los mensajes

# command_prefix="!" -> el framework detecta y enruta los comandos por nosotros.
# help_command=None  -> desactivamos el !help por defecto para usar nuestro !ayuda.
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

NOMBRE_BOT = "BotiUX"
hora_inicio = None  # Se asigna cuando el bot está listo


@bot.event
async def on_ready():
    global hora_inicio
    hora_inicio = datetime.datetime.now()
    print(f"Sincronizado como {bot.user} (ID: {bot.user.id})")
    print("------")


# --- IMPLEMENTACIÓN DE COMANDOS ---
# Cada comando llama a la función correspondiente del archivo base.

@bot.command(name="saludo")
async def saludo(ctx):
    """!saludo -> Muestra un saludo del bot."""
    respuesta = obtener_saludo(NOMBRE_BOT)
    await ctx.send(f"**Bot Procesador:** {respuesta}")


@bot.command(name="recordar")
async def recordar(ctx, *, nombre: str = None):
    """!recordar [nombre] -> El bot recordará el nombre proporcionado."""
    argumento = nombre.strip() if nombre else ""
    respuesta = procesar_comando_recordar(argumento)
    await ctx.send(f"**Bot Procesador:** {respuesta}")


@bot.command(name="uptime")
async def uptime(ctx):
    """!uptime -> Muestra el tiempo de actividad del bot."""
    if hora_inicio:
        respuesta = calcular_uptime(hora_inicio)
    else:
        respuesta = "El bot aún no ha registrado su hora de inicio."
    await ctx.send(f"**Bot Procesador:** {respuesta}")


@bot.command(name="ayuda")
async def ayuda(ctx):
    """!ayuda -> Lista los comandos disponibles."""
    respuesta = mostrar_ayuda()
    await ctx.send(f"**Bot Procesador:** {respuesta}")


@bot.command(name="salir")
async def salir(ctx):
    """!salir -> Finaliza el programa (solo para el dueño del bot)."""
    if await bot.is_owner(ctx.author):
        await ctx.send("**Bot Procesador:** ¡Hasta luego!")
        await bot.close()
    else:
        await ctx.send("**Bot Procesador:** No tienes permiso para usar este comando.")


# --- MANEJO DE ERRORES ---

@bot.event
async def on_command_error(ctx, error):
    """Si el comando no existe, notificamos al usuario."""
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(
            f"**Bot Procesador:** Comando no reconocido. Usa **!ayuda** para ver los comandos disponibles."
        )
    else:
        print(f"Error en comando '{ctx.message.content}': {error}")
        await ctx.send("**Bot Procesador:** Ocurrió un error al procesar el comando.")


# --- EJECUCIÓN DEL BOT ---

if __name__ == "__main__":
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("ERROR: No se encontró el TOKEN en el archivo .env")
