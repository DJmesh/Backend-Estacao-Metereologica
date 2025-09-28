# Python slim
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Sistema
RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Reqs
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Código
COPY . .

# Coleta de estáticos no build (usa DEBUG=0 por padrão no Render)
RUN python manage.py collectstatic --noinput

# Entrypoint
COPY deploy/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000
CMD ["/entrypoint.sh"]
