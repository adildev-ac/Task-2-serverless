# Medical Portal

A Django web application for doctors and patients to sign up and log in, with role-based dashboards.

## Features

- User registration with profile information
- Role-based login (Doctor/Patient)
- File upload for profile pictures
- Responsive UI with Bootstrap
- SQLite database

## Setup Instructions

1. Ensure Python 3.8+ is installed.

2. Install dependencies:
   ```
   pip install django pillow
   ```

3. Navigate to the project directory:
   ```
   cd medical_portal
   ```

4. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

6. Open your browser and go to `http://127.0.0.1:8000/signup/` to register a new user.

## Usage

- **Signup**: Fill out the form at `/signup/` and select your role (Doctor or Patient).
- **Login**: Use `/login/` to log in. You will be redirected to your role-specific dashboard.
- **Dashboards**: Doctors and patients see their profile details on their respective dashboards.

## Project Structure

- `medical_portal/`: Main project directory
- `accounts/`: Django app for user accounts
  - `models.py`: Profile model
  - `forms.py`: Signup form
  - `views.py`: Views for signup, login, dashboards
  - `templates/accounts/`: HTML templates

## Technologies Used

- Django 5.2
- Bootstrap 5.3
- SQLite
- Pillow for image handling

## Notes

- Profile pictures are stored in `media/profile_pics/`.
- Passwords must match during signup.
- All fields are required except profile picture.