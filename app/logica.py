from app import datos
 
def registrar(nombre, nota):
    if not 0 <= nota <= 10:
        raise ValueError("Nota fuera de 0-10")
    notas = datos.cargar_notas()
    notas.append({"nombre": nombre,
                  "nota": nota})
    datos.guardar_notas(notas)
 
def promedio():
    notas = datos.cargar_notas()
    if not notas:
        return 0
    total = sum(n["nota"] for n in notas)
    return total / len(notas)
