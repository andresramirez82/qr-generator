@echo off
echo ========================================
echo   QR Generator Pro - Instalador
echo ========================================
echo.

echo Verificando Python...
python --version
if errorlevel 1 (
    echo ERROR: Python no esta instalado
    echo Por favor instala Python 3.8 o superior desde https://www.python.org/
    pause
    exit /b 1
)

echo.
echo Instalando dependencias...
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERROR: No se pudieron instalar las dependencias
    pause
    exit /b 1
)

echo.
echo ========================================
echo   Instalacion completada!
echo ========================================
echo.
echo Para ejecutar la aplicacion, usa: run.bat
echo O ejecuta: python main.py
echo.
pause
