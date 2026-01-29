from PIL import Image
import os

def convert_to_ico(png_path, ico_path):
    try:
        img = Image.open(png_path)
        # Asegurarnos de que sea cuadrada y de buen tamaño para un icono
        icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        img.save(ico_path, sizes=icon_sizes)
        print(f"Icono creado exitosamente en: {ico_path}")
    except Exception as e:
        print(f"Error al convertir icono: {e}")

if __name__ == "__main__":
    # La ruta de la imagen generada (proporcionada por la herramienta)
    source_png = r"C:/Users/aramirez/.gemini/antigravity/brain/917f0555-d0c6-4828-b463-5687a757d63c/qr_generator_icon_1769685709903.png"
    target_png = "app_icon.png"
    target_ico = "app_icon.ico"
    
    # También guardar una copia PNG en la carpeta del proyecto
    try:
        import shutil
        shutil.copy2(source_png, target_png)
        print(f"PNG guardado en: {target_png}")
        
        # Convertir a ICO
        convert_to_ico(target_png, target_ico)
    except Exception as e:
        print(f"Error: {e}")
