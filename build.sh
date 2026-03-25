#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Convert static files
cd portfolio
python manage.py collectstatic --no-input

# Apply migrations
python manage.py migrate

# Create superuser if it doesn't exist
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
import os
username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', '')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
if password and not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print('Superuser created.')
else:
    print('Superuser already exists or password not set.')
"
