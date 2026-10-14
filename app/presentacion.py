from app import logica
 
def pedir_nota():
    nombre = input("Nombre: ")
    nota = float(input("Nota (0-10): "))
    logica.registrar(nombre, nota)
 
def mostrar_resumen():
    prom = logica.promedio()
    print(f"Promedio del curso: {prom:.2f}")
