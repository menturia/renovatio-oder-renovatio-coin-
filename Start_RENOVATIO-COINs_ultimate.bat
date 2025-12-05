@echo off
title RENOVATIO-COIN 2025 ULTIMATE EDITION
chcp 65001 > nul
cls
echo.
echo    ============================================
echo        RENOVATIO-COIN 2025 ULTIMATE EDITION
echo    ============================================
echo.

:: Versuche verschiedene Python-Befehle
python --version > nul 2>&1
if %errorlevel%==0 (
    python "%~dp0RENOVATIO-COIN_ultimate.py"
    goto :end
)

py --version > nul 2>&1
if %errorlevel%==0 (
    py "%~dp0RENOVATIO-COIN_ultimate.py"
    goto :end
)

python3 --version > nul 2>&1
if %errorlevel%==0 (
    python3 "%~dp0RENOVATIO-COIN_ultimate.py"
    goto :end
)

:: Wenn kein Python gefunden wurde
echo.
echo ❌ ERROR: Python wurde nicht gefunden!
echo.
echo BITTE FOLGENDES TUN:
echo 1. Python von python.org installieren
echo 2. Wichtig: "Add Python to PATH" aktivieren
echo 3. Oder den vollständigen Pfad zu Python unten eintragen
echo.
echo Beispiel: C:\Python311\python.exe "RENOVATIO-COIN_ultimate.py"
echo.
pause
exit /b 1

:end
pause