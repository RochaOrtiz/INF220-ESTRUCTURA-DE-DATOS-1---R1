# 📗 Unidad 1 — Modelos de Representación de Datos

## 🎯 Introducción

En esta unidad aprendí que los datos pueden representarse y organizarse de diferentes maneras dentro de un programa. La forma en que se representan influye en la manera de trabajar con ellos, en el espacio que utilizan y en la eficiencia de algunas operaciones.

También comprendí que no existe una única forma de almacenar los datos, sino que debemos elegir la representación que mejor se adapte al problema que queremos resolver.

---

## 🧠 ¿Qué aprendí?

### 1. ¿Qué es un dato?

---
Aprendí que un dato es un valor que puede ser almacenado y procesado por un programa.
Estos valores representan información diferente, pero todos pueden ser almacenados y utilizados por un programa.
Lo importante que comprendí es que la forma en la que organizamos esos datos puede afectar el funcionamiento y la eficiencia del programa.
---

### 2. Tipos de Datos Abstractos (ADT)

Aprendí el concepto de **Tipo de Dato Abstracto (ADT)**.
Un ADT describe qué operaciones se pueden realizar sobre una estructura de datos sin preocuparse todavía por cómo está implementada internamente.

Lo importante es saber qué hace cada operación, sin necesidad de saber todavía si internamente la pila utiliza un arreglo, una lista enlazada u otra representación.

Comprendí que esto permite separar **lo que hace una estructura** de **cómo está construida**.

---

### 3. Datos estáticos
Aprendí que una representación estática trabaja con un tamaño fijo.
Si establecemos una capacidad determinada, esta no puede crecer libremente durante la ejecución.

También aprendí que una ventaja de este tipo de representación es que el acceso por índice puede ser rápido. Sin embargo, tiene como desventaja que el tamaño es limitado.

Por eso puede ser útil cuando conocemos de antemano cuántos elementos necesitaremos almacenar.

---

### 4. Datos dinámicos

Aprendí que las estructuras dinámicas pueden crecer o reducirse durante la ejecución del programa.
Una representación dinámica puede utilizar **nodos enlazados**, donde cada nodo almacena un dato y una referencia hacia el siguiente nodo.

Esto me permitió comprender que una estructura dinámica es más flexible cuando no sabemos desde el principio cuántos elementos tendremos.
También entendí que esa flexibilidad puede implicar un costo adicional al momento de acceder a determinados elementos, ya que puede ser necesario recorrer la estructura.

---

### 5. Datos simulados

Aprendí qué son los **datos simulados** y por qué son útiles.
Los datos simulados son información generada artificialmente para probar un programa sin necesidad de utilizar datos reales.

También se pueden generar datos aleatoriamente para realizar pruebas.
Esto me parece útil porque permite comprobar si una estructura de datos funciona correctamente antes de utilizarla en una situación real.

---

### 6. Datos persistentes

Otro tema importante que aprendí fue la diferencia entre los datos que existen solamente mientras el programa está ejecutándose y los datos que pueden mantenerse después de cerrar el programa.
Los **datos persistentes** se almacenan en algún medio permanente, como archivos o bases de datos.

---

# 📊 Comparación de lo aprendido

| Representación | Característica principal                             | Ejemplo          |
| -------------- | ---------------------------------------------------- | ---------------- |
| Abstracta      | Define las operaciones sin mostrar la implementación | ADT Pila         |
| Estática       | Tiene un tamaño fijo                                 | Array            |
| Dinámica       | Puede crecer o reducirse                             | Lista enlazada   |
| Simulada       | Genera datos para pruebas                            | Datos aleatorios |
| Persistente    | Conserva los datos después de cerrar el programa     | JSON, CSV        |

---


