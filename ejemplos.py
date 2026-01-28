"""
Script de ejemplo para generar QRs programáticamente
Útil para generar múltiples QRs de forma automática
"""

from qr_generator import QRGenerator
from database import QRDatabase

def ejemplo_basico():
    """Genera un QR simple sin logo"""
    print("=== Ejemplo 1: QR Básico ===")
    
    qr_gen = QRGenerator()
    db = QRDatabase()
    
    url = "https://www.google.com"
    image_path = qr_gen.generate_qr(url)
    
    db.add_qr(url, image_path, notes="QR de ejemplo - Google")
    
    print(f"✓ QR generado: {image_path}")
    print()

def ejemplo_con_logo():
    """Genera un QR con logo"""
    print("=== Ejemplo 2: QR con Logo ===")
    
    qr_gen = QRGenerator()
    db = QRDatabase()
    
    url = "https://github.com"
    logo_path = "ruta/a/tu/logo.png"  # Cambia esto por tu logo
    
    # Verifica si el logo existe
    import os
    if os.path.exists(logo_path):
        image_path = qr_gen.generate_qr(url, logo_path)
        db.add_qr(url, image_path, logo_path, notes="QR con logo - GitHub")
        print(f"✓ QR con logo generado: {image_path}")
    else:
        print(f"✗ Logo no encontrado: {logo_path}")
        print("  Generando sin logo...")
        image_path = qr_gen.generate_qr(url)
        db.add_qr(url, image_path, notes="QR sin logo - GitHub")
        print(f"✓ QR generado: {image_path}")
    print()

def ejemplo_colores_personalizados():
    """Genera un QR con colores personalizados"""
    print("=== Ejemplo 3: QR con Colores Personalizados ===")
    
    qr_gen = QRGenerator()
    db = QRDatabase()
    
    url = "https://www.python.org"
    
    # Colores personalizados (azul sobre amarillo)
    image_path = qr_gen.generate_qr_with_custom_colors(
        url,
        fill_color="#1E40AF",  # Azul oscuro
        back_color="#FEF3C7"   # Amarillo claro
    )
    
    db.add_qr(url, image_path, notes="QR personalizado - Python")
    
    print(f"✓ QR con colores personalizados: {image_path}")
    print()

def ejemplo_batch():
    """Genera múltiples QRs de una lista"""
    print("=== Ejemplo 4: Generación en Lote ===")
    
    qr_gen = QRGenerator()
    db = QRDatabase()
    
    urls = [
        ("https://www.facebook.com", "Red Social - Facebook"),
        ("https://www.instagram.com", "Red Social - Instagram"),
        ("https://www.twitter.com", "Red Social - Twitter"),
        ("https://www.linkedin.com", "Red Social - LinkedIn"),
    ]
    
    for url, nota in urls:
        image_path = qr_gen.generate_qr(url)
        db.add_qr(url, image_path, notes=nota)
        print(f"✓ {nota}: {image_path}")
    
    print(f"\n✓ Total: {len(urls)} QRs generados")
    print()

def ejemplo_estadisticas():
    """Muestra estadísticas de la base de datos"""
    print("=== Ejemplo 5: Estadísticas ===")
    
    db = QRDatabase()
    stats = db.get_stats()
    
    print(f"Total de QRs generados: {stats['total']}")
    print(f"URLs únicas: {stats['unique_urls']}")
    print()
    
    # Mostrar últimos 5 QRs
    print("Últimos 5 QRs generados:")
    records = db.get_all_qrs(limit=5)
    
    for i, record in enumerate(records, 1):
        qr_id, url, logo_path, image_path, created_at, notes = record
        print(f"\n{i}. {url}")
        print(f"   Fecha: {created_at}")
        if notes:
            print(f"   Nota: {notes}")
        if logo_path:
            print(f"   Con logo: ✓")

def ejemplo_busqueda():
    """Busca QRs en la base de datos"""
    print("=== Ejemplo 6: Búsqueda ===")
    
    db = QRDatabase()
    
    search_term = "google"  # Cambia esto por tu término de búsqueda
    results = db.search_qrs(search_term)
    
    print(f"Resultados para '{search_term}': {len(results)}")
    
    for i, record in enumerate(results, 1):
        qr_id, url, logo_path, image_path, created_at, notes = record
        print(f"\n{i}. {url}")
        print(f"   Fecha: {created_at}")
        if notes:
            print(f"   Nota: {notes}")

def menu_principal():
    """Menú interactivo para ejecutar ejemplos"""
    print("\n" + "="*50)
    print("  EJEMPLOS DE USO - QR Generator Pro")
    print("="*50)
    print("\nSelecciona un ejemplo para ejecutar:")
    print("\n1. QR Básico")
    print("2. QR con Logo")
    print("3. QR con Colores Personalizados")
    print("4. Generación en Lote")
    print("5. Ver Estadísticas")
    print("6. Buscar QRs")
    print("7. Ejecutar Todos los Ejemplos")
    print("0. Salir")
    print("\n" + "="*50)
    
    opcion = input("\nOpción: ").strip()
    
    if opcion == "1":
        ejemplo_basico()
    elif opcion == "2":
        ejemplo_con_logo()
    elif opcion == "3":
        ejemplo_colores_personalizados()
    elif opcion == "4":
        ejemplo_batch()
    elif opcion == "5":
        ejemplo_estadisticas()
    elif opcion == "6":
        ejemplo_busqueda()
    elif opcion == "7":
        ejemplo_basico()
        ejemplo_con_logo()
        ejemplo_colores_personalizados()
        ejemplo_batch()
        ejemplo_estadisticas()
    elif opcion == "0":
        print("\n¡Hasta luego! 👋\n")
        return
    else:
        print("\n❌ Opción no válida\n")
    
    input("\nPresiona Enter para continuar...")
    menu_principal()

if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\n¡Hasta luego! 👋\n")
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
