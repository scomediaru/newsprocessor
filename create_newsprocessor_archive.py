
## 🤝 Участие в проекте

1. Fork репозитория
2. Создай feature branch: `git checkout -b feature/amazing-feature`
3. Commit изменения: `git commit -m 'Add amazing feature'`
4. Push в branch: `git push origin feature/amazing-feature`
5. Создай Pull Request

## 📄 Лицензия

MIT License. См. [LICENSE](LICENSE) для деталей.

## 🆘 Поддержка

- 📧 Email: support@newsprocessor.com
- 🐛 Issues: https://github.com/your-username/newsprocessor/issues
- 💬 Discussions: https://github.com/your-username/newsprocessor/discussions
""",

        f"{project_name}/.env.example": """# === ОСНОВНЫЕ НАСТРОЙКИ DJANGO ===
SECRET_KEY=your-super-secret-key-change-this-in-production-min-50-chars
DEBUG=False
ALLOWED_HOSTS=your-domain.com,www.your-domain.com,localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=https://your-domain.com,https://www.your-domain.com

# === БАЗА ДАННЫХ ===
DB_NAME=news_processor
DB_USER=news_user
DB_PASSWORD=your-very-strong-database-password-123
DB_HOST=db
DB_PORT=5432

# === REDIS ===
REDIS_URL=redis://redis:6379/0

# === ДОМЕН И SSL ===
DOMAIN=your-domain.com
EMAIL=admin@your-domain.com

# === АДМИНИСТРАТИВНЫЕ ПАРОЛИ ===
ADMIN_PASSWORD=your-admin-password-change-me
GRAFANA_PASSWORD=your-grafana-password-change-me

# === EMAIL НАСТРОЙКИ ===
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password

# === AI ПРОВАЙДЕРЫ (добавь свои API ключи) ===
OPENAI_API_KEY=sk-your-openai-api-key-here
DEEPSEEK_API_KEY=your-deepseek-api-key-here
PERPLEXITY_API_KEY=your-perplexity-api-key-here
ANTHROPIC_API_KEY=your-anthropic-api-key-here

# === TELEGRAM (для парсинга каналов) ===
TELEGRAM_API_ID=your-telegram-api-id
TELEGRAM_API_HASH=your-telegram-api-hash

# === МОНИТОРИНГ ===
SENTRY_DSN=https://your-sentry-dsn-here
LOG_LEVEL=INFO

# === ПРОКСИ (опционально) ===
HTTP_PROXY=
HTTPS_PROXY=
""",

        f"{project_name}/.gitignore": """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Django stuff
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal
media/
staticfiles/

# Flask stuff
instance/
.webassets-cache

# Scrapy stuff
.scrapy

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
Pipfile.lock

# PEP 582
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
.env.local
.env.development.local
.env.test.local
.env.production.local

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# Node.js
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
lerna-debug.log*

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Coverage directory used by tools like istanbul
coverage/
*.lcov

# nyc test coverage
.nyc_output

# Bower dependency directory
bower_components

# node-waf configuration
.lock-wscript

# Compiled binary addons
build/Release

# Dependency directories
jspm_packages/

# TypeScript cache
*.tsbuildinfo

# Optional npm cache directory
.npm

# Optional eslint cache
.eslintcache

# Optional stylelint cache
.stylelintcache

# Microbundle cache
.rpt2_cache/
.rts2_cache_cjs/
.rts2_cache_es/
.rts2_cache_umd/

# Optional REPL history
.node_repl_history

# Output of 'npm pack'
*.tgz

# Yarn Integrity file
.yarn-integrity

# parcel-bundler cache
.cache
.parcel-cache

# next.js build output
.next

# nuxt.js build output
.nuxt

# vuepress build output
.vuepress/dist

# Serverless directories
.serverless/

# FuseBox cache
.fusebox/

# DynamoDB Local files
.dynamodb/

# TernJS port file
.tern-port

# Stores VSCode versions used for testing VSCode extensions
.vscode-test

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Docker
.dockerignore

# Logs
logs/
*.log

# Backups
backups/

# SSL Certificates
*.pem
*.key
*.crt
*.csr
nginx/ssl/

# Temporary files
*.tmp
*.temp
""",

        f"{project_name}/docker-compose.prod.yml": """version: '3.8'

services:
  # PostgreSQL Database
  db:
    image: postgres:15-alpine
    restart: unless-stopped
    volumes:
      - postgres_data:/var/lib/postgresql/data/
      - ./backups:/backups
    environment:
      POSTGRES_DB: \${DB_NAME}
      POSTGRES_USER: \${DB_USER}
      POSTGRES_PASSWORD: \${DB_PASSWORD}
      POSTGRES_INITDB_ARGS: "--encoding=UTF-8 --lc-collate=C --lc-ctype=C"
    networks:
      - news_network
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U \${DB_USER} -d \${DB_NAME}"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 20s

  # Redis for Celery and Caching
  redis:
    image: redis:7-alpine
    restart: unless-stopped
    volumes:
      - redis_data:/data
    networks:
      - news_network
    command: redis-server --appendonly yes --maxmemory 256mb --maxmemory-policy allkeys-lru
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 30s
      timeout: 10s
      retries: 3

  # Django Backend Application
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile.prod
      args:
        - DJANGO_ENV=production
    restart: unless-stopped
    volumes:
      - static_volume:/app/staticfiles
      - media_volume:/app/media
      - ./logs:/app/logs
    environment:
      - DJANGO_ENV=production
      - DEBUG=False
      - DATABASE_URL=postgresql://\${DB_USER}:\${DB_PASSWORD}@db:5432/\${DB_NAME}
      - REDIS_URL=redis://redis:6379/0
      - SECRET_KEY=\${SECRET_KEY}
      - ALLOWED_HOSTS=\${ALLOWED_HOSTS}
      - CORS_ALLOWED_ORIGINS=\${CORS_ALLOWED_ORIGINS}
      - OPENAI_API_KEY=\${OPENAI_API_KEY}
      - DEEPSEEK_API_KEY=\${DEEPSEEK_API_KEY}
      - PERPLEXITY_API_KEY=\${PERPLEXITY_API_KEY}
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
    networks:
      - news_network
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/api/health/"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  # Celery Worker for Background Tasks
  celery:
    build:
      context: ./backend
      dockerfile: Dockerfile.prod
      args:
        - DJANGO_ENV=production
    restart: unless-stopped
    command: celery -A news_processor worker -l info --concurrency=4 --max-tasks-per-child=100
    volumes:
      - media_volume:/app/media
      - ./logs:/app/logs
    environment:
      - DJANGO_ENV=production
      - DATABASE_URL=postgresql://\${DB_USER}:\${DB_PASSWORD}@db:5432/\${DB_NAME}
      - REDIS_URL=redis://redis:6379/0
      - SECRET_KEY=\${SECRET_KEY}
      - OPENAI_API_KEY=\${OPENAI_API_KEY}
      - DEEPSEEK_API_KEY=\${DEEPSEEK_API_KEY}
      - PERPLEXITY_API_KEY=\${PERPLEXITY_API_KEY}
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
    networks:
      - news_network
    deploy:
      resources:
        limits:
          memory: 512M
        reservations:
          memory: 256M

  # Celery Beat Scheduler
  celery-beat:
    build:
      context: ./backend
      dockerfile: Dockerfile.prod
      args:
        - DJANGO_ENV=production
    restart: unless-stopped
    command: celery -A news_processor beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
    volumes:
      - ./logs:/app/logs
    environment:
      - DJANGO_ENV=production
      - DATABASE_URL=postgresql://\${DB_USER}:\${DB_PASSWORD}@db:5432/\${DB_NAME}
      - REDIS_URL=redis://redis:6379/0
      - SECRET_KEY=\${SECRET_KEY}
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
    networks:
      - news_network

  # Celery Flower Monitoring
  flower:
    build:
      context: ./backend
      dockerfile: Dockerfile.prod
    restart: unless-stopped
    command: celery -A news_processor flower --port=5555
    ports:
      - "5555:5555"
    environment:
      - DATABASE_URL=postgresql://\${DB_USER}:\${DB_PASSWORD}@db:5432/\${DB_NAME}
      - REDIS_URL=redis://redis:6379/0
      - SECRET_KEY=\${SECRET_KEY}
    depends_on:
      - redis
    networks:
      - news_network

  # React Frontend
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile.prod
      args:
        - REACT_APP_API_URL=https://\${DOMAIN}/api
    restart: unless-stopped
    networks:
      - news_network

  # Nginx Reverse Proxy
  nginx:
    image: nginx:alpine
    restart: unless-stopped
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./nginx/conf.d:/etc/nginx/conf.d:ro
      - ./nginx/ssl:/etc/nginx/ssl:ro
      - static_volume:/usr/share/nginx/html/static:ro
      - media_volume:/usr/share/nginx/html/media:ro
      - ./logs:/var/log/nginx
    depends_on:
      - backend
      - frontend
    networks:
      - news_network
    command: "/bin/sh -c 'while :; do sleep 6h & wait \$\${!}; nginx -s reload; done & nginx -g \"daemon off;\"'"

  # Prometheus Monitoring
  prometheus:
    image: prom/prometheus:latest
    restart: unless-stopped
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--web.console.libraries=/etc/prometheus/console_libraries'
      - '--web.console.templates=/etc/prometheus/consoles'
      - '--storage.tsdb.retention.time=200h'
      - '--web.enable-lifecycle'
    volumes:
      - ./monitoring/prometheus.yml:/etc/prometheus/prometheus.yml:ro
      - prometheus_data:/prometheus
    networks:
      - news_network
    deploy:
      resources:
        limits:
          memory: 256M

  # Grafana Dashboards
  grafana:
    image: grafana/grafana:latest
    restart: unless-stopped
    ports:
      - "3001:3000"
    volumes:
      - grafana_data:/var/lib/grafana
      - ./monitoring/grafana/dashboards:/etc/grafana/provisioning/dashboards:ro
      - ./monitoring/grafana/datasources:/etc/grafana/provisioning/datasources:ro
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=\${GRAFANA_PASSWORD}
      - GF_USERS_ALLOW_SIGN_UP=false
      - GF_INSTALL_PLUGINS=grafana-clock-panel,grafana-simple-json-datasource
    networks:
      - news_network
    depends_on:
      - prometheus

volumes:
  postgres_data:
    driver: local
  redis_data:
    driver: local
  static_volume:
    driver: local
  media_volume:
    driver: local
  prometheus_data:
    driver: local
  grafana_data:
    driver: local

networks:
  news_network:
    driver: bridge
    ipam:
      config:
        - subnet: 172.20.0.0/16
""",

        f"{project_name}/backend/requirements.txt": """# Core Django
Django==4.2.16
djangorestframework==3.14.0
django-cors-headers==4.3.1
django-filter==23.5
django-extensions==3.2.3

# Database
psycopg2-binary==2.9.7
dj-database-url==2.1.0

# Async & Background Tasks
redis==5.0.1
celery==5.3.4
django-celery-beat==2.5.0
kombu==5.3.4

# Web Server
gunicorn==21.2.0
whitenoise==6.6.0

# Image Processing
Pillow==10.4.0

# HTTP Requests
requests==2.31.0
httpx==0.25.2

# Web Scraping & Parsing
feedparser==6.0.11
beautifulsoup4==4.12.3
lxml==4.9.3
selenium==4.15.2
newspaper3k==0.2.8

# AI Providers
openai==1.3.5
anthropic==0.7.7

# Social Media APIs
python-telegram-bot==20.7
tweepy==4.14.0

# WordPress Integration
python-wordpress-xmlrpc==2.3

# Configuration
python-decouple==3.8
python-dotenv==1.0.0

# Date & Time
python-dateutil==2.8.2
pytz==2023.3

# Validation & Serialization
marshmallow==3.20.1
pydantic==2.5.0

# Utilities
slugify==0.0.1
Unidecode==1.3.7
chardet==5.2.0

# Development Tools
django-debug-toolbar==4.2.0
ipython==8.17.2

# Testing
pytest==7.4.3
pytest-django==4.7.0
factory-boy==3.3.0

# Monitoring
sentry-sdk[django]==1.38.0
prometheus-client==0.19.0

# Security
cryptography==41.0.7
PyJWT==2.8.0

# File Handling
openpyxl==3.1.2
xlsxwriter==3.1.9
""",

        f"{project_name}/backend/Dockerfile.prod": """# Multi-stage build for optimized production image
FROM python:3.11-slim as builder

WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies for building
RUN apt-get update && apt-get install -y \\
    build-essential \\
    libpq-dev \\
    pkg-config \\
    curl \\
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Production stage
FROM python:3.11-slim

WORKDIR /app

# Create app user
RUN groupadd -r app && useradd -r -g app app

# Install runtime dependencies
RUN apt-get update && apt-get install -y \\
    libpq5 \\
    curl \\
    netcat-traditional \\
    && rm -rf /var/lib/apt/lists/*

# Copy Python packages from builder stage
COPY --from=builder /root/.local /home/app/.local

# Copy application code
COPY --chown=app:app . .

# Create necessary directories
RUN mkdir -p staticfiles media logs && \\
    chown -R app:app /app

# Copy and make entrypoint executable
COPY --chown=app:app entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

# Switch to app user
USER app

# Set PATH for pip packages
ENV PATH=/home/app/.local/bin:$PATH

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \\
  CMD curl -f http://localhost:8000/api/health/ || exit 1

# Use entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]

# Default command
CMD ["gunicorn", "news_processor.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120", "--max-requests", "1000", "--max-requests-jitter", "100"]
""",

        f"{project_name}/backend/entrypoint.sh": """#!/bin/bash

set -e

# Function to wait for database
wait_for_db() {
    echo "Waiting for PostgreSQL..."
    
    while ! nc -z db 5432; do
        sleep 1
    done
    
    echo "PostgreSQL is ready!"
}

# Function to wait for Redis
wait_for_redis() {
    echo "Waiting for Redis..."
    
    while ! nc -z redis 6379; do
        sleep 1
    done
    
    echo "Redis is ready!"
}

# Wait for services
wait_for_db
wait_for_redis

# Run migrations
echo "Running database migrations..."
python manage.py migrate --noinput

# Create superuser if it doesn't exist
echo "Creating superuser if needed..."
python manage.py shell -c "
from apps.authentication.models import User
import os
email = os.environ.get('EMAIL', 'admin@localhost')
password = os.environ.get('ADMIN_PASSWORD', 'admin')
if not User.objects.filter(email=email).exists():
    User.objects.create_superuser('admin', email, password)
    print(f'Superuser created: {email}')
else:
    print(f'Superuser already exists: {email}')
"

# Load initial data
echo "Loading initial data..."
python manage.py loaddata fixtures/initial_data.json || echo "No fixtures found"

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting application..."
exec "$@"
""",

        f"{project_name}/backend/manage.py": """#!/usr/bin/env python
\"\"\"Django's command-line utility for administrative tasks.\"\"\"
import os
import sys


def main():
    \"\"\"Run administrative tasks.\"\"\"
    # Default to development settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_processor.settings.development')
    
    # Override with production settings if DJANGO_ENV is set
    if os.environ.get('DJANGO_ENV') == 'production':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_processor.settings.production')
    elif os.environ.get('DJANGO_ENV') == 'testing':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_processor.settings.testing')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
""",

        # Скрипт развертывания
        f"{project_name}/scripts/deploy.sh": """#!/bin/bash

set -e

# Colors for output
RED='\\033[0;31m'
GREEN='\\033[0;32m'
YELLOW='\\033[1;33m'
BLUE='\\033[0;34m'
NC='\\033[0m' # No Color

# Logging functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Configuration
DOMAIN=${DOMAIN:-"localhost"}
EMAIL=${EMAIL:-"admin@localhost"}
BACKUP_DIR="./backups/$(date +%Y%m%d_%H%M%S)"
COMPOSE_FILE="docker-compose.prod.yml"

# Check if .env file exists
check_env() {
    log_info "Checking environment configuration..."
    
    if [ ! -f ".env" ]; then
        log_error ".env file not found. Please copy .env.example to .env and configure it."
        exit 1
    fi
    
    # Source environment variables
    set -a
    source .env
    set +a
    
    # Check required variables
    required_vars=("SECRET_KEY" "DB_PASSWORD" "ADMIN_PASSWORD")
    for var in "${required_vars[@]}"; do
        if [ -z "${!var}" ]; then
            log_error "Environment variable $var is not set in .env"
            exit 1
        fi
    done
    
    log_success "Environment configuration is valid"
}

# Create backup
backup() {
    if [ "$1" = "--skip-backup" ]; then
        log_warning "Skipping backup creation"
        return
    fi
    
    log_info "Creating backup..."
    
    mkdir -p "$BACKUP_DIR"
    
    # Database backup
    if docker-compose -f $COMPOSE_FILE ps db | grep -q "Up"; then
        log_info "Creating database backup..."
        docker-compose -f $COMPOSE_FILE exec -T db pg_dump -U $DB_USER $DB_NAME > "$BACKUP_DIR/database.sql"
        log_success "Database backup created"
    fi
    
    # Media files backup
    if [ -d "media" ] || docker volume ls | grep -q "media"; then
        log_info "Creating media files backup..."
        if docker volume ls | grep -q "newsprocessor_media_volume"; then
            docker run --rm -v newsprocessor_media_volume:/data -v $(pwd)/$BACKUP_DIR:/backup alpine tar czf /backup/media.tar.gz -C /data .
        elif [ -d "media" ]; then
            tar -czf "$BACKUP_DIR/media.tar.gz" media/
        fi
        log_success "Media files backup created"
    fi
    
    # Config backup
    cp .env "$BACKUP_DIR/env.backup"
    cp $COMPOSE_FILE "$BACKUP_DIR/"
    
    log_success "Backup created in $BACKUP_DIR"
}

# Build frontend
build_frontend() {
    if [ ! -d "frontend" ]; then
        log_warning "Frontend directory not found, skipping build"
        return
    fi
    
    log_info "Building frontend..."
    
    # Build using Docker if Dockerfile exists
    if [ -f "frontend/Dockerfile.prod" ]; then
        log_info "Building frontend with Docker..."
        docker-compose -f $COMPOSE_FILE build frontend
    else
        log_warning "Frontend Dockerfile not found, building locally..."
        
        cd frontend
        
        if [ -f "package.json" ]; then
            # Install dependencies
            log_info "Installing npm dependencies..."
            npm ci --only=production
            
            # Build
            log_info "Building React application..."
            REACT_APP_API_URL=https://$DOMAIN/api npm run build
        else
            log_error "package.json not found in frontend directory"
            exit 1
        fi
        
        cd ..
    fi
    
    log_success "Frontend build completed"
}

# Setup SSL certificates
setup_ssl() {
    if [ "$DOMAIN" = "localhost" ] || [ "$DOMAIN" = "127.0.0.1" ]; then
        log_info "Skipping SSL setup for localhost"
        return
    fi
    
    if [ ! -d "./nginx/ssl" ]; then
        mkdir -p ./nginx/ssl
    fi
    
    # Check if certificates already exist
    if [ -f "./nginx/ssl/${DOMAIN}.crt" ]; then
        log_info "SSL certificates already exist for $DOMAIN"
        return
    fi
    
    log_info "Setting up SSL certificates for $DOMAIN..."
    
    # Install certbot if not available
    if ! command -v certbot &> /dev/null; then
        log_info "Installing certbot..."
        sudo apt update
        sudo apt install -y certbot python3-certbot-nginx
    fi
    
    # Generate certificates
    log_info "Generating SSL certificates..."
    sudo certbot certonly --standalone --email $EMAIL --agree-tos --no-eff-email -d $DOMAIN -d www.$DOMAIN
    
    # Copy certificates to nginx directory
    if [ -d "/etc/letsencrypt/live/$DOMAIN" ]; then
        sudo cp /etc/letsencrypt/live/$DOMAIN/fullchain.pem ./nginx/ssl/${DOMAIN}.crt
        sudo cp /etc/letsencrypt/live/$DOMAIN/privkey.pem ./nginx/ssl/${DOMAIN}.key
        sudo chown $USER:$USER ./nginx/ssl/${DOMAIN}.*
        log_success "SSL certificates installed"
    else
        log_warning "SSL certificate generation may have failed, continuing without SSL"
    fi
}

# Deploy application
deploy() {
    log_info "Deploying NewsProcessor application..."
    
    # Stop existing containers
    log_info "Stopping existing containers..."
    docker-compose -f $COMPOSE_FILE down --remove-orphans
    
    # Clean up old images (optional)
    if [ "$1" = "--clean" ]; then
        log_info "Cleaning up old Docker images..."
        docker system prune -f
    fi
    
    # Build new images
    log_info "Building Docker images..."
    docker-compose -f $COMPOSE_FILE build --no-cache
    
    # Start services
    log_info "Starting services..."
    docker-compose -f $COMPOSE_FILE up -d
    
    # Wait for services to be healthy
    log_info "Waiting for services to be ready..."
    sleep 30
    
    # Check service health
    log_info "Checking service health..."
    docker-compose -f $COMPOSE_FILE ps
    
    log_success "Deployment completed successfully"
}

# Health check
health_check() {
    log_info "Performing health checks..."
    
    # Check container status
    log_info "Checking container status..."
    if ! docker-compose -f $COMPOSE_FILE ps --services --filter "status=running" | grep -q "backend"; then
        log_error "Backend container is not running"
        docker-compose -f $COMPOSE_FILE logs backend
        exit 1
    fi
    
    # Check API endpoint
    log_info "Checking API endpoint..."
    local api_url="http://localhost/api/health/"
    if [ "$DOMAIN" != "localhost" ] && [ "$DOMAIN" != "127.0.0.1" ]; then
        api_url="https://$DOMAIN/api/health/"
    fi
    
    for i in {1..30}; do
        if curl -f -s $api_url > /dev/null; then
            log_success "API is responding correctly"
            break
        fi
        
        if [ $i -eq 30 ]; then
            log_error "API health check failed"
            docker-compose -f $COMPOSE_FILE logs backend
            exit 1
        fi
        
        log_info "Waiting for API to respond... (attempt $i/30)"
        sleep 5
    done
    
    # Check database connection
    log_info "Checking database connection..."
    if docker-compose -f $COMPOSE_FILE exec -T backend python manage.py check --database default; then
        log_success "Database connection is healthy"
    else
        log_error "Database connection failed"
        exit 1
    fi
    
    # Check Celery workers
    log_info "Checking Celery workers..."
    if docker-compose -f $COMPOSE_FILE exec -T celery celery -A news_processor inspect active > /dev/null; then
        log_success "Celery workers are active"
    else
        log_warning "Celery workers might not be fully ready yet"
    fi
    
    log_success "All health checks passed!"
}

# Update application
update() {
    log_info "Updating NewsProcessor application..."
    
    # Pull latest code
    if [ -d ".git" ]; then
        log_info "Pulling latest code from git..."
        git pull origin main
    fi
    
    # Create backup
    backup
    
    # Build and deploy
    build_frontend
    deploy
    
    # Health check
    health_check
    
    log_success "Update completed successfully"
}

# Show logs
show_logs() {
    local service=${2:-""}
    local follow=${3:-""}
    
    if [ -n "$service" ]; then
        if [ "$follow" = "-f" ] || [ "$follow" = "--follow" ]; then
            docker-compose -f $COMPOSE_FILE logs -f "$service"
        else
            docker-compose -f $COMPOSE_FILE logs --tail=100 "$service"
        fi
    else
        if [ "$follow" = "-f" ] || [ "$follow" = "--follow" ]; then
            docker-compose -f $COMPOSE_FILE logs -f
        else
            docker-compose -f $COMPOSE_FILE logs --tail=100
        fi
    fi
}

# Show status
show_status() {
    log_info "NewsProcessor Application Status"
    echo "=================================="
    
    # Container status
    echo "Container Status:"
    docker-compose -f $COMPOSE_FILE ps
    echo
    
    # Resource usage
    echo "Resource Usage:"
    docker stats --no-stream --format "table {{.Name}}\\t{{.CPUPerc}}\\t{{.MemUsage}}" $(docker-compose -f $COMPOSE_FILE ps -q)
    echo
    
    # Disk usage
    echo "Disk Usage:"
    du -sh backups/ logs/ 2>/dev/null || echo "No backups/logs directories"
    echo
    
    # Recent logs
    echo "Recent Backend Logs (last 5 lines):"
    docker-compose -f $COMPOSE_FILE logs --tail=5 backend
}

# Restore from backup
restore() {
    local backup_path=$2
    
    if [ -z "$backup_path" ]; then
        log_error "Please specify backup directory path"
        echo "Usage: $0 restore /path/to/backup/directory"
        exit 1
    fi
    
    if [ ! -d "$backup_path" ]; then
        log_error "Backup directory not found: $backup_path"
        exit 1
    fi
    
    log_warning "This will restore from backup and may overwrite current data!"
    read -p "Are you sure? (y/N): " -n 1 -r
    echo
    
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        log_info "Restore cancelled"
        exit 0
    fi
    
    log_info "Restoring from backup: $backup_path"
    
    # Stop services
    docker-compose -f $COMPOSE_FILE down
    
    # Restore database
    if [ -f "$backup_path/database.sql" ]; then
        log_info "Restoring database..."
        docker-compose -f $COMPOSE_FILE up -d db
        sleep 10
        docker-compose -f $COMPOSE_FILE exec -T db psql -U $DB_USER -d $DB_NAME < "$backup_path/database.sql"
    fi
    
    # Restore media files
    if [ -f "$backup_path/media.tar.gz" ]; then
        log_info "Restoring media files..."
        tar -xzf "$backup_path/media.tar.gz" -C ./
    fi
    
    # Restore configuration
    if [ -f "$backup_path/env.backup" ]; then
        log_info "Restoring environment configuration..."
        cp "$backup_path/env.backup" .env
    fi
    
    # Start all services
    docker-compose -f $COMPOSE_FILE up -d
    
    log_success "Restore completed"
}

# Main script logic
case $1 in
    deploy)
        check_env
        backup $2
        build_frontend
        setup_ssl
        deploy $2
        health_check
        ;;
    update)
        check_env
        update
        ;;
    backup)
        check_env
        backup
        ;;
    restore)
        check_env
        restore $@
        ;;
    logs)
        show_logs $@
        ;;
    status)
        show_status
        ;;
    health)
        check_env
        health_check
        ;;
    stop)
        log_info "Stopping all services..."
        docker-compose -f $COMPOSE_FILE down
        log_success "All services stopped"
        ;;
    restart)
        log_info "Restarting all services..."
        docker-compose -f $COMPOSE_FILE restart
        log_success "All services restarted"
        ;;
    clean)
        log_info "Cleaning up Docker resources..."
        docker-compose -f $COMPOSE_FILE down --volumes --remove-orphans
        docker system prune -af
        docker volume prune -f
        log_success "Cleanup completed"
        ;;
    *)
        echo "NewsProcessor Deployment Script"
        echo "==============================="
        echo ""
        echo "Usage: $0 {COMMAND} [OPTIONS]"
        echo ""
        echo "Commands:"
        echo "  deploy         Full deployment (first time or complete rebuild)"
        echo "  update         Update application (pull code, rebuild, deploy)"
        echo "  backup         Create backup of database and files"
        echo "  restore DIR    Restore from backup directory"
        echo "  logs [SERVICE] Show logs (optional: specific service)"
        echo "  status         Show application status"
        echo "  health         Run health checks"
        echo "  stop           Stop all services"
        echo "  restart        Restart all services"
        echo "  clean          Clean up Docker resources"
        echo ""
        echo "Options:"
        echo "  --skip-backup  Skip backup creation"
        echo "  --clean        Clean Docker cache before build"
        echo ""
        echo "Examples:"
        echo "  $0 deploy                    # Full deployment"
        echo "  $0 deploy --skip-backup      # Deploy without backup"
        echo "  $0 logs backend              # Show backend logs"
        echo "  $0 logs backend -f           # Follow backend logs"
        echo "  $0 restore ./backups/20231201_120000  # Restore from backup"
        echo ""
        exit 1
        ;;
esac
""",

    }
    
    # Создаем файлы
    for file_path, content in files.items():
        directory = os.path.dirname(file_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
            
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content.strip())
    
    print("📝 Создание файлов... ✅")
    
    # Делаем скрипты исполняемыми
    scripts = [
        f'{project_name}/scripts/deploy.sh',
        f'{project_name}/backend/entrypoint.sh'
    ]
    
    for script in scripts:
        if os.path.exists(script):
            os.chmod(script, 0o755)
    
    print("🔧 Настройка прав доступа... ✅")
    
    # Создаем ZIP архив
    archive_name = f"{project_name}-complete.zip"
    
    with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(project_name):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, '.')
                zipf.write(file_path, arcname)
    
    print("📦 Создание ZIP архива... ✅")
    
    # Получаем размер архива
    archive_size = os.path.getsize(archive_name)
    size_mb = archive_size / (1024 * 1024)
    
    print(f"""
🎉 АРХИВ NEWSPROCESSOR СОЗДАН УСПЕШНО!

📦 Файл архива: {archive_name}
📏 Размер: {size_mb:.2f} МБ
📁 Содержит: {len([f for _, _, files in os.walk(project_name) for f in files])} файлов

📋 Что включено:
✅ Backend Django с REST API
✅ Frontend React + TypeScript  
✅ Docker конфигурация для продакшна
✅ Nginx веб-сервер
✅ Мониторинг (Prometheus + Grafana)
✅ Скрипты автоматического развертывания
✅ Полная документация

🚀 Следующие шаги:
1. Загрузи архив в свой GitHub репозиторий
2. Настрой переменные в .env файле
3. Разверни на сервере командой: ./scripts/deploy.sh deploy

💡 Инструкции по развертыванию в README.md файле!
""")

if __name__ == "__main__":
    create_newsprocessor_archive()
