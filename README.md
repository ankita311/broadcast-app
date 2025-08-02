# My Neighbourhood

A community-driven neighborhood communication platform built with Django, designed to help residents share information, report grievances, and keep everyone informed about local happenings.

## Purpose

My Neighbourhood is specifically designed for:
- **Residents** to share neighborhood updates and concerns
- **RWA Members** to receive and address community grievances
- **Society Secretaries** to stay informed about maintenance and safety issues
- **Community Leaders** to disseminate important announcements

## Features

### **Community Communication**
- **Categorized Posts**: Share information under relevant categories (Celebration, Grievance, Information, Safety, etc.)
- **Scheduled Publishing**: Schedule posts for optimal timing
- **Image Support**: Include photos with your posts
- **User Profiles**: Complete profiles with address information

### **Smart Notifications**
- **Real-time Updates**: Get notified when people you follow post
- **Category-based Alerts**: Different notification types for different concerns
- **Read/Unread Tracking**: Keep track of important notifications

### **Community Management**
- **Follow System**: Follow neighbors to stay updated
- **User Profiles**: View detailed profiles with contact information
- **Address Integration**: Include house number, building, and society details

### **Content Management**
- **Post Categories**: 
  - **Celebration** - Happy events and achievements
  - **Grievance** - Complaints and issues
  - **Information** - General updates
  - **Invitation** - Event invitations
  - **Safety & Security** - Security concerns
  - **Maintenance** - Building/society maintenance
  - **Event** - Community events
  - **Announcement** - Official announcements
  - **Emergency** - Urgent matters
  - **Suggestion** - Improvement ideas
  - **Lost & Found** - Lost items
  - **Other** - Miscellaneous posts

## Quick Start

### Prerequisites
- Docker and Docker Compose
- Python 3.8+

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd broadcast
```

2. **Start the services**
```bash
# On Windows
start.bat

# On Linux/macOS
./start.sh
```

3. **Access the application**
- Open your browser and go to `http://localhost:8000`
- Register a new account or login

## Architecture

### **Backend Stack**
- **Django 5.2**: Web framework
- **PostgreSQL**: Database
- **Redis**: Caching and message broker
- **Celery**: Background task processing
- **Celery Beat**: Scheduled task management

### **Frontend**
- **HTML/CSS**: Clean, responsive design
- **Bootstrap-inspired**: Modern UI components
- **Mobile-friendly**: Responsive design for all devices

### **Key Components**
- **User Management**: Registration, profiles, authentication
- **Post System**: Create, edit, delete, categorize posts
- **Subscription System**: Follow/unfollow neighbors
- **Notification System**: Real-time updates
- **Scheduling System**: Automated post publishing

## Use Cases

### **For Residents**
- Report maintenance issues to RWA
- Share community celebrations
- Alert neighbors about security concerns
- Find lost items
- Get updates about society events

### **For RWA Members**
- Monitor community grievances
- Respond to maintenance requests
- Share official announcements
- Track community feedback

### **For Society Secretaries**
- Manage society communications
- Address resident concerns
- Coordinate maintenance activities
- Share important updates

## Development

### **Running Locally**
```bash
# Start all services
docker-compose up -d

# Run migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser

# Access admin panel
# http://localhost:8000/admin
```

### **File Structure**
```
src/
├── broadcast/          # Django project settings
├── website/           # Main Django app
│   ├── models.py     # Database models
│   ├── views.py      # Business logic
│   ├── forms.py      # Form handling
│   ├── templates/    # HTML templates
│   └── management/   # Custom commands
├── media/            # Uploaded files
└── staticfiles/      # Static assets
```

## 🚀 Deployment

The application is containerized with Docker for easy deployment:

- **Web Service**: Django application
- **Database**: PostgreSQL
- **Cache/Broker**: Redis
- **Background Tasks**: Celery worker
- **Scheduler**: Celery Beat

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License.

---

**My Neighbourhood** - Building stronger communities, one post at a time! 🏘️✨ 