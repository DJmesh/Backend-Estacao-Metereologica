# Backend Estação Meteorológica

API backend em **Django + Django REST Framework** com **ViewSets**, **JWT (SimpleJWT)**, **Swagger (drf-spectacular)** e **Jazzmin** para painel administrativo.
O projeto fornece endpoints para gerenciar **Estações** e **Leituras meteorológicas** (Umidade, Temperatura, Direção/Velocidade do Vento, Pluviometria, Luminosidade), além de um **healthcheck** simples.

> **Status**: Esqueleto pronto para subir; migrações do `AUTH_USER_MODEL` (CustomUser) podem estar pendentes para finalizar a auth.
>
> **Stack**: Python 3.11+, Django 5, DRF, SimpleJWT, drf-spectacular, django-filter, Jazzmin.

---

## Tecnologias & Bibliotecas

- **Django 5** — Framework web Python.
- **Django REST Framework (DRF)** — API REST com ViewSets, filtros, paginação.
- **SimpleJWT** — Autenticação via JSON Web Tokens.
- **drf-spectacular** — Geração de schema OpenAPI + UI Swagger (protegida por JWT).
- **django-filter** — Filtros declarativos.
- **Jazzmin** — Tema moderno para o `django-admin`.

---

## Arquitetura & Padrões

- **`app/`**: settings, urls, wsgi/asgi.
- **`base/`**: `BaseModel` abstrato com `guid` (UUID) como PK, `created_at`, `updated_at`.
- **`user/`**: `CustomUser` (UUID como PK) + admin; `AUTH_USER_MODEL = "user.User"`.
- **`core/`**: healthcheck público (`GET /api/health/`).
- **`weather/`**: 
  - **Station**: nome, descrição, lat/long, ativo.
  - **Reading**: FK para Station + humidity, temperature, wind_dir, wind_speed, rain_mm, luminosity + `measured_at`.
  - ViewSets com filtros por estação e janelas de data (`created_after/before`, `measured_after/before`).

### Estrutura (resumo)
```
app/
  settings.py # Corrigir problema do AuthUser
  urls.py
base/
  apps.py
  models/
    base.py         # BaseModel (UUID + timestamps)
user/
  apps.py
  models/
    __init__.py
    user.py      # Utilizar AuthUser do django 
  admin/
    user_admin.py
core/
  apps.py
  views/
    health.py
weather/
  apps.py
  models/
    station.py
    reading.py
  serializers/
    station_serializers.py
    reading_serializers.py
  views/
    station_views.py
    reading_views.py
  admin/
    weather_admin.py
```

---

## ⚙️ Configuração

### 1) Requisitos
- Python 3.11+
- pip / venv
- (Opcional) Postgres

### 2) Ambiente
```bash
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

> Se não houver `requirements.txt`, instale:
```bash
pip install django djangorestframework djangorestframework-simplejwt drf-spectacular django-filter jazzmin
```

### 3) Variáveis de ambiente
```
DJANGO_SECRET_KEY="troque-isto-em-producao"
DJANGO_DEBUG=1
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=<path ou db.sqlite3>
```

---

## 🔐 Autenticação (JWT)

- `POST /api/auth/token/` — recebe `username` e `password` e retorna `{ access, refresh }`.
- `POST /api/auth/refresh/` — envia `{ refresh }` e recebe um novo `{ access }`.
- **Swagger UI** em `/api/docs/` **só** abre endpoints se você clicar em **Authorize** e colar `Bearer <access>`.

**Exemplo (PowerShell / curl):**
```bash
curl -X POST http://127.0.0.1:8000/api/auth/token/ ^
  -H "Content-Type: application/json" ^
  -d "{\"username\":\"admin\",\"password\":\"sua_senha\"}"
```

---

## Endpoints Principais

- `GET /api/health/` — público, status do serviço.
- `GET /api/docs/` — Swagger UI (protegido por JWT).
- `GET /api/schema/` — OpenAPI (JSON).
- `stations/` (ViewSet):
  - `GET /api/stations/` — lista
  - `POST /api/stations/` — cria
  - `GET /api/stations/{guid}/` — detalhe
  - `PATCH/PUT/DELETE /api/stations/{guid}/`
  - `GET /api/stations/{guid}/latest-reading/` — última leitura
- `readings/` (ViewSet):
  - `GET /api/readings/?station=<guid>&measured_after=...&measured_before=...`
  - `POST /api/readings/` — cria leitura
  - CRUD completo via ViewSet
- `users/` (se habilitado):
  - `GET /api/users/` (autenticado), operações de escrita reservadas a staff
  - `GET /api/me/` — dados do usuário logado

---

## Modelagem

### BaseModel
- `guid: UUID (PK)`
- `created_at: datetime`
- `updated_at: datetime`

### User (custom)
- Extende `AbstractUser`
- `guid: UUID (PK)`

### Station
- `name: str (unique)`
- `description: str`
- `latitude/longitude: Decimal`
- `is_active: bool`

### Reading
- `station: FK(Station)`
- `humidity, temperature, wind_dir, wind_speed, rain_mm, luminosity: float`
- `measured_at: datetime (opcional)`

---

## Execução (Dev)

```bash
# gerar e aplicar migrações
python manage.py makemigrations
python manage.py migrate

# criar superusuário
python manage.py createsuperuser

# subir servidor
python manage.py runserver
```

> **Nota:** Se aparecer erro de `AUTH_USER_MODEL`, verifique:
> - `AUTH_USER_MODEL = "user.User"` em `settings.py`.
> - Não existe arquivo `user/models.py` conflitando com a pasta `user/models/`.
> - `user/models/__init__.py` contém `from .user import User`.
> - Use `INSTALLED_APPS = ["user.apps.UserConfig", ...]`.

---

## Testes (sugestão futura)
- `pytest` + `pytest-django` para testes de API.
- Factories com `model_bakery`.

---

## Roadmap / TODO
- [ ] Resolver migrações do CustomUser (`AUTH_USER_MODEL`).
- [ ] Adicionar `requirements.txt`/`poetry.lock`.
- [ ] Docker Compose (Django + Postgres + Redis opcional).
- [ ] Endpoint de agregações (médias por hora/dia, chuva acumulada, rajada máxima).
- [ ] CORS (se front for separado).

---

## Contribuição & Commits

Siga **Conventional Commits**:
- `feat:` nova funcionalidade
- `fix:` correção de bug
- `docs:` documentação
- `chore:` rotinas e manutenção
- `refactor:`, `test:`, etc.

Exemplos:
- `feat(weather): add Station and Reading models with viewsets`
- `fix(auth): adjust AUTH_USER_MODEL and migrations order`
- `docs(readme): add quickstart and endpoints`

---

## Licença
MIT — veja `LICENSE`.
