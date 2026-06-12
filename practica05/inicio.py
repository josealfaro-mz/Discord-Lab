import discord
import os
import re
from dotenv import load_dotenv

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from practica01.gestor_comando import analizar_comando
from practica04.tareas_agente import agregar_tarea, listar_tareas, eliminar_tarea

# "Base de datos" en memoria: lista compartida de tareas.
# Es global para que persista entre los distintos mensajes del bot.
tareas = []


def mostrar_bienvenida():
    """Retorna la lista de comandos disponibles."""
    return (
        "📜 Bot de Gestión de Tareas (Modo Estructurado):\n"
        "📜 Comandos de tareas: !add <texto>, !list, !del <numero>\n"
        "📜 Comandos de lógica: !definir, !validar, !hora, !ayuda\n"
        "📜 Escriba !exit para salir del Agente"
    )


def main(entrada):
    PREFIJO = "!"

    if not entrada.startswith(PREFIJO):
        if entrada:
            return "Recuerda usar '!' para comandos."
        return ""

    # Procesamiento de la entrada
    cuerpo = entrada[len(PREFIJO):].split(maxsplit=1)
    if not cuerpo:
        return "Escribe un comando después de '!'."

    comando = cuerpo[0].lower()
    argumento = cuerpo[1] if len(cuerpo) > 1 else ""

    # Selección de acción (Estructura de control)
    if comando == "exit":
        return "Saliendo del gestor..."

    elif comando == "inicio":
        return mostrar_bienvenida()

    # --- Comandos de gestión de tareas (practica04) ---
    elif comando == "add":
        return agregar_tarea(tareas, argumento)

    elif comando == "list":
        return listar_tareas(tareas)

    elif comando == "del":
        return eliminar_tarea(tareas, argumento)

    # --- Comandos de lógica (practica01) ---
    elif comando in ["definir", "validar", "hora", "ayuda"]:
        return analizar_comando(entrada)

    else:
        return f"Error: Comando '!{comando}' no reconocido."


# --- CONFIGURACIÓN DE DISCORD ---

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Definir los "intents" (permisos) necesarios
intents = discord.Intents.default()
intents.message_content = True  # Necesario para leer el contenido de los mensajes

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Sincronizado como {client.user} (ID: {client.user.id})')
    print('------')


@client.event
async def on_message(message):
    # Evitar que el bot se responda a sí mismo
    if message.author == client.user:
        return

    print(f"Mensaje recibido de {message.author}: {message.content}")

    # Solo procesamos los mensajes que empiezan con el prefijo '!'
    if message.content.startswith('!'):
        resultado = main(message.content)
        print(f"Resultado del procesamiento: {resultado}")
        await message.channel.send(f"**Bot Procesador:** {resultado}")


# Ejecutar el bot
if __name__ == "__main__":
    if TOKEN:
        client.run(TOKEN)
    else:
        print("ERROR: No se encontró el TOKEN en el archivo .env")