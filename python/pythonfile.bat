@echo off
call "%~dp0env\Scripts\activate"
"%~dp0env\Scripts\python.exe" -m pip install -r "%~dp0..\requirements.txt"
"%~dp0env\Scripts\python.exe" "%~dp0..\Main.py"
pause
