#!/bin/bash

echo "=== INICIANDO DEPLOY DE LOGÍSTICA GLOBAL ==="

# 1. Actualizar sistema
echo "1. Actualizando sistema..."
sudo yum update -y

# 2. Instalar dependencias del sistema
echo "2. Instalando dependencias del sistema..."
sudo yum install -y python3-pip nginx

# 3. Verificar que PostgreSQL esté ejecutándose
echo "3. Verificando PostgreSQL..."
sudo systemctl enable postgresql
sudo systemctl start postgresql

# 4. Verificar que la base de datos exista
echo "4. Verificando base de datos..."
sudo -u postgres psql -c "\l" | grep logistica_db || sudo -u postgres psql -c "CREATE DATABASE logistica_db;"
sudo -u postgres psql -c "\du" | grep logistica_user || sudo -u postgres psql -c "CREATE USER logistica_user WITH PASSWORD 'maldonado4321';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE logistica_db TO logistica_user;"

# 5. Instalar dependencias de Python
echo "5. Instalando dependencias Python..."
cd /var/www/html/logistica
pip3 install -r requirements.txt

# 6. Configurar Nginx
echo "6. Configurando Nginx..."
sudo cp nginx.conf /etc/nginx/conf.d/logistica.conf
sudo systemctl enable nginx
sudo systemctl start nginx

# 7. Colectar archivos estáticos
echo "7. Colectando archivos estáticos..."
python3 manage.py collectstatic --noinput

# 8. Ejecutar migraciones
echo "8. Ejecutando migraciones..."
python3 manage.py migrate

# 9. Crear superusuario
echo "9. Creando superusuario..."
echo "from django.contrib.auth import get_user_model; User =