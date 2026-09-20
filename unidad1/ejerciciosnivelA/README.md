<<<<<<< HEAD
# Estructuras de Datos - Unidad 1

Proyecto académico para comprender los fundamentos de las estructuras lineales y su implementación en Python utilizando programación orientada a objetos.

## Descripción general

Este proyecto desarrolla una estructura de datos tipo arreglo estático, aplicando conceptos clave de la materia como:

- Abstracción y diseño de interfaces mediante `ABC`
- Encapsulamiento de datos y validación de límites
- Manejo de errores personalizados
- Modularización del código en paquetes
- Pruebas unitarias automáticas

## Objetivo del proyecto

El objetivo principal es crear estructuras de datos eficientes y bien definidas, reforzando los conceptos de:

- capacidad fija
- control de tamaño actual
- prevención de sobrellenado
- uso de excepciones para errores de lógica
- separación de responsabilidades por módulos

## Características principales

### 1. Interfaz abstracta con ABC

La estructura base define un contrato común para todas las estructuras lineales. Esto permite garantizar que una clase concreta implemente métodos esenciales como:

- `insertar()`
- `esta_vacia()`
- `__len__()`

Esto se logra mediante la herencia de `ABC` y el uso de métodos abstractos.

### 2. Array estático con validación de límites

La clase `ArrayEstatico` almacena elementos en una lista interna de tamaño fijo. Su comportamiento incluye:

- capacidad definida al crear la instancia
- comprobación de espacio disponible antes de insertar
- control del tamaño actual del arreglo
- validación para evitar desbordamiento

### 3. Excepción personalizada

Cuando se intenta agregar un elemento cuando el arreglo ya está lleno, se lanza una excepción personalizada llamada `Estalleno`.

Esto evita errores silenciosos y permite manejar la condición de manera clara y profesional.

## Estructura del proyecto

```text
Unidad1_ADT/
├── main.py
├── README.md
├── Estructuras/
│   ├── __init__.py
│   ├── estructuras.py
│   ├── excepcion.py
│   ├── interfaces.py
│
├── tests/
│   ├── __init__.py
│   └── test_array.py
└── utils/
    ├── __init__.py
    └── visualizaciones.py
```

## Módulos principales

### `Estructuras/`

Contiene la lógica de la estructura de datos y la definición de la interfaz abstracta.

### `utils/`

Incluye funciones auxiliares para mostrar información o facilitar la visualización del estado de la estructura.

### `tests/`

Contiene las pruebas unitarias para validar el comportamiento correcto del arreglo estático.

### `main.py`

Es el punto de entrada del proyecto. Aquí se pueden crear instancias de la estructura, insertar datos y verificar su funcionamiento.

## ¿Qué aprendí con este proyecto?

Durante el desarrollo de esta unidad aprendí a:

- Diferenciar entre abstracción e implementación concreta.
- Diseñar interfaces con `ABC` para definir contratos claros.
- Implementar estructuras con límites predefinidos.
- Gestionar errores con excepciones personalizadas.
- Organizar un proyecto en módulos y paquetes.
- Realizar validaciones mediante pruebas unitarias con `unittest`.
- Comprender la importancia de mantener el código estructurado y reutilizable.

## Requisitos

- Python 3.x
- VS Code recomendado
- Terminal o consola del sistema

## Cómo ejecutar el proyecto

Abre una terminal en la carpeta raíz del proyecto y ejecuta:

### Ejecutar `main.py`

```bash
python main.py
```

O en Windows con `py`:

```bash
py main.py
```

### Ejecutar pruebas unitarias

```bash
python -m unittest discover -s tests -v
```

O con `py`:

```bash
py -m unittest discover -s tests -v
```

## Ejemplo de uso

```python
from Estructuras import ArrayEstatico

arr = ArrayEstatico(3)
arr.insertar("A")
arr.insertar("B")

print(len(arr))
print(arr)
```

## Resultado esperado

El programa permite crear un arreglo estático con tamaño limitado, insertar elementos válidos y detectar errores cuando se intenta exceder su capacidad.

## Conclusión

Este proyecto permite consolidar los conceptos fundamentales de estructuras de datos en Python, especialmente la definición de interfaces abstractas, manejo de límites y diseño modular de software.

---

Proyecto desarrollado como parte de la unidad de Estructuras de Datos.
=======
# 📚 INF-220 | Estructuras de Datos I | R1

> Repositorio personal de estudiante para la materia **Estructuras de Datos I (INF-220)**.

## 👨‍🎓 Información

* **Materia:** Estructuras de Datos I
* **Código:** INF-220
* **Lenguaje:** Python
* **Semestre:** cuarto semestre
* **Tipo de repositorio:** Académico / Estudiante

---

## 🎯 Descripción

Este repositorio contiene mis apuntes, ejemplos y ejercicios desarrollados durante las primeras unidades de la materia **Estructuras de Datos I**.

El objetivo es organizar de manera progresiva los conocimientos adquiridos sobre buenas prácticas de programación y diferentes formas de representar y organizar datos.

Actualmente, el repositorio contiene:

* **Unidad 0:** Estándares y buenas prácticas de codificación.
* **Unidad 1:** Modelos de representación de datos.

---

## 📂 Contenido del repositorio

| Unidad                      | Tema                               | Contenido                                                                           |
| ----------------------------| ---------------------------------- | ----------------------------------------------------------------------------------- |
| 📘 [Unidad 0](unidad0/)     | Estándares y buenas prácticas      | PEP 8, nombres, docstrings, type hints, clases abstractas y organización del código |
| 📗  [Unidad 1](unidad1/)    | Modelos de representación de datos | Datos abstractos, estáticos, dinámicos y simulados                                  |

---

## 🗂️ Estructura del proyecto

```text
INF220-EstructurasDatos1-Estudiante/
│
├── README.md
│
├── unidad0/
│   ├── README.md
│   └── ejercicios/
│
└── unidad1/
    ├── README.md
    └── ejercicios/
```

## 🐍 Requisitos

Para ejecutar los ejemplos se necesita:

* Python 3.8 o superior.
* Git.
* Un editor de código como Visual Studio Code.
* GoogleColab
---

## 👨‍💻 Autor

**Estudiante de INF-220**

Repositorio creado con fines académicos para organizar las prácticas y aprendizajes de la materia **Estructuras de Datos I**.

---

> 📚 *“La práctica constante permite comprender mejor las estructuras y los algoritmos.”*

>>>>>>> e3e38abad0a8b0c09bef14e15f6f96c9e984b02e
