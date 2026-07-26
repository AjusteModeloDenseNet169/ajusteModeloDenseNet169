import os

def renombrar_dataset_mangos():
    # --- CONFIGURACIÓN DIRECTA ---
    # Usamos r'' para que Windows reconozca las barras invertidas sin problemas
    ruta_carpeta = r'C:\Users\Cristina\OneDrive\Desktop\Mangos\Dataset-Mangos\Sanos'
    nuevo_nombre_base = 'sano'
    extensiones_validas = ('.jpg', '.jpeg', '.png', '.webp')

    # Verificar si la ruta existe
    if not os.path.exists(ruta_carpeta):
        print(f"Error: No se encontró la carpeta en: {ruta_carpeta}")
        return

    # Obtener lista de archivos y filtrar imágenes
    archivos = [f for f in os.listdir(ruta_carpeta) if f.lower().endswith(extensiones_validas)]
    
    # Ordenar para mantener consistencia
    archivos.sort()

    if not archivos:
        print("No se encontraron imágenes para renombrar.")
        return

    print(f"Iniciando el renombrado de {len(archivos)} imágenes...")

    for i, nombre_archivo in enumerate(archivos, start=1):
        extension = os.path.splitext(nombre_archivo)[1]
        
        # Formato: mango_sano_1.jpg, mango_sano_2.jpg...
        nuevo_nombre = f"{nuevo_nombre_base}_{i}{extension}"
        
        ruta_antigua = os.path.join(ruta_carpeta, nombre_archivo)
        ruta_nueva = os.path.join(ruta_carpeta, nuevo_nombre)

        try:
            os.rename(ruta_antigua, ruta_nueva)
            print(f"OK: {nombre_archivo} -> {nuevo_nombre}")
        except Exception as e:
            print(f"Error en {nombre_archivo}: {e}")

    print("\n✅ ¡Listo! Todas las imágenes han sido renombradas.")

if __name__ == "__main__":
    renombrar_dataset_mangos()