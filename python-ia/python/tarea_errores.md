# Actividad práctica: Robustecer `regulon_summary`

## Objetivo

Mejorar la robustez del programa `regulon_summary.py` incorporando manejo de errores en operaciones de entrada y salida, y extendiendo la validación del programa cuando sea necesario.

## Programa base

Archivo a trabajar:

`src/regulon_summary.py`

Repositorio:  
https://github.com/{user}/regulatory-network

Archivo directo:  
https://github.com/{user}/regulatory-network/blob/main/src/regulon_summary.py

---

## Contexto

El programa:

- lee un archivo de interacciones regulatorias,
- construye un regulón,
- permite filtrar con `--min_genes`,
- genera un archivo de salida.

Actualmente tiene validaciones básicas, pero aún puede fallar en distintos escenarios reales de uso.


### 1. Manejo de errores en lectura

Robustecer la lectura del archivo de entrada considerando:

- archivo inexistente (`FileNotFoundError`),
- falta de permisos (`PermissionError`),
- ruta inválida (`OSError`),
- errores al abrir o leer el archivo (`IOError`, `OSError`).

El programa debe:
- mostrar mensajes claros,
- terminar de forma controlada.

---

### 2. Manejo de errores en escritura

Robustecer la escritura del archivo de salida considerando:

- rutas inválidas (`OSError`),
- carpetas inexistentes (`FileNotFoundError` al escribir),
- falta de permisos (`PermissionError`),
- errores al escribir el archivo (`IOError`, `OSError`).

El programa debe:
- informar claramente el problema,
- evitar fallos abruptos.

---

### 3. Validaciones adicionales (pensamiento de desarrollador)

Además de lo anterior:

👉 **Debes identificar si existen otros posibles errores de ejecución o validaciones faltantes.**

Ejemplos (no limitativos):

- líneas mal formadas en el archivo (`ValueError`),
- número incorrecto de columnas (validación manual),
- valores inesperados en los campos (`ValueError`),
- `--min_genes` negativo o inválido (`ValueError`),
- argumentos incorrectos (`argparse.ArgumentTypeError`),
- archivo vacío (validación manual),
- tipos de datos incorrectos (`TypeError`).

#### Requisito

- Si detectas un caso que puede romper el programa o generar resultados incorrectos:
  - debes manejarlo (con validación o excepción),
  - o justificar por qué decides no hacerlo.

💡 Aquí no hay una única respuesta correcta — se evalúa tu criterio.


## Criterios de evaluación

Bajo este criterio se revisará lo que se implemente:

| Criterio | Descripción | Valor |
|----------|-------------|-------|
| Manejo de errores en lectura | Captura correctamente errores al leer archivos (FileNotFoundError, PermissionError, etc.) y muestra mensajes claros al usuario | 20% |
| Manejo de errores en escritura | Maneja errores al generar el archivo de salida (permisos, rutas, etc.) sin que el programa falle abruptamente | 20% |
| Validaciones adicionales | Identifica y maneja casos no evidentes (datos mal formados, argumentos inválidos, archivo vacío, etc.) | 20% |
| Calidad de las decisiones | Justifica (implícita o explícitamente) qué errores manejar y cuáles no; no usa try/except de forma indiscriminada | 15% |
| Casos de prueba | Ejecuta casos relevantes (correctos y de error) y demuestra que el programa responde adecuadamente | 15% |
| Claridad del reporte | El reporte de pruebas es claro, ordenado y fácil de entender | 10% |

---

## Nivel de desempeño (guía)

### Excelente (90–100)
- Maneja errores de forma precisa y controlada.
- Anticipa casos reales que no estaban explícitos.
- Los mensajes son claros y útiles.
- Se nota criterio de desarrollo (no solo seguir instrucciones).

### Bueno (80–89)
- Maneja los errores principales correctamente.
- Incluye algunas validaciones adicionales.
- Casos de prueba adecuados.

### Suficiente (70–79)
- Manejo básico de errores (principalmente lectura/escritura).
- Pocas validaciones adicionales.
- Pruebas limitadas.

### Insuficiente (<70)
- Manejo incompleto o incorrecto de errores.
- Uso incorrecto de excepciones (ej. `except:` sin criterio).
- Falta de pruebas o evidencia.

