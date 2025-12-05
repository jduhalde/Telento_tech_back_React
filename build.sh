#!/usr/bin/env bash
set -o errexit

echo "🔧 Instalando dependencias..."
pip install -r requirements.txt

echo "🗄️ Aplicando migraciones..."
python manage.py migrate --noinput

echo "📦 Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

echo "👤 Creando superusuario si no existe..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('✅ Superusuario creado: admin / admin123')
else:
    print('✅ Superusuario ya existe')
END

echo "📦 Cargando datos iniciales si no existen..."
python manage.py shell << END
from api.models import Producto
if Producto.objects.count() == 0:
    from django.core.management import call_command
    call_command('loaddata', 'fixtures/initial_data.json')
    call_command('loaddata', 'fixtures/productos_inicial.json')
    print('✅ Datos iniciales cargados')
else:
    print('✅ Ya existen productos en la base de datos')
END

echo "✅ Build completado!"