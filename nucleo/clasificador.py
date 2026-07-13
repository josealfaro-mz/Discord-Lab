import re
import unicodedata


def _normalizar(texto):
    texto = unicodedata.normalize("NFD", texto)
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


def _palabras(texto):
    return re.findall(r"[a-z]+", texto)


def _hay_raiz(palabras, raiz):
    for palabra in palabras:
        if palabra.startswith(raiz):
            return True
    return False


def clasificar_intencion(texto):
    texto = _normalizar(texto.strip().lower())
    palabras = _palabras(texto)

    print(f"clasificar_intencion: texto = {texto}")

    if _hay_raiz(palabras, "cuestionari") or _hay_raiz(palabras, "quiz") or _hay_raiz(palabras, "examen") or _hay_raiz(palabras, "pregunt"):
        return "generar_cuestionario"

    if _hay_raiz(palabras, "reservad"):
        return "palabras_reservadas"

    if _hay_raiz(palabras, "identific"):
        return "identificadores"

    if _hay_raiz(palabras, "tipo") and _hay_raiz(palabras, "dato"):
        return "tipos_datos"

    tiene_tarea = _hay_raiz(palabras, "tarea")
    tiene_agregar = _hay_raiz(palabras, "agreg") or _hay_raiz(palabras, "anad") or _hay_raiz(palabras, "guarda")
    tiene_eliminar = _hay_raiz(palabras, "elimin") or _hay_raiz(palabras, "borr") or _hay_raiz(palabras, "quita")

    if tiene_tarea and not tiene_agregar and not tiene_eliminar:
        return "listar_tareas"

    if _hay_raiz(palabras, "ayud") or _hay_raiz(palabras, "menu") or _hay_raiz(palabras, "comand"):
        return "menu"

    comando = texto.split(" ")[0].replace("!", "")

    if comando.startswith("palabra") or comando.startswith("reservad"):
        return "palabras_reservadas"
    elif comando.startswith("identific"):
        return "identificadores"
    elif comando.startswith("tipo") or comando.startswith("dato"):
        return "tipos_datos"
    elif comando.startswith("valid") or comando.startswith("variable"):
        return "validar_variable"
    elif comando.startswith("for"):
        return "evaluar_ciclo_for"
    elif comando.startswith("while"):
        return "evaluar_ciclo_while"
    elif comando.startswith("condicional") or comando == "if":
        return "evaluar_condicional"
    elif comando.startswith("agreg") or comando.startswith("anad") or comando.startswith("guarda"):
        return "agregar_tarea"
    elif comando.startswith("tarea") or comando.startswith("list"):
        return "listar_tareas"
    elif comando.startswith("elimin") or comando.startswith("borr") or comando.startswith("quita"):
        return "eliminar_tarea"
    elif comando.startswith("sum"):
        return "ejecutar_suma"
    elif comando.startswith("multiplic"):
        return "ejecutar_multiplicacion"
    else:
        return "desconocida"
