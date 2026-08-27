# 📘 Unidad 0 — Estándares y Buenas Prácticas de Codificación

## 🎯 Introducción

En esta unidad aprendí que programar no consiste solamente en hacer que un código funcione, sino también en escribirlo de una manera ordenada, clara y fácil de entender.

Aprendí diferentes reglas y buenas prácticas de Python que me ayudarán a mejorar la calidad de mis programas y a mantener un código más organizado.

---

## 🧠 ¿Qué aprendí?

### 1. PEP 8 y convenciones de nombres

Aprendí que **PEP 8** es una guía de estilo para escribir código Python de una manera más ordenada y fácil de leer.

También aprendí que dependiendo del elemento que estamos creando se utilizan diferentes formas de nombrarlo:

* Las variables y funciones utilizan `snake_case`.
* Las clases utilizan `PascalCase`.
* Las constantes utilizan `UPPER_SNAKE_CASE`.
* Los atributos privados pueden comenzar con `_`.
---

### 2. Formato e indentación

Aprendí que la forma en que escribimos el código también es importante.

En Python se recomienda utilizar **4 espacios para la indentación** y mantener una estructura ordenada. También aprendí a utilizar espacios correctamente alrededor de los operadores y a evitar líneas demasiado largas.

---

### 3. Docstrings

Aprendí qué son los **docstrings** y para qué sirven.

Los docstrings permiten explicar qué hace un módulo, una clase o una función. Esto es útil porque otra persona puede entender nuestro código sin tener que analizar cada línea.

---

### 4. Type Hints

También aprendí a utilizar **type hints**, que permiten indicar qué tipo de dato recibe una función y qué tipo de dato devuelve.
Esto me ayuda a entender mejor qué datos espera una función y qué resultado puedo esperar de ella.

---

### 5. Clases abstractas e interfaces

Aprendí que en Python podemos utilizar el módulo `abc` para crear **clases abstractas**.
Una clase abstracta puede definir métodos que las clases que hereden de ella deberán implementar.

Comprendí que esto permite establecer una especie de estructura o contrato que deben seguir otras clases.
Esto será importante posteriormente porque en Estructuras de Datos vamos a trabajar con diferentes estructuras como listas, pilas y colas.

---

### 6. Manejo de errores

Aprendí que no siempre es recomendable mostrar un mensaje de error utilizando solamente `print()`.
Python permite utilizar **excepciones** para controlar situaciones que pueden provocar errores durante la ejecución del programa.

También aprendí que podemos crear nuestras propias excepciones cuando sea necesario.
Esto permite que los programas sean más seguros y que los errores puedan ser identificados y tratados correctamente.

---

### 7. Organización de un proyecto

Otra cosa importante que aprendí es que un proyecto no debería tener todos sus archivos mezclados.
Es mejor organizarlo utilizando carpetas y archivos según la función que cumplen.

Por ejemplo:

```text
mi_proyecto/
├── README.md
├── estructuras/
├── tests/
├── utils/
└── main.py
```
Esto facilita encontrar los archivos y trabajar en proyectos más grandes.

---

### 8. `if __name__ == "__main__"`

Aprendí para qué sirve:

```python
if __name__ == "__main__":
    main()
```

Esta estructura permite indicar qué código debe ejecutarse cuando un archivo Python se ejecuta directamente.

Entendí que esto ayuda a organizar mejor los programas y permite que un archivo pueda utilizarse también como módulo sin ejecutar automáticamente la parte principal.

---

# 💡 Lo más importante que aprendí

Lo más importante que aprendí en esta unidad es que **un buen programador no solamente debe preocuparse por obtener un resultado correcto, sino también por la calidad y organización de su código**.

Antes podía pensar que mientras el programa funcionara era suficiente. Ahora entiendo que utilizar nombres claros, documentar las funciones, mantener una buena estructura, controlar los errores y seguir estándares como PEP 8 hace que el código sea mucho más fácil de entender, modificar y mantener.

---

# 🛠️ ¿Cómo puedo aplicar lo aprendido?

A partir de esta unidad, intentaré aplicar estas buenas prácticas en los siguientes ejercicios de la materia:

* Utilizar nombres descriptivos para variables y funciones.
* Mantener una correcta indentación.
* Utilizar `snake_case` y `PascalCase` según corresponda.
* Agregar docstrings a mis funciones y clases.
* Utilizar type hints cuando sea necesario.
* Manejar correctamente los posibles errores.
* Organizar los archivos de mis proyectos.
* Utilizar `if __name__ == "__main__"` en los programas principales.
* Escribir código pensando no solamente en que funcione, sino también en que otra persona pueda entenderlo.

---
