import json
 
ARCHIVO = "notas.json"
 
def cargar_notas():
    try:
        with open(ARCHIVO) as f:
            return json.load(f)
    except FileNotFoundError:
        return []
 
def guardar_notas(notas):
    with open(ARCHIVO, "w") as f:
        json.dump(notas, f)
