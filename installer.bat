@echo off
title Instalador de Crosshair Widget
color 0A

echo ============================================
echo    INSTALADOR DE CROSSHAIR WIDGET v1.0.3
echo ============================================
echo.

REM Verificar permisos de administrador
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Este instalador requiere permisos de administrador
    echo.
    echo Por favor, haz clic derecho en este archivo y selecciona
    echo "Ejecutar como administrador"
    echo.
    pause
    exit /b 1
)

echo [1/2] Instalando certificado de seguridad...
certutil -addstore TrustedPeople Crosshair_1.0.3.0_x86_x64.cer >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: No se pudo instalar el certificado
    echo Verifica que el archivo Crosshair_1.0.3.0_x86_x64.cer este en la misma carpeta
    pause
    exit /b 1
)
echo    Certificado instalado correctamente
echo.

echo [2/2] Instalando Crosshair Widget...
start /wait Crosshair_1.0.3.0_x86_x64.msixbundle
if %errorlevel% neq 0 (
    echo ERROR: No se pudo instalar la aplicacion
    echo Verifica que el archivo Crosshair_1.0.3.0_x86_x64.msixbundle este en la misma carpeta
    pause
    exit /b 1
)

echo.
echo ============================================
echo    INSTALACION COMPLETADA
echo ============================================
echo.
echo Crosshair Widget ha sido instalado correctamente
echo Puedes abrirlo desde Xbox Game Bar (Win + G)
echo.
pause