import os
import shutil
from collections import defaultdict

def create_directories(base_path, directories):
    """Crea las carpetas necesarias si no existen."""
    for folder in directories:
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)

def organize_files(base_path, file_mapping):
    """Organiza los archivos en sus respectivas carpetas."""
    for folder, extensions in file_mapping.items():
        for ext in extensions:
            for file in glob.glob(f"*.{ext}"):
                shutil.move(os.path.join(base_path, file), os.path.join(base_path, folder))

def main():
    print('\n' + '¦' * 50)
    print('¦', ' FILE ORGANIZER '.center(46), '¦')
    print('¦' * 50)

    path = input("¿Qué carpeta quieres ordenar?\n")
    if not os.path.isdir(path):
        print("La ruta proporcionada no es válida.")
        return

    os.chdir(path)

    # Mapeo de carpetas a extensiones
    file_mapping = {
        "documents": ["doc", "docx", "pdf", "txt", "rtf", "htm", "html", "epub"],
        "images": ["jpg", "jpeg", "png", "arw"],
        "videos": ["mp4"],
        "zip": ["zip", "rar"],
        "iso": ["iso", "img"],
        "exe": ["exe", "msi"],
        "bat": ["bat"],
        "varios": ["ltc"]
    }

    # Crear carpetas si no existen
    create_directories(path, file_mapping.keys())

    # Organizar archivos
    organize_files(path, file_mapping)

    print("Archivos organizados correctamente.")

if __name__ == "__main__":
    main()
