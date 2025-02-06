# Instalación de la Infraestructura del Curso


## Instalación y Configuración de Git y GitHub.

#### Requisitos.

1. **Crea una cuenta en el sitio web de [GitHub](https://github.com/signup?source=login)**. Se recomienda que utilices tu cuenta @ccg.unam.mx para obtener beneficios adicionales por ser estudiante.  
2. Contar con computadora personal.
3. Verifica que en tu computadora personal se encuentre instalado el sistema de control de versiones "git". Para ello, abre una terminal/consola o línea de comandos (cmd) en Windows y ejecuta el comando:

```
git version
```

Debes de obtener un resultado como el siguiente (puede variar la versión):

```
$ git version 
git version 2.19.0 

```

En caso de que no obtengas ningún resultado, descarga e instala git en tu computadora personal. Consulta los siguientes tutoriales para instalarlo de acuerdo al sistema operativo que tengas

- **Windows**: [https://www.youtube.com/watch?v=jdXKwLNUfmg]()
- **Ubuntu**: [https://www.youtube.com/watch?v=4M8cL-lXANQ]()
- **MacOS**: [https://www.youtube.com/watch?v=5EXAugHfhuk]()

Realiza los pasos del TUTORIAL **SOLO HASTA** la instalación de git. No crees ningún directorio ni configures nada adicional.

----

## Instalación de Visual Studio Code

Sigue estos pasos para instalar Visual Studio Code en tu sistema operativo.

### Paso 1: Descarga el instalador

- Visita la página oficial de Visual Studio Code: [Visual Studio Code](https://code.visualstudio.com/)
- Selecciona y descarga el instalador adecuado para tu sistema operativo (Windows, macOS o Linux).

### Paso 2: Instalación

#### Windows

1. Ejecuta el archivo descargado (ej., `VSCodeUserSetup-x64-<version>.exe`).
2. Sigue las instrucciones del asistente de instalación.
3. Opcionalmente, selecciona opciones como crear un ícono en el escritorio.
4. Una vez instalado, abre Visual Studio Code desde el menú de inicio o el ícono en el escritorio.

#### macOS

1. Abre el archivo `.zip` descargado y arrastra Visual Studio Code a la carpeta Aplicaciones.
2. Ejecuta VS Code desde la carpeta Aplicaciones.
3. Opcionalmente, añádelo al dock si lo usarás frecuentemente.

#### Linux

- **Usando Snap:**

```bash
  sudo snap install --classic code
```

#### Usando paquetes .deb o .rpm:

Para Debian/Ubuntu:

```bash
sudo dpkg -i <file>.deb
sudo apt-get install -f
```

Para Fedora/Red Hat:

```bash
sudo dnf install <file>.rpm
```

### Paso 3: Ejecución de Visual Studio Code
Abre Visual Studio Code desde el lanzador de aplicaciones de tu sistema operativo.

### Paso 4: Instalar extensiones
Visual Studio Code permite la instalación de extensiones para añadir funcionalidades, lenguajes de programación y temas.
Accede al Marketplace de extensiones desde el ícono de extensiones en la barra lateral izquierda y busca las extensiones que necesites (En clase te indicaremos algunas).




## Instalación y Configuración de Python Usando Entornos Virtuales

La instalación y adecuada configuración de Python es un paso fundamental para asegurar un inicio exitoso en tu viaje de programación. Para maximizar el entorno de trabajo, utilizaremos entornos virtuales, los cuales te permitirán crear y gestionar espacios de desarrollo aislados en tu computadora. Estos entornos son esenciales para mantener organizados los proyectos, ya que permiten instalar paquetes y bibliotecas específicos sin interferir con otros proyectos o con la instalación global de Python. En esta sección, te guiaremos a través de los pasos necesarios para instalar Python, crear un entorno virtual, y configurarlo para un trabajo sin interrupciones, asegurando que todos los estudiantes tengan una base sólida y consistente desde la cual partir.


### Entornos virtuales

Un entorno virtual en Python es una herramienta esencial que permite crear un espacio aislado para un proyecto de Python, donde puedes instalar librerías y dependencias específicas sin interferir con otros proyectos ni con el sistema Python global. Aquí tienes una explicación sencilla, seguida de algunos detalles adicionales:

### Explicación Sencilla

Piensa en un entorno virtual como en una "burbuja" para tu proyecto de Python. Dentro de esta burbuja, puedes instalar cualquier librería o versión específica de una librería que tu proyecto necesite, sin preocuparte por conflictos con otras librerías instaladas en tu sistema. Esto es especialmente útil cuando trabajas en múltiples proyectos que pueden requerir diferentes versiones de una misma librería.

### Detalles Adicionales

1. **Aislamiento de Dependencias:** 
   - Cada entorno virtual tiene su propio directorio para almacenar librerías específicas de Python.
   - Cuando activas un entorno virtual, cualquier librería instalada se guarda dentro de ese entorno, no afectando al sistema Python principal ni a otros entornos.

2. **Facilidad de Gestión:** 
   - Puedes tener múltiples entornos virtuales en una misma máquina, cada uno adaptado para diferentes proyectos, lo que facilita el manejo de proyectos con diferentes requisitos.
   - Esto ayuda a evitar el problema de las "dependencias en conflicto", donde dos proyectos requieren versiones diferentes de la misma librería.

3. **Compatibilidad y Control:**
   - Mantener las versiones exactas de las librerías controladas garantiza que el software probado bajo ciertas condiciones funcione de manera esperada en otros entornos o cuando se comparten proyectos con otros desarrolladores.

4. **Creación y Activación de Entornos Virtuales:**
   - **Verificar la Instalación de Python:** Asegúrate de que tanto Python como `pip` estén instalados en tu sistema. Puedes verificarlo ejecutando los siguientes comandos en la terminal:
   
     ```bash
     python3 --version
     pip3 --version
     ```

  - **Instalación del Módulo `venv`:** El módulo `venv` es parte de la biblioteca estándar de Python 3, por lo que ya deberías tenerlo disponible si estás usando una versión reciente de Python 3.

   - **Crear un entorno virtual:** Usas `venv` que es un módulo estándar disponible en Python 3.
     ```bash
     python -m venv nombre_del_entorno
     ```
   - **Activar el entorno virtual:**
     - En Windows:
       ```bash
       .\nombre_del_entorno\Scripts\activate
       ```
     - En macOS/Linux:
       ```bash
       source nombre_del_entorno/bin/activate
       ```
   - Cuando un entorno virtual está activado, el terminal indicará el nombre cerca del prompt, dejándote ver visualmente que estás trabajando dentro de ese entorno.
   - **Desactivar el entorno virtual:**
     ```bash
     deactivate
     ```
   - Esto te retorna al sistema Python global.

5. **Uso Práctico:**
   - Los entornos virtuales son esenciales cuando colaboras en proyectos, pues puedes definir un `requirements.txt` con todas las dependencias necesarias y compartirlo con otros desarrolladores. Simplemente pueden replicar el entorno usando:
     ```bash
     pip install -r requirements.txt
     ```

Usar entornos virtuales es una gran práctica que te ayudará a mantener la organización, prevenir problemas con dependencias y asegurar consistencia en tu entorno de desarrollo de Python.




## Recomendaciones para Instalar Python y Configurar VS Code


Para estudiantes principiantes, es esencial configurar un entorno de desarrollo que sea accesible, fácil de manejar y que facilite la instalación de paquetes y el manejo de proyectos en Python. Aquí tienes una guía para establecer un entorno amigable utilizando Visual Studio Code (VS Code):


#### Paso 1: Instalar Python

1. **Descargar Python:**
   - Visita [python.org](https://www.python.org/) y descarga la última versión estable de Python.
   - Durante la instalación, asegúrate de seleccionar la opción **"Add Python to PATH"** para que Python esté disponible desde cualquier terminal.

2. **Verificar la Instalación:**
   - Abre una terminal (Command Prompt en Windows o Terminal en macOS/Linux) y escribe:
     ```bash
     python --version
     ```
   - Esto debería mostrar la versión de Python que instalaste.

#### Paso 2: Instalar Visual Studio Code (VS Code)

1. **Descargar VS Code:**
   - Visita [code.visualstudio.com](https://code.visualstudio.com/) y descarga el editor.

2. **Instalar VS Code:**
   - Sigue las instrucciones del instalador para completar la instalación.

#### Paso 3: Configurar VS Code para Python

1. **Instalar la Extensión de Python:**
   - Abre VS Code y ve a la pestaña de Extensiones (o presiona `Ctrl+Shift+X`).
   - Busca "Python" y selecciona la extensión oficial de Microsoft, luego haz clic en "Instalar".

2. **Configurar el Entorno Python:**
   - Abre la paleta de comandos (con `Ctrl+Shift+P`) y busca "Python: Select Interpreter".
   - Selecciona el intérprete de Python instalado (deberías ver la lista de versiones instaladas).

#### Paso 4: Configurar un Entorno Virtual

Para facilitar el manejo de librerías y evitar conflictos de versiones, se recomienda usar entornos virtuales:

1. **Crear un Entorno Virtual:**
   - Abre tu terminal dentro de VS Code (con `Ctrl+ñ`) y navega al directorio del proyecto.
   - Crea un entorno virtual usando `venv`:
     ```bash
     python -m venv venv
     ```
   - Este comando creará una carpeta llamada `venv` que contiene un entorno aislado.

2. **Activar el Entorno Virtual:**
   - En Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Notar el Cambio de Entorno:**
   - Deberías ver que el nombre del entorno (e.g., `venv`) aparece al comienzo de la línea de comandos como indicativo de que el entorno virtual está activo.

#### Paso 5: Instalación de Librerías

1. **Instalar Librerías Necesarias:**
   - Mientras el entorno virtual está activado, puedes instalar librerías usando `pip`:
     ```bash
     pip install nombre_de_la_libreria
     ```
   - Por ejemplo, para instalar NumPy:
     ```bash
     pip install numpy
     ```

2. **Crear un Archivo Requirements:**
   - Para facilitar la instalación de librerías en otros entornos, crea un archivo `requirements.txt`:
     ```bash
     pip freeze > requirements.txt
     ```

#### Paso 6: Prueba de Configuración

1. **Probar la Configuración con un Script Simple:**
   - Crea un archivo `main.py` y pega el siguiente código:
     ```python
     import numpy as np

     a = np.array([1, 2, 3])
     print(f"Array: {a}")
     ```
   - Ejecuta el script desde la terminal dentro de VS Code para verificar que todo esté funcionando correctamente:
     ```bash
     python main.py
     ```
     
  
