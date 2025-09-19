# How to run

1. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
2. Generate a new Django secret key and add it to your settings.
3. Make sure DEBUG = False in settings.
4. Start the server:
   ```bash 
   python manage.py runserver
   ```
