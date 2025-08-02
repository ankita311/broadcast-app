#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting Broadcast App with Docker...${NC}"

# Check if .env file exists
if [ ! -f .env ]; then
    echo -e "${RED}.env file not found! Please create it first.${NC}"
    echo "Copy env.example to .env and update the values:"
    echo "cp env.example .env"
    exit 1
fi

# Function to check if Docker is running
check_docker() {
    if ! docker info > /dev/null 2>&1; then
        echo -e "${RED}Docker is not running! Please start Docker Desktop.${NC}"
        exit 1
    fi
}

# Function to build and start services
start_services() {
    echo -e "${YELLOW}Building and starting services...${NC}"
    docker-compose up --build -d
    
    echo -e "${YELLOW}Waiting for services to be ready...${NC}"
    sleep 10
    
    echo -e "${YELLOW}Running database migrations...${NC}"
    docker-compose exec web python manage.py migrate
    
    echo -e "${YELLOW}Setting up Celery Beat...${NC}"
    docker-compose exec web python manage.py setup_celery_beat
    
    echo -e "${GREEN}All services are running!${NC}"
    echo -e "${GREEN}Web app: http://localhost:8000${NC}"
    echo -e "${GREEN}Admin: http://localhost:8000/admin${NC}"
}

# Function to stop services
stop_services() {
    echo -e "${YELLOW}Stopping services...${NC}"
    docker-compose down
    echo -e "${GREEN}Services stopped!${NC}"
}

# Function to view logs
view_logs() {
    echo -e "${YELLOW}Viewing logs...${NC}"
    docker-compose logs -f
}

# Function to restart services
restart_services() {
    echo -e "${YELLOW}Restarting services...${NC}"
    docker-compose restart
    echo -e "${GREEN}Services restarted!${NC}"
}

# Main script logic
case "$1" in
    "start")
        check_docker
        start_services
        ;;
    "stop")
        stop_services
        ;;
    "restart")
        check_docker
        restart_services
        ;;
    "logs")
        view_logs
        ;;
    "status")
        docker-compose ps
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|logs|status}"
        echo ""
        echo "Commands:"
        echo "  start   - Build and start all services"
        echo "  stop    - Stop all services"
        echo "  restart - Restart all services"
        echo "  logs    - View logs from all services"
        echo "  status  - Show status of all services"
        ;;
esac 