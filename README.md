# Algoritmos-de-Foil

## Descripción

Este proyecto implementa una versión básica del algoritmo **FOIL (First Order Inductive Learner)** utilizando Python.

El objetivo es inducir reglas que permitan identificar empleados que se encuentran en formación a partir de atributos como:

- Edad
- Departamento
- Nivel educativo
- Estado de formación

También se utiliza **FOIL Gain** para evaluar qué tan útil es una condición para separar ejemplos positivos de negativos.

---

## Dataset

El conjunto de datos utilizado contiene 8 empleados:

- 4 ejemplos positivos (`en_formacion = True`)
- 4 ejemplos negativos (`en_formacion = False`)

Los atributos utilizados son:

- `edad`
- `departamento`
- `nivel_educativo`
- `en_formacion`

---

## Ejercicio 1 - Inducción de reglas

Primero se separaron los ejemplos positivos y negativos.

Luego se compararon los valores de cada atributo para encontrar aquellos que aparecen en los positivos pero no en los negativos.

### Resultados

**Departamento:**

No existe un departamento exclusivo de los ejemplos positivos, ya que `IT` y `RRHH` también aparecen en ejemplos negativos.

**Nivel educativo:**

El nivel educativo que aparece únicamente en los positivos es:

`terciario`

**Edad:**

Las edades que aparecen únicamente en los positivos son:

`21, 22, 23 y 24`

A partir de estos datos se puede inducir la siguiente regla:

SI edad <= 24 ENTONCES en_formacion = True

Esta regla permite identificar todos los ejemplos positivos del dataset sin incluir ejemplos negativos.

---

## Ejercicio 2 - FOIL Gain

Se calculó el **FOIL Gain** para evaluar dos condiciones diferentes.

La fórmula utilizada fue:

FOIL Gain = p × [log2(p / (p + n)) - log2(P / (P + N))]

Donde:

- `P` = positivos antes de aplicar la condición
- `N` = negativos antes de aplicar la condición
- `p` = positivos después de aplicar la condición
- `n` = negativos después de aplicar la condición

---

### Condición 1: nivel_educativo == "terciario"

Valores obtenidos:

P = 4  
N = 4  
p = 3  
n = 0

Cálculos:

p / (p + n) = 3 / 3 = 1

P / (P + N) = 4 / 8 = 0.5

log2(1) = 0

log2(0.5) = -1

Por lo tanto:

FOIL Gain = 3 × [0 - (-1)]

FOIL Gain = 3.000

---

### Condición 2: edad <= 23

Valores obtenidos:

P = 4  
N = 4  
p = 3  
n = 0

Cálculos:

p / (p + n) = 3 / 3 = 1

P / (P + N) = 4 / 8 = 0.5

log2(1) = 0

log2(0.5) = -1

Por lo tanto:

FOIL Gain = 3 × [0 - (-1)]

FOIL Gain = 3.000

---

## Comparación de las condiciones

Aunque las condiciones son diferentes:

- `nivel_educativo == "terciario"`
- `edad <= 23`

ambas obtienen un **FOIL Gain de 3.000**.

Esto ocurre porque las dos condiciones seleccionan exactamente:

- 3 ejemplos positivos
- 0 ejemplos negativos

Por lo tanto, para este conjunto de datos ambas condiciones tienen la misma capacidad para separar los ejemplos seleccionados.

---

## Conclusión

El ejercicio permitió aplicar los conceptos básicos del algoritmo FOIL para inducir reglas a partir de ejemplos positivos y negativos.

Además, mediante el cálculo de **FOIL Gain**, se pudo medir la utilidad de distintas condiciones para mejorar la clasificación.

La regla general obtenida en el primer ejercicio fue:

SI edad <= 24 ENTONCES en_formacion = True

Mientras que las condiciones analizadas mediante FOIL Gain obtuvieron:

- `nivel_educativo == "terciario"` → FOIL Gain = 3.000
- `edad <= 23` → FOIL Gain = 3.000

## Tecnologías utilizadas

- Python
- Librería `math`
- Algoritmo FOIL
- FOIL Gain
