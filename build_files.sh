#!/bin/bash
pip install -r requirements.txt
python portfolio/manage.py collectstatic --noinput --clear
