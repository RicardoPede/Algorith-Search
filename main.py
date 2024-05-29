import time

def busqueda_lineal(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1

def busqueda_binaria(lista, valor):
    inicio = 0
    final = len(lista) - 1
    while inicio <= final:
        medio = (inicio + final) // 2
        if lista[medio] == valor:
            return medio
        elif lista[medio] < valor:
            inicio = medio + 1
        else:
            final = medio - 1
    return -1

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valor = 6

inicio = time.perf_counter()
print("Búsqueda Lineal:", busqueda_lineal(lista, valor))
final = time.perf_counter()
print("Tiempo de ejecución de la Búsqueda Lineal:", final - inicio, "segundos")

inicio = time.perf_counter()
print("Búsqueda Binaria:", busqueda_binaria(lista, valor))
final = time.perf_counter()
print("Tiempo de ejecución de la Búsqueda Binaria:", final - inicio, "segundos")