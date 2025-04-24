# Guía para Configurar un Entorno Virtual en Python (Portable)

Este README te guiará paso a paso sobre cómo configurar un entorno virtual de Python en una ubicación que no sea la ruta predeterminada (C:), como un USB o una carpeta personalizada en tu PC.

## Pasos para Configurar el Entorno Virtual

### **Paso 1: Descargar Python en una Ruta Personalizada**

1. **Descargar Python** desde el sitio oficial de Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. **Selecciona una ubicación diferente a la unidad C** para instalar Python. Por ejemplo, puedes instalarlo en un USB.

   **Ejemplo:**
   - Crea una carpeta en tu USB (por ejemplo, `E:\Python`).
   - Accede a la ruta de tu USB: `E:\`

### **Paso 2: Crear el Entorno Virtual**

1. Abre un **CMD como Administrador**.
2. En el CMD, dirígete a la raíz de tu USB (o a la carpeta donde hayas elegido instalar Python).
   ```bash
   E:\
   ```
3. Crea el entorno virtual con el siguiente comando:
   ```bash
   python -m venv venv
   ```
   Este comando generará las carpetas necesarias para el entorno virtual.

### **Paso 3: Configurar el Archivo pyvenv.cfg**

1. Una vez que las carpetas se hayan creado, navega hasta la carpeta `venv` (o `env`) y busca el archivo `pyvenv.cfg`.
2. **Edita el archivo** `pyvenv.cfg` con el siguiente contenido, modificando la ruta para que apunte correctamente a la ubicación donde descargaste Python.

   ```ini
   Home = ..\python
   include-system-site-packages = false
   version = 3.13.3
   ```

   - **Nota:** En este ejemplo, la carpeta donde descargaste Python es `python` y está ubicada en la raíz de tu USB.

### **Paso 4: Configurar el Archivo de Activación**

1. Navega hasta `venv\Scripts\` o `env\Scripts\`.
2. Abre el archivo `activate.bat` en un editor de texto.
3. Busca la línea que contiene:
   ```batch
   set "VIRTUAL_ENV=E:\Python\env"
   ```
4. Cámbiala por una de las siguientes líneas, dependiendo de cómo hayas nombrado la carpeta de tu entorno virtual:
   ```batch
   set "VIRTUAL_ENV=%cd%env"
   ```
   o
   ```batch
   set "VIRTUAL_ENV=%cd%venv"
   ```

   - Esto permite que el entorno virtual funcione independientemente de la ubicación del USB o carpeta donde esté el proyecto.

### **Paso 5: Usar el Entorno Virtual**

1. **Activar el entorno virtual** ejecutando el archivo `activate.bat` dentro de la carpeta `Scripts` (en `venv` o `env`).
2. Con el entorno virtual activado, podrás instalar paquetes y ejecutar tus proyectos sin interferir con otras instalaciones de Python en tu sistema.
