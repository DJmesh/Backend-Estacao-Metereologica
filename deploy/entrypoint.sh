#!/usr/bin/env bash
set -e

# Render define PORT automaticamente
export PORT="${PORT:-8000}"

# Garanta caminho do sqlite numa área gravável/persistente
export DB_NAME="${DB_NAME:-/data/db.sqlite3}"

# Cria diretório do DB se necessário
mkdir -p "$(dirname "$DB_NAME")"

# Migrações
python manage.py migrate --noinput

# Cria superusuário se não existir
python manage.py shell <<'PY'
from django.contrib.auth import get_user_model
User = get_user_model()
u, e, p = "admin", "admin@admin.com", "admin"
if not User.objects.filter(username=u).exists():
    User.objects.create_superuser(u, e, p)
    print("Superuser created:", u)
else:
    print("Superuser already exists:", u)
PY

# Sobe o servidor
exec gunicorn app.wsgi:application --bind 0.0.0.0:${PORT} --workers 3 --timeout 120
