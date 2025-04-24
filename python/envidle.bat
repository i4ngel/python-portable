@echo off
call %~dp0env\Scripts\activate
"%~dp0env\Scripts\python.exe" "%cd%\py\Lib\idlelib\idle.pyw"
pause
