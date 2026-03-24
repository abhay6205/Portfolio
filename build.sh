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
