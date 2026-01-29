@echo off
title Compilando QRGeneratorPro
cls

echo =======================================================
echo   GENERADOR DE EJECUTABLE - QRGeneratorPro
echo =======================================================
echo.

:: 1. Verificamos que existan los archivos necesarios
if not exist "main.py" (
    color 0C
    echo [ERROR] No se encuentra el archivo 'main.py' en esta carpeta.
    pause
    exit /b
)

if not exist "version_info.txt" (
    color 0E
    echo [ADVERTENCIA] No se encontro 'version_info.txt'.
    echo El comando fallara si el archivo no existe.
    echo.
    echo Quieres continuar de todos modos? (Ctrl+C para cancelar)
    pause
)

:: 2. Limpieza de archivos temporales previos (Recomendado para evitar errores)
echo [INFO] Limpiando archivos temporales antiguos...
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "QRGeneratorPro.spec" del "QRGeneratorPro.spec"

:: 3. Ejecucion del comando PyInstaller
echo.
echo [INFO] Iniciando PyInstaller...
echo.

:: --- COMANDO PRINCIPAL ---
python -m PyInstaller --clean --onefile --noconsole --name "QRGeneratorPro" --version-file="version_info.txt" --icon="app_icon.ico" main.py
:: -------------------------

:: 4. Verificamos si hubo errores
if %errorlevel% neq 0 (
    color 0C
    echo.
    echo =======================================================
    echo   [FALLO] Ocurrio un error al crear el EXE.
    echo   Revisa los mensajes de error arriba.
    echo =======================================================
    pause
    exit /b
)

:: 5. Éxito
color 0A
echo.
echo =======================================================
echo   [EXITO] Compilacion completada correctamente.
echo   Tu archivo esta en la carpeta: dist/QRGeneratorPro.exe
echo =======================================================
echo.
pause