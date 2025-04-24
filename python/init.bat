@echo off
:: Verificar si el entorno virtual existe
if not exist "%~dp0env\Scripts\activate.bat" (
    echo ❌ El entorno virtual no existe. Creándolo ahora...
    "%~dp0py\python.exe" -m venv "%~dp0env"
    
    :: Corregir el activate.bat para hacerlo portable (si es necesario)
    call "%~dp0fix_activate.bat"
) else (
    echo ✅ Entorno virtual encontrado.
)

:: Activar el entorno virtual
call "%~dp0env\Scripts\activate"

:: Instalar las dependencias desde el archivo requirements.txt (si es necesario)
echo 📦 Instalando dependencias...
"%~dp0env\Scripts\python.exe" -m pip install --upgrade pip > nul
"%~dp0env\Scripts\python.exe" -m pip install -r "%~dp0..\requirements.txt"

:: Ejecutar el archivo Main.py
echo 🚀 Ejecutando el script Main.py...
"%~dp0env\Scripts\python.exe" "%~dp0..\Main.py"

:: Pausar para ver resultados o errores
pause
