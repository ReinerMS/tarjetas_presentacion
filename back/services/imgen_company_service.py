import os
import shutil
from fastapi import UploadFile, HTTPException

UPLOAD_FOLDER = "imgs/company"
MAX_FILE_SIZE = 1 * 1024 * 1024  # Definir el tamaño máximo en bytes (1 MB)

async def save_image(file: UploadFile):
    # Validar si el archivo tiene la extensión correcta
    allowed_extensions = ["jpg", "jpeg", "png"]
    file_extension = file.filename.split(".")[-1].lower()  # Extraer la extensión del archivo

    if file_extension not in allowed_extensions:
        raise HTTPException(status_code=400, detail="Solo se permiten archivos con extensión .jpg, .jpeg o .png")

    # Leer el contenido del archivo para verificar su tamaño
    file_size = 0
    file_content = b""
    
    try:
        while True:
            chunk = await file.read(1024)  # Leer en bloques de 1 KB
            if not chunk:
                break
            file_content += chunk
            file_size += len(chunk)

            if file_size > MAX_FILE_SIZE:
                raise HTTPException(status_code=413, detail="El archivo es demasiado grande. Tamaño máximo permitido: 1 MB")

        # Definir la ruta donde se va a guardar la imagen
        file_location = os.path.join(UPLOAD_FOLDER, file.filename)

        # Guardar el archivo en la carpeta especificada
        with open(file_location, "wb") as buffer:
            buffer.write(file_content)

        return f"Archivo {file.filename} guardado correctamente en {file_location}"
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al guardar la imagen: {e}")