# Proyecto de Estructuras de Datos - Nivel B

Este proyecto implementa dos estructuras lineales fundamentales para aprender el comportamiento y la complejidad de las estructuras de datos:

- Un array estático con control de capacidad.
- Una lista dinámica enlazada con inserción por inicio y final.

La base del diseño se apoya en una interfaz abstracta que define los métodos mínimos que debe cumplir cualquier estructura lineal.

## Descripción general

El objetivo de este proyecto es comparar dos formas distintas de almacenar datos y analizar cómo se comportan cuando se insertan, consultan o eliminan elementos.

### Estructuras implementadas

1. `Estructura` (interfaz abstracta)
   - Define la API común para estructuras lineales.
   - Exige métodos como `insertar`, `esta_vacia` y `__len__`.

2. `ArrayEstatico`
   - Tiene una capacidad fija definida al crear la instancia.
   - Guarda datos en una lista interna.
   - Si se intenta insertar más elementos de los permitidos, lanza la excepción `Estalleno`.

3. `ListaDinamica`
   - Se basa en nodos enlazados.
   - Permite insertar al inicio y al final.
   - No tiene una capacidad máxima fija, por lo que crece dinámicamente.

4. `main.py`
   - Es una simulación que demuestra el funcionamiento de ambas estructuras.
   - Muestra ejemplos de inserción y validación de límites.

5. Pruebas unitarias
   - Se encuentran en la carpeta `tests`.
   - Verifican que la creación, inserción y control de errores funcionen correctamente.

---

## Estructura de carpetas

```text
unidad1/
└── ejerciciosnivelB/
    ├── README.md
    ├── main.py
    ├── estructura/
    │   ├── __init__.py
    │   ├── array_estatico.py
    │   ├── lista_dinamica.py
    │   ├── interfaces.py
    │   ├── excepcion.py
    │   └── __init__.py
    └── tests/
        ├── __init__.py
        ├── test_array.py
        └── test_dinamico.py
```

---

## Supuestos de prueba de ambas estructuras

### 1. Array Estático (`ArrayEstatico`)

Se asume que:

- La capacidad se especifica al instanciar el objeto.
- El array empieza vacío.
- La inserción añade elementos en la siguiente posición libre.
- Si la cantidad de elementos alcanza la capacidad máxima, se lanza `Estalleno`.
- La longitud del array se obtiene con `len(array)`.

Ejemplos de prueba:

- Crear un array con capacidad 3.
- Insertar 3 elementos correctamente.
- Intentar insertar un cuarto elemento y verificar que se lance la excepción.
- Validar que `esta_vacia()` devuelva `False` cuando hay elementos.

### 2. Lista Dinámica (`ListaDinamica`)

Se asume que:

- La lista comienza vacía.
- `insertar_al_inicio` agrega un elemento en la cabeza.
- `insertar_al_final` agrega un elemento al final de la lista.
- `insertar` actúa como una operación general y, por defecto, añade al final.
- La estructura crece sin limitar su tamaño en memoria.

Ejemplos de prueba:

- Crear la lista vacía y verificar `len(lista) == 0`.
- Insertar varios elementos al inicio y comprobar el orden.
- Insertar varios elementos al final y comprobar el orden.
- Validar que la lista se pueda recorrer y representarse con `str(lista)`.

---

## Comparación de complejidades (Big O)

| Estructura | Inserción | Acceso | Eliminación | Observación |
|------------|-----------|--------|-------------|------------|
| `ArrayEstatico` | O(1) al final (si hay espacio) | O(1) por índice | O(n) en general | Tiene capacidad fija y puede provocar desbordamiento |
| `ListaDinamica` | O(1) al inicio; O(n) al final | O(n) | O(1) al inicio; O(n) al final | Crece dinámicamente y no exige capacidad previa |

### Interpretación

- En un array estático, el acceso por índice es muy rápido, pero la eliminación o inserción en posiciones intermedias exige desplazar elementos.
- En una lista enlazada, la inserción al inicio es constante, pero acceder a un elemento por posición requiere recorrer la lista desde el inicio.

---

## Requisitos y ejecución

### Ejecutar la simulación

Desde la carpeta del proyecto:

```bash
cd "ruta\al\proyecto\unidad1\ejerciciosnivelB"
python main.py
```

En Windows PowerShell, por ejemplo:

```powershell
cd "c:\Users\PERSONAL\Desktop\programas\visual stude code\EstructuraDatos\Unidad1_ADT\unidad1\ejerciciosnivelB"
python main.py
```

### Ejecutar pruebas unitarias

Desde la misma carpeta del proyecto:

```bash
python -m unittest discover -s tests -v
```

O con PowerShell:

```powershell
cd "c:\Users\PERSONAL\Desktop\programas\visual stude code\EstructuraDatos\Unidad1_ADT\unidad1\ejerciciosnivelB"
python -m unittest discover -s tests -v
```

---

## Conclusión

Este ejercicio permite comprender de forma práctica la diferencia entre una estructura de tamaño fijo y otra de tamaño dinámico. Mientras el array estático ofrece acceso directo y rápido, la lista dinámica ofrece mayor flexibilidad al no requerir una capacidad definida de antemano.

El proyecto sirve como base para estudiar conceptos fundamentales de estructuras de datos, manejo de excepciones y diseño orientado a objetos en Python.
