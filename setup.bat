@echo off
title Discord Multi Tool - Setup

echo Checking Python...

python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is NOT installed!
    echo Please install Python and add it to PATH.
    pause
    exit
)

echo Python found!
echo.

echo Installing requirements...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo.
echo Starting tool...
python main.py

pause
