# Investigación de Algoritmos de Búsqueda:
## Búsqueda Lineal y Búsqueda Binaria
### Criterios
### Investigación Teórica:
● Investiga cómo funcionan los algoritmos de búsqueda lineal y búsqueda binaria en el contexto de Python.
● Comprende los requisitos previos para aplicar cada algoritmo en Python.
### Análisis de Ejemplos:
● Buscar ejemplos de implementaciones de búsqueda lineal y búsqueda binaria
en Python.
● Analizar el código para entender cómo se lleva a cabo cada algoritmo y qué
principios subyacentes los guían en Python.
### Prueba y Evaluación:
● Probar las implementaciones con diferentes conjuntos de datos y valores en Python.
● Verifcar que los algoritmos devuelvan los resultados correctos para los valores
objetivos encontrados y manejen correctamente los casos en los que el valor
objetivo no está presente en la lista de Python.
### Comparación de Efciencia:
● Comparar la efciencia de los algoritmos de búsqueda lineal y búsqueda binaria
en Python en términos de tiempo de ejecución y recursos utilizados.
### Objetivo:
Investigar y comprender los algoritmos de búsqueda lineal y búsqueda binaria, y luego
implementar ambos algoritmos en python. Investigar cómo mostrar el tiempo de
ejecución de un script en Python, para comparar los tiempos de ejecución de cada
uno.
Una vez concluido el desarrollo, se debe subir el código a un repositorio y adjuntar el
link en el classroom para su posterior corrección.

***
# DESARROLLO:
***
### Búsqueda Lineal:
La búsqueda lineal es un algoritmo de búsqueda que recorre secuencialmente una lista
para encontrar un valor específco. La búsqueda lineal es el método más sencillo para
buscar un elemento en una lista, pero no es el más efciente. La búsqueda lineal es
adecuada para listas pequeñas o no ordenadas.
Pseudocódigo de la búsqueda lineal:
1. Comenzar desde el primer elemento de la lista.
2. Comparar cada elemento de la lista con el valor deseado.
3. Si el elemento actual es igual al valor deseado, devolver el índice del elemento.
4. Si el elemento actual no es igual al valor deseado, pasar al siguiente elemento.
5. Repetir los pasos 2-4 hasta que se encuentre el valor deseado o se recorra toda la lista.
Implementación de la búsqueda lineal en Python:
```py
def busqueda_lineal(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1
```
Este código define una función llamada busqueda_lineal que toma dos argumentos: una lista y un valor. La función recorre cada elemento de la lista (esto se hace con el bucle for i in range(len(lista))). Para cada elemento, compara si es igual al valor buscado (if lista[i] == valor). Si encuentra el valor, devuelve el índice en el que se encontró (return i). Si recorre toda la lista y no encuentra el valor, devuelve -1 (return -1).
### Búsqueda Binaria:
La búsqueda binaria es un algoritmo de búsqueda que divide repetidamente a la mitad
una lista ordenada para encontrar el valor deseado. La búsqueda binaria es un método
más efciente que la búsqueda lineal, pero requiere que la lista esté ordenada. La
búsqueda binaria es adecuada para listas grandes y ordenadas.
Pseudocódigo de la búsqueda binaria:
1. Comenzar con los índices de inicio y fin de la lista.
2. Calcular el índice medio de la lista.
3. Comparar el valor deseado con el elemento medio de la lista.
4. Si el valor deseado es igual al elemento medio, devolver el índice medio.
5. Si el valor deseado es menor que el elemento medio, buscar en la mitad izquierda de la lista.
6. Si el valor deseado es mayor que el elemento medio, buscar en la mitad derecha de la lista.
7. Repetir los pasos 2-6 hasta que se encuentre el valor deseado o los índices de inicio y fnal se crucen.
Implementación de la búsqueda binaria en Python:
```py
def busqueda_binaria(lista, valor):
    inicio = 0
    fnal = len(lista) - 1
    while inicio <= fnal:
        medio = (inicio + fnal) // 2
        if lista[medio] == valor:
            return medio
        elif lista[medio] < valor:
            inicio = medio + 1
        else:
            fnal = medio - 1
    return -1
```
Este código define una función llamada busqueda_binaria que toma dos argumentos: una lista y un valor. La función inicializa dos variables, inicio y final, para representar los extremos de la lista o sublista que se está examinando actualmente.
Luego entra en un bucle while que continúa mientras inicio sea menor o igual a final. Dentro del bucle, calcula el índice medio de la lista o sublista (medio = (inicio + final) // 2), y luego compara el valor en ese índice medio con el valor buscado.
Si el valor medio es igual al valor buscado (if lista[medio] == valor), entonces ha encontrado el valor y devuelve el índice medio. Si el valor medio es menor que el valor buscado (elif lista[medio] < valor), entonces sabe que el valor buscado, si está en la lista, está en la mitad derecha de la lista o sublista, por lo que ajusta inicio para que sea medio + 1. Si el valor medio es mayor que el valor buscado, entonces el valor buscado, si está en la lista, está en la mitad izquierda de la lista o sublista, por lo que ajusta final para que sea medio - 1.
Si el bucle termina sin encontrar el valor, la función devuelve -1 para indicar que el valor no se encontró en la lista.
***
### Comparación de Eficiencia:
La búsqueda binaria es más efciente que la búsqueda lineal en términos de tiempo de
ejecución y recursos utilizados. La búsqueda binaria tiene una complejidad de tiempo de
O(log n), mientras que la búsqueda lineal tiene una complejidad de tiempo de O(n).
La búsqueda binaria es adecuada para listas grandes y ordenadas, mientras que la
búsqueda lineal es adecuada para listas pequeñas o no ordenadas.
La búsqueda binaria es más rápida que la búsqueda lineal para listas grandes, ya que
divide repetidamente la lista por la mitad para encontrar el valor deseado. La búsqueda
lineal recorre secuencialmente la lista para encontrar el valor deseado, lo que puede ser
lento para listas grandes.
En general, la búsqueda binaria es más efciente que la búsqueda lineal para la mayoría
de los casos de uso, pero la búsqueda lineal puede ser más adecuada para listas pequeñas
o no ordenadas.
***
### Para mostrar tiempo de ejecución de un script en Python:
```py
import time
inicio = time.time()
# Código a medir
fnal = time.time()
print("Tiempo de ejecución:", fnal - inicio, "segundos")
```
***
### Ejemplo de uso:
```py
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valor = 5
print("Búsqueda Lineal:", busqueda_lineal(lista, valor))
print("Búsqueda Binaria:", busqueda_binaria(lista, valor))
```

### Referencias:
- Python Documentation: https://docs.python.org/3/
- GeeksforGeeks: https://www.geeksforgeeks.org/
- Real Python: https://realpython.com/
