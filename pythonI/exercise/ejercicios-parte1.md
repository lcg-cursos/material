
## **Objetivo de la Sesión Práctica**

Esta sesión práctica tiene como propósito ayudar al estudiante a reforzar sus conocimientos sobre **variables, listas, comprensión de listas, condicionales** y algunas funciones  y métodos como `print()`, `len()`, `.startwith()`, `input()`, `.count()`, etc.

Revisa cada ejercicio con atención, sigue las instrucciones y escribe el código en Python dentro del bloque correspondiente. Puedes ejecutar y probar tu código en **Visual Studio Code** o en cualquier otro entorno de desarrollo que prefieras.

⚠ **Importante:** Resuelve los ejercicios por tu cuenta. **No uses ChatGPT ni otras herramientas de asistencia automática** para generar las respuestas. El objetivo es que practiques y desarrolles tus habilidades de programación. 🚀


### **Ejercicio 1: Contar la longitud de una secuencia de ADN**

📌 _Objetivo:_ Uso de variables,  función `input` y  `len()`.

**Instrucciones:**

-   Pide al usuario que ingrese una secuencia de ADN.
-   Calcula e imprime su longitud.

```python

```

### **Ejercicio 2. Contar la frecuencia de cada nucleótido en una secuencia (5 min)**

📌 _Objetivo:_ Uso de variables y del método `count()` .

**Instrucciones:**

-   Pide al usuario que ingrese una secuencia de ADN.
-   Cuenta e imprime cuántas veces aparece cada nucleótido (`A, T, C, G`).


```python

```

### **Ejercicio 3: Identificar el codón de inicio en una secuencia de ADN (5 min)**

📌 _Objetivo:_ Uso de `if`,  `print()` y método `.startswith`.

**Instrucciones:**

-   Pide al usuario que ingrese una secuencia de ADN.
-   Verifica si la secuencia comienza con el codón de inicio `ATG`.

```python

```


###  **Ejercicio 4: Eliminar Adaptadores de secuencias**

📌 _Objetivo:_ Uso de `with`,  `open()` y  `for`.

**Instrucciones:**

- Lee el archivo de entrada `4_input_adapters.txt`
- Cortar adaptadores de la secuencia `4_input_adapters.txt`. Los adaptadores son los primeros 1-14 caracteres de cada secuencia.  
- Manda la salida a un archivo `4_input_no_adapters.txt`

`4_input_adapters.txt`
```
ATTCGATTATAAGCTCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATC
ATTCGATTATAAGCACTGATCGATCGATCGATCGATCGATGCTATCGTCGT
ATTCGATTATAAGCATCGATCACGATCTATCGTACGTATGCATATCGATATCGATCGTAGTC
ATTCGATTATAAGCACTATCGATGATCTAGCTACGATCGTAGCTGTA
ATTCGATTATAAGCACTAGCTAGTCTCGATGCATGATCAGCTTAGCTGATGATGCTATGCA
```

```python

```


### **Ejercicio 5: Convertir de tsv a fasta**

📌 _Objetivo:_ Uso de `with`,  `open()` y  `for`.

**Instrucciones:**
- Lee el archivo de entrada `dna_sequences.txt`
-  Convertir las secuencias en formato tsv `dna_sequences.txt`  a formato fasta.
- Guarda las secuencias en un archivo `dna_sequences.fa` 

`dna_sequences.txt`
```
seq_1   ATCGTACGATCGATCGATCGCTAGACGTATCG
seq_2   actgatcgacgatcgatcgatcacgact
seq_3   ACTGAC-ACTGT—ACTGTA----CATGTG
```

`dna_sequences.fa` 
```
> seq_1
ATCGTACGATCGATCGATCGCTAGACGTATCG
> seq_2
ACTGATCGACGATCGATCGATCACGACT
> seq_3
ACTGACACTGTACTGTACATGTG
```

```python

```

### **Ejercicio 6: Contar líneas en un archivo FASTA (10 min)**

📌 _Objetivo:_ Uso de `with`,  `open()` y  `len`, `startswith`, `list comprehension`

**Instrucciones:**

-   Lee el archivo `secuencias.fasta`
-  Cuenta cuántas secuencias hay en el archivo (líneas que comienzan con `>`)
- Imprime un mensaje que indique el numero de secuencias.

```
>Secuencia1
ATGCGTACGTAGCTAGCTAGC
>Secuencia2
CGTAGCTAGCTAGCTAGCTAGC
```

```python

```


### **Ejercicio 7: Extraer los primeros tres nucleótidos de cada secuencia (10 min)**

📌 _Objetivo:_ Uso de comprensión de listas para extraer subcadenas y `split`.

**Instrucciones:**

-   Pide al usuario que ingrese varias secuencias de ADN separadas por comas.
-   Extrae los primeros tres nucleótidos de cada secuencia.

```python

```


### **Ejercicio 8: Calcular el contenido de GC en una secuencia (10 min)**

📌 _Objetivo:_ Uso de listas, comprensión de listas, `len` e `in`.

**Instrucciones:**

-   Pide al usuario que ingrese una secuencia de ADN.
-   Calcula el porcentaje de nucleótidos `G` y `C` en la secuencia.


```python

```

### **Ejercicio 9: Transformar secuencias de ADN en ARN (10 min)**

📌 _Objetivo:_ Uso de comprensión de listas, `input`,  método `.replace()`.

**Instrucciones:**

-   Pide al usuario que ingrese varias secuencias de ADN separadas por comas.
-   Convierte cada secuencia a ARN reemplazando `T` por `U`.

```python

```

📌 **Extensión:** Guardar las secuencias convertidas en un archivo `secuencias_arn.txt`.


### **Ejercicio 10:  Filtrar muestras biológicas según su pH (20 min)**

📌 _Objetivo:_ Uso de comprensión de listas para filtrar valores numéricos.

**Instrucciones:**

-   Pide al usuario que ingrese valores de pH de distintas muestras separados por comas.
-   Filtra aquellas muestras que están dentro del rango fisiológico (pH entre 6.8 y 7.8).

**Código:**


```python

```


### **Ejercicio 11:  Invertir secuencias de ADN**

📌 _Objetivo:_ Uso de comprensión de listas para invertir cadenas.

**Instrucciones:**

-   Pide al usuario que ingrese varias secuencias de ADN separadas por comas.
-   Imprime las secuencias en orden inverso.


```python
```


### **Ejercicio 12:  Encontrar secuencias que contengan un codón de parada (10 min)**

📌 _Objetivo:_ Uso de listas y comprensión de listas para filtrar datos.

**Instrucciones:**

-   Pide al usuario que ingrese varias secuencias de ADN separadas por comas.
-   Filtra aquellas que contengan un codón de parada (`TAA`, `TAG`, `TGA`).

```python

```


### **Ejercicio 13: Contar nucleótidos en cada secuencia (15 min)**

📌 _Objetivo:_ Uso de listas anidadas y comprensión de listas.

**Instrucciones:**

-   Pide al usuario que ingrese varias secuencias de ADN separadas por comas.
-   Devuelve una lista con la cantidad de `A, T, C, G` en cada secuencia.

```python

```

📌 **Extensión:** Si queremos que tome en cuenta secuencias en minúsculas??


### **Ejercicio 14: Filtrar secuencias con alto contenido de GC (15 min)**

📌 _Objetivo:_ Uso de comprensión de listas para filtrar secuencias.

**Instrucciones:**

-   Pide al usuario que ingrese varias secuencias separadas por comas.
-   Calcula el porcentaje de GC de cada secuencia.
-   Filtra e imprime solo aquellas con un contenido de GC superior al 50%.

```python
```

📌 **Extensión:** Mostrar también el porcentaje de GC de cada secuencia.


### **Ejercicio 15: Saltar secuencias que no tengan el codón de inicio `ATG`**

📌 _Objetivo:_ Uso de `for`, `if`, `continue`, y listas.

**Instrucciones:**

- Recorre la lista de secuencias de ADN 
-  Imprime solo aquellas que contienen el codón de inicio `ATG`.

### **Ejercicio 16: Combinar genes y secuencias 

📌 _Objetivo:_ Uso de `for`, `zip()`, y listas.

**Instrucciones:**

- Dadas dos listas, una con nombres de genes y otra con sus secuencias correspondientes, 
- usa `zip()` para imprimir cada gen junto con su secuencia.

salida esperada

```
Gen: rpoB, Secuencia: ATGC
Gen: lacZ, Secuencia: CGTA
Gen: gyrA, Secuencia: TTGA
```

