@echo off
:: Activar el entorno virtual
call "%~dp0env\Scripts\activate"

:: Instalar las dependencias desde el archivo requirements.txt (si es necesario)
echo Instalando dependencias...
"%~dp0env\Scripts\python.exe" -m pip install -r "%~dp0..\requirements.txt"

:: Ejecutar el archivo Main.py
echo Ejecutando el script Main.py...
"%~dp0env\Scripts\python.exe" "%~dp0..\Main.py"

:: Pausar para que puedas ver cualquier mensaje de error o resultado
pause
