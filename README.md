# File Organizer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Versión: 1.0](https://img.shields.io/badge/Version-1.0-blue.svg)](./README.md)

**File Organizer** es un script en **Python** diseñado para organizar automáticamente archivos en carpetas según su tipo. Ideal para mantener tus directorios ordenados y facilitar la búsqueda de archivos.

## Características

- **Organización por tipo de archivo**:
  - Archivos de documentos (e.g., `doc`, `pdf`, `txt`).
  - Imágenes (e.g., `jpg`, `png`).
  - Videos (e.g., `mp4`).
  - Archivos comprimidos (e.g., `zip`, `rar`).
  - Otros tipos de archivos como `iso`, `exe`, y más.
- **Automatización completa**: Detecta y mueve los archivos a las carpetas correspondientes.
- **Configuración personalizable**: Fácil de adaptar a tus necesidades añadiendo nuevas categorías y extensiones.

## Requisitos

- **Python 3.6+**: Instalado en tu sistema.
- **Librerías estándar**: El script usa únicamente librerías estándar de Python (`os`, `shutil`, `glob`, etc.).

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/file-organizer.git
   cd file-organizer
   ```

2. Asegúrate de tener Python instalado. Puedes verificarlo con:
   ```bash
   python --version
   ```

3. El script está listo para usarse, no requiere instalación adicional.

## Uso

1. Ejecuta el script:
   ```bash
   python organize_files.py
   ```

2. Introduce la ruta de la carpeta que deseas organizar:
   - Ejemplo: `C:/Users/TuUsuario/Downloads`.

3. El script creará carpetas para cada tipo de archivo y moverá los archivos correspondientes.

### Ejemplo de Salida

```plaintext
##################################################
#                FILE ORGANIZER                  #
##################################################
¿Qué carpeta quieres ordenar?
> C:/Users/TuUsuario/Downloads

Archivos organizados correctamente.
```

### Personalización

Puedes modificar el mapeo de carpetas y extensiones directamente en el script, en la variable `file_mapping`. Por ejemplo, para añadir una categoría para archivos de audio:

```python
file_mapping = {
    "audio": ["mp3", "wav", "flac"],
    "documents": ["doc", "pdf", "txt"],
    # Otras categorías...
}
```

## Contribuciones

¡Contribuciones, reportes de errores y sugerencias son bienvenidos! Siéntete libre de abrir un _issue_ o enviar un _pull request_.

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](./LICENSE).

---

**Nota**: Este script es una herramienta simple y efectiva para organizar archivos. Se recomienda probarlo en carpetas con contenido no crítico para evitar errores inesperados.
