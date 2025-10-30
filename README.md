# screen recording
https://drive.google.com/file/d/1ECva8cTMOfwMWucUqJt3yXfizM3skpfB/view?usp=sharing

# Medical Portal

A comprehensive Django web application for doctors and patients with user authentication, role-based dashboards, and an integrated blog system.

## Features

- **User Management**
  - User registration with profile information
  - Role-based login (Doctor/Patient)
  - File upload for profile pictures
  
- **Blog System** (NEW!)
  - Doctors can create, edit, and delete blog posts
  - Save posts as drafts before publishing
  - Patients can view and filter published blogs by category
  - 4 predefined categories: Mental Health, Heart Disease, COVID-19, Immunization
  - Summary truncation (15 words max)
  - Responsive UI with Bootstrap

## Quick Start

### Prerequisites
- Python 3.8+
- MySQL 5.7+ (see MYSQL_SETUP.md for setup instructions)

### Installation

1. Install dependencies:
   ```bash
   pip install django mysqlclient pillow
   ```

2. Navigate to the project directory:
   ```bash
   cd medical_portal
   ```

3. Configure MySQL database (see MYSQL_SETUP.md):
   - Create database: `medical_portal_db`
   - Update `settings.py` if using different credentials

4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create superuser (optional, for admin panel):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Open your browser and go to `http://127.0.0.1:8000/signup/` to register.

## Usage

### Signup & Login
- **Signup**: Fill out the form at `/signup/` and select your role (Doctor or Patient)
- **Login**: Use `/login/` to log in. You will be redirected to your role-specific dashboard

### Doctor Dashboard
- View profile details
- **"My Blog Posts"** - View all your blogs (drafts + published)
- **"Create New Blog"** - Write a new blog post

### Doctor Blog Features
- Create blog posts with title, image, category, summary, and content
- Save posts as drafts to publish later
- Edit existing blogs
- Delete blogs
- Publish draft blogs anytime

### Patient Dashboard
- View profile details
- **"Read Blog Posts"** - Browse published blogs

### Patient Blog Features
- View all published blog posts
- Filter blogs by category (Mental Health, Heart Disease, COVID-19, Immunization)
- Click to read full blog content
- See blog summaries (truncated to 15 words)

## Project Structure

```
medical_portal/
├── accounts/               # User authentication app
│   ├── models.py          # User Profile model
│   ├── forms.py           # Signup form
│   ├── views.py           # Auth views
│   ├── urls.py            # Auth routes
│   └── templates/         # Auth templates
│
├── blog/                  # Blog system app
│   ├── models.py          # BlogCategory, BlogPost models
│   ├── forms.py           # BlogPostForm
│   ├── views.py           # Blog views (create, edit, view)
│   ├── urls.py            # Blog routes
│   ├── admin.py           # Admin configuration
│   ├── migrations/        # Database migrations
│   └── templates/         # Blog templates
│
├── medical_portal/        # Project settings
│   ├── settings.py        # Database & app configuration
│   └── urls.py            # Main URL routing
│
└── media/                 # Uploaded files (images)
```

## Technologies Used

- **Backend**: Django 5.2
- **Database**: MySQL (or SQLite for development)
- **Frontend**: Bootstrap 5.3
- **Image Processing**: Pillow
- **ORM**: Django ORM

## Configuration

### MySQL Setup
See `MYSQL_SETUP.md` for detailed MySQL installation and configuration steps.

### Database
The application uses MySQL by default. Configuration in `settings.py`:
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "medical_portal_db",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}
```

### Media Files
- Profile pictures: `media/profile_pics/`
- Blog images: `media/blog_images/`

## Admin Panel

Access admin panel at `http://127.0.0.1:8000/admin/` with superuser credentials to:
- Manage users and profiles
- Create/manage blog categories
- View/edit/delete blog posts
- Filter posts by status, category, and author

## Notes

- All fields are required during signup except profile picture
- Passwords must match during signup
- Blog categories are auto-created during migration
- Drafts are only visible to the author
- Published blogs are visible to all patients
- Summaries are automatically truncated to 15 words
