from estructura.array_estatico import ArrayEstatico
from estructura.lista_dinamica import ListaDinamica
from estructura.excepcion import Estalleno


def main():
    print("==================================================")
    print("    SIMULACIÓN: ARRAY ESTÁTICO VS LISTA DINÁMICA   ")
    print("==================================================")

    # ----------------------------------------------------
    # 1. Simulación y Prueba del Array Estático
    # ----------------------------------------------------
    print("\n[1] Probando el Array Estático (Capacidad máxima: 3)")

    # Creamos un array estático con capacidad de 3 elementos
    array = ArrayEstatico(3)
    datos_simulados = [10, 20, 30]

    for dato in datos_simulados:
        array.insertar(dato)
        print(f" -> Insertado exitosamente: {dato} | Estado: {array} | Tamaño actual: {len(array)}")

    print("\nIntentando sobrepasar el límite del Array Estático...")
    try:
        # Esto debería lanzar la excepción porque la capacidad es 3 y ya está lleno
        array.insertar(40)
    except Estalleno as e:
        print(f" [¡Alerta capturada con éxito!]: {e}")

    # ----------------------------------------------------
    # 2. Simulación y Prueba de la Lista Dinámica Enlazada
    # ----------------------------------------------------
    print("\n[2] Probando la Lista Dinámica Enlazada (Sin límite fijo)")

    # Creamos la lista dinámica
    lista = ListaDinamica()

    print(" -> Insertando al inicio: 100, luego 50")
    lista.insertar_al_inicio(100)
    lista.insertar_al_inicio(50)
    print(f"    Estado de la lista: {lista} | Tamaño: {len(lista)}")

    print(" -> Insertando al final: 200, luego 300")
    lista.insertar_al_final(200)
    lista.insertar_al_final(300)
    print(f"    Estado final de la lista: {lista} | Tamaño: {len(lista)}")

    print("\n==================================================")
    print("Simulación finalizada correctamente. ¡Listo para presentar!")
    print("==================================================")


if __name__ == "__main__":
    main()