# Meteo Station API

Steps:
1. Create venv and install requirements:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Migrate and create superuser:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```
3. Run:
   ```bash
   python manage.py runserver
   ```

Docs: `/api/docs/` (Swagger) – JWT auth available at `/api/auth/token/`.
