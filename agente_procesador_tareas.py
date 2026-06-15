"""
Checkpoint 04 - Agente Discord: Implementación Procesador de Tareas
====================================================================
Este archivo implementa los comandos del bot utilizando el framework
`discord.ext.commands`. La lógica de cada comando NO vive aquí: se
delega al archivo base `practica04/tareas_agente.py`, separando así
la capa de interfaz (Discord) de la capa de lógica (funciones).
"""

import os
import sys

import discord
from discord.ext import commands
from dotenv import load_dotenv

# Permite importar los paquetes del proyecto sin importar desde donde
# se ejecute el script.
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Archivo base con la lógica de los comandos
from practica04.tareas_agente import (
    agregar_tarea,
    listar_tareas,
    eliminar_tarea,
)

# --- CONFIGURACIÓN DEL BOT ---

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # Necesario para leer el contenido de los mensajes

# command_prefix="!" -> el framework detecta y enruta los comandos por nosotros.
# help_command=None  -> desactivamos el !help por defecto para usar nuestro !ayuda.
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

# "Base de datos" en memoria: lista compartida entre todos los comandos
tareas = []


@bot.event
async def on_ready():
    print(f"Sincronizado como {bot.user} (ID: {bot.user.id})")
    print("------")


# --- IMPLEMENTACIÓN DE COMANDOS ---
# Cada comando llama a la función correspondiente del archivo base.

@bot.command(name="add")
async def add(ctx, *, descripcion: str = None):
    """!add [descripcion] -> Agrega una nueva tarea a la lista."""
    argumento = descripcion.strip() if descripcion else ""
    respuesta = agregar_tarea(tareas, argumento)
    await ctx.send(f"**Bot Tareas:** {respuesta}")


@bot.command(name="list")
async def list_tareas(ctx):
    """!list -> Muestra todas las tareas pendientes."""
    respuesta = listar_tareas(tareas)
    await ctx.send(f"**Bot Tareas:** {respuesta}")


@bot.command(name="del")
async def del_tarea(ctx, indice: str = None):
    """!del [numero] -> Elimina la tarea con el número indicado."""
    argumento = indice.strip() if indice else ""
    respuesta = eliminar_tarea(tareas, argumento)
    await ctx.send(f"**Bot Tareas:** {respuesta}")


@bot.command(name="ayuda")
async def ayuda(ctx):
    """!ayuda -> Muestra los comandos disponibles."""
    respuesta = (
        "**Comandos disponibles:**\n"
        "`!add [descripcion]` - Agrega una nueva tarea\n"
        "`!list` - Muestra todas las tareas pendientes\n"
        "`!del [numero]` - Elimina la tarea con el número indicado\n"
        "`!ayuda` - Muestra esta lista de comandos"
    )
    await ctx.send(f"**Bot Tareas:** {respuesta}")


# --- MANEJO DE ERRORES ---

@bot.event
async def on_command_error(ctx, error):
    """Si el comando no existe, notificamos al usuario."""
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(
            "**Bot Tareas:** Comando no reconocido. Usa **!ayuda** para ver los comandos disponibles."
        )
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            "**Bot Tareas:** Falta un argumento. Usa **!ayuda** para ver el uso correcto."
        )
    else:
        print(f"Error en comando '{ctx.message.content}': {error}")
        await ctx.send("**Bot Tareas:** Ocurrió un error al procesar el comando.")


# --- EJECUCIÓN DEL BOT ---

if __name__ == "__main__":
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("ERROR: No se encontró el TOKEN en el archivo .env")
