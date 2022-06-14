#!/bin/bash
flask db init
flask db migrate
flask db upgrade
flask init
gunicorn -b 0.0.0.0:5000 app.wsgi:app