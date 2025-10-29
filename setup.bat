@echo off
REM Medical Portal - Quick Setup Script for Windows

echo ============================================
echo Medical Portal - Setup Script
echo ============================================
echo.

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    exit /b 1
)

echo [1/5] Installing Python packages...
pip install django mysqlclient pillow
if errorlevel 1 (
    echo ERROR: Failed to install packages
    exit /b 1
)
echo OK

echo.
echo [2/5] Running makemigrations...
python manage.py makemigrations
if errorlevel 1 (
    echo ERROR: makemigrations failed (check MySQL connection)
    exit /b 1
)
echo OK

echo.
echo [3/5] Running migrations...
python manage.py migrate
if errorlevel 1 (
    echo ERROR: migrate failed (check MySQL connection)
    exit /b 1
)
echo OK

echo.
echo [4/5] Creating superuser...
echo Enter superuser credentials below:
python manage.py createsuperuser
echo OK

echo.
echo ============================================
echo Setup Complete!
echo ============================================
echo.
echo Next steps:
echo 1. Start the server: python manage.py runserver
echo 2. Visit: http://127.0.0.1:8000/signup/
echo 3. Admin panel: http://127.0.0.1:8000/admin/
echo.
echo For MySQL troubleshooting, see MYSQL_SETUP.md
echo For detailed guide, see README_BLOG_SYSTEM.md
echo.
pause
