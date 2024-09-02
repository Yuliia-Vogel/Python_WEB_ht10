# Python_WEB_ht10
App for adding quotes to the web-page. App created with Django 5 (потім ще перевірити версію!!!).

1) Installed Postgres DB, and account at MongoDB, and ready database cluster
2) Create venv: python -m venv venv
3) pip install pymongo sqlalchemy psycopg2 django python-dotenv
4) Create .env file with your credentials for your MongoDB and your Postgres DB.
5) Create migrations: python manage.py makemigrations
6) Run migrations: python manage.py migrate
7) Run script for data migration: python migrate_data.py
8) Check if all data were transferred from MongoDB to PostgreSQL.
9) 

django

