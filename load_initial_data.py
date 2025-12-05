import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'comida_al_paso.settings')
django.setup()

from django.core.management import call_command

print("🔄 Cargando datos iniciales...")

try:
    # Cargar categorías
    print("📂 Cargando categorías...")
    call_command('loaddata', 'fixtures/initial_data.json')
    print("✅ Categorías cargadas exitosamente")
    
    # Cargar productos
    print("🍔 Cargando productos...")
    call_command('loaddata', 'fixtures/productos_inicial.json')
    print("✅ Productos cargados exitosamente")
    
    print("\n🎉 ¡Todos los datos se cargaron correctamente!")
    
except Exception as e:
    print(f"❌ Error: {e}")