# Readme.md

## Overview

This is a Flask-based portfolio website for Seema Devi, an AI & Automation Engineer. The application is a personal portfolio showcasing professional experience, skills, and providing a contact form functionality. The site is built with a modern, responsive design using Bootstrap 5 and includes features like resume download and contact form submission.

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 templates with Flask
- **CSS Framework**: Bootstrap 5.3.0 for responsive design
- **JavaScript**: Vanilla JavaScript for interactive features
- **Icons**: Font Awesome 6.4.0
- **Fonts**: Google Fonts (Inter)

### Backend Architecture
- **Framework**: Flask 3.1.1 (Python web framework)
- **WSGI Server**: Gunicorn for production deployment
- **Form Handling**: Flask-WTF with WTForms for form validation
- **Session Management**: Flask sessions with configurable secret key

### Application Structure
```
├── app.py          # Flask application factory
├── main.py         # Application entry point
├── routes.py       # URL routing and view functions
├── forms.py        # Form definitions and validation
├── templates/      # Jinja2 templates
├── static/         # CSS, JS, and assets
└── pyproject.toml  # Python dependencies
```

## Key Components

### 1. Application Factory (`app.py`)
- Creates Flask application instance
- Configures session secret key from environment variables
- Implements ProxyFix middleware for deployment behind reverse proxy
- Handles circular import prevention

### 2. Routing System (`routes.py`)
- **Home Route** (`/`): Serves the main portfolio page
- **Contact Route** (`/contact`): Handles POST requests for contact form
- **Resume Download** (`/download-resume`): Serves PDF resume file

### 3. Form Validation (`forms.py`)
- ContactForm class with comprehensive validation
- Field validations: name, email, subject, message
- CSRF protection via Flask-WTF
- Custom error messaging and length constraints

### 4. Template System
- **Base Template**: Common layout, navigation, and assets
- **Index Template**: Main portfolio content with sections
- Responsive design with mobile-first approach

### 5. Static Assets
- Custom CSS with CSS variables for theming
- Interactive JavaScript for smooth scrolling and animations
- Resume PDF file for download functionality

## Data Flow

### Contact Form Submission
1. User fills out contact form on homepage
2. Form data submitted via POST to `/contact` endpoint
3. Flask-WTF validates form data server-side
4. Success: Flash message displayed, redirect to contact section
5. Failure: Error messages flashed, redirect back to form

### Resume Download
1. User clicks download resume button
2. Request sent to `/download-resume` endpoint
3. Flask serves PDF file with proper headers
4. File not found: Error message flashed, redirect to homepage

## External Dependencies

### Python Packages
- **Flask**: Web framework (3.1.1)
- **Flask-WTF**: Form handling and CSRF protection (1.2.2)
- **WTForms**: Form validation (3.2.1)
- **Email-Validator**: Email validation (2.2.0)
- **Gunicorn**: WSGI HTTP server (23.0.0)
- **Flask-SQLAlchemy**: Database ORM (3.1.1) - Ready for future database integration
- **psycopg2-binary**: PostgreSQL adapter (2.9.10) - Ready for PostgreSQL integration
- **Werkzeug**: WSGI utilities (3.1.3)

### Frontend Dependencies (CDN)
- Bootstrap 5.3.0
- Font Awesome 6.4.0
- Google Fonts (Inter)


## User Preferences

```
Preferred communication style: Simple, everyday language.
```