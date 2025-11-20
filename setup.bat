@echo off
echo ========================================
echo   LinkedIn Post Generator - Setup
echo ========================================
echo.

echo Checking Python installation...
python --version
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ from python.org
    pause
    exit /b 1
)
echo.

echo Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt
echo.

echo Testing installation...
python test_installation.py
echo.

echo ========================================
echo   Setup Complete!
echo ========================================
echo.
echo Next steps:
echo   1. Run demo: python demo.py
echo   2. Try CLI: python cli.py --help
echo   3. Check examples: dir examples
echo   4. Read documentation: README.md
echo.

pause
