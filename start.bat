@echo off
setlocal enabledelayedexpansion

echo Starting Broadcast App with Docker...

REM Check if .env file exists
if not exist .env (
    echo .env file not found! Please create it first.
    echo Copy env.example to .env and update the values:
    echo copy env.example .env
    pause
    exit /b 1
)

REM Function to check if Docker is running
docker info >nul 2>&1
if errorlevel 1 (
    echo Docker is not running! Please start Docker Desktop.
    pause
    exit /b 1
)

if "%1"=="start" (
    echo Building and starting services...
    docker-compose up --build -d
    
    echo Waiting for services to be ready...
    timeout /t 10 /nobreak >nul
    
    echo Running database migrations...
    docker-compose exec web python manage.py migrate
    
    echo Setting up Celery Beat...
    docker-compose exec web python manage.py setup_celery_beat
    
    echo All services are running!
    echo Web app: http://localhost:8000
    echo Admin: http://localhost:8000/admin
    pause
) else if "%1"=="stop" (
    echo Stopping services...
    docker-compose down
    echo Services stopped!
    pause
) else if "%1"=="restart" (
    echo Restarting services...
    docker-compose restart
    echo Services restarted!
    pause
) else if "%1"=="logs" (
    echo Viewing logs...
    docker-compose logs -f
) else if "%1"=="status" (
    echo Service status:
    docker-compose ps
    pause
) else (
    echo Usage: %0 {start^|stop^|restart^|logs^|status}
    echo.
    echo Commands:
    echo   start   - Build and start all services
    echo   stop    - Stop all services
    echo   restart - Restart all services
    echo   logs    - View logs from all services
    echo   status  - Show status of all services
    pause
) 