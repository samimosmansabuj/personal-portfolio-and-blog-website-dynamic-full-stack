from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO
import os


def image_delete_os(picture):
    if picture and default_storage.exists(picture.name):
        default_storage.delete(picture.name)
        return True

def previous_image_delete_os(oldpicture, newpicture):
    if oldpicture and oldpicture != newpicture and default_storage.exists(oldpicture.name):
        default_storage.delete(oldpicture.name)
        return True

def compress_image(image_file, quality=90):
    img_temp = BytesIO()
    ext = os.path.splitext(image_file.name)[1].lower()
    if ext in ('.jpg', '.png', '.jpeg', '.webp'):
        with Image.open(image_file) as img:
            if img.mode not in ("RGB", "RGBA"):
                img = img.convert("RGB")

            base_name = os.path.splitext(image_file.name)[0]
            new_name = f"{base_name}.webp"
            
            img.save(img_temp, format="WEBP", quality=quality, optimize=True)
        img_temp.seek(0)
        return ContentFile(img_temp.read(), name=new_name)

