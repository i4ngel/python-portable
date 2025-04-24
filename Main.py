import subprocess
import sys

# Lista de todas las librerías necesarias para el proyecto
Librerias_Requeridas = ['minecraft_launcher_lib']

# Función para verificar e instalar librerías
def instalar_libreria(libreria):
    try:
        # Intenta importar el módulo
        __import__(libreria)
    except ImportError:
        print(f"❌ No se encontró la librería {libreria}. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", libreria])

# Verificar todas las librerías necesarias
for libreria in Librerias_Requeridas:
    instalar_libreria(libreria)

import minecraft_launcher_lib
import subprocess
import os

# Definir nombre personalizado del directorio del launcher
NOMBRE_LAUNCHER = ".LauncherAngel"

# Obtener ruta del usuario
user_window = os.environ['username']
minecraft_directory = os.path.join(f"C:/Users/{user_window}/AppData/Roaming", NOMBRE_LAUNCHER)

# Crear el directorio si no existe
if not os.path.exists(minecraft_directory):
    print(f"📁 Creando carpeta del launcher en: {minecraft_directory}")
    os.makedirs(minecraft_directory)
else:
    print(f"✅ Carpeta del launcher encontrada: {minecraft_directory}")

# Función para instalar una versión de Minecraft
def instalar_minecraft(version):
    print(f"⬇  Instalando Minecraft {version}...")
    try:
        minecraft_launcher_lib.install.install_minecraft_version(version, minecraft_directory)
        print("✅ Instalación completada.")
    except Exception as e:
        print(f"❌ Error al instalar Minecraft {version}: {e}")

# Función para iniciar Minecraft con una versión específica
def iniciar_minecraft(nombre, ver):
    versiones_instaladas = [v['id'] for v in minecraft_launcher_lib.utils.get_installed_versions(minecraft_directory)]

    if ver not in versiones_instaladas:
        print(f"⚠  Versión {ver} no instalada. Instalando automáticamente...")
        instalar_minecraft(ver)
    else:
        print(f"✅ Versión {ver} ya instalada.")

    options = {
        "username": nombre,
        "uuid": "",  # Autenticación futura
        "token": "",
        "jvmArguments": ["-Xmx2G", "-Xms1G"],
        "launcherVersion": "0.0.2",
    }

    try:
        print("🚀 Iniciando Minecraft...")
        minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(ver, minecraft_directory, options)
        subprocess.run(minecraft_command)
    except Exception as e:
        print(f"❌ No se pudo iniciar Minecraft: {e}")

# Mostrar las versiones instaladas
def mostrar_versiones_instaladas():
    versiones_instaladas = minecraft_launcher_lib.utils.get_installed_versions(minecraft_directory)
    if not versiones_instaladas:
        print("\n📦 No hay versiones instaladas actualmente.")
        return []
    else:
        print("\n📋 --- Versiones instaladas ---")
        for i, v in enumerate(versiones_instaladas, 1):
            print(f"{i}. {v['id']}")
        return [v['id'] for v in versiones_instaladas]

# Menú principal
def menu():
    while True:
        print("\n🕹  Menú Principal")
        print("1. Instalar Minecraft")
        print("2. Iniciar Minecraft")
        print("3. Mostrar versiones instaladas")
        print("4. Salir")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            version = input("Ingrese la versión de Minecraft a instalar: ")
            instalar_minecraft(version)
        elif choice == "2":
            nombre = input("Ingrese su nombre de usuario: ")
            versiones_instaladas = mostrar_versiones_instaladas()
            if versiones_instaladas:
                try:
                    ver_index = int(input(f"Seleccione la versión de Minecraft a iniciar (1-{len(versiones_instaladas)}): ")) - 1
                    ver = versiones_instaladas[ver_index]
                    iniciar_minecraft(nombre, ver)
                except (ValueError, IndexError):
                    print("❌ Selección inválida.")
        elif choice == "3":
            mostrar_versiones_instaladas()
        elif choice == "4":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("⚠  Opción no válida. Intente nuevamente.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
