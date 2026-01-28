@echo off
echo ========================================
echo   QR Generator Pro
echo ========================================
echo.
python main.py
if errorlevel 1 (
    echo.
    echo ERROR: No se pudo ejecutar la aplicacion
    echo Asegurate de haber ejecutado install.bat primero
    pause
)
