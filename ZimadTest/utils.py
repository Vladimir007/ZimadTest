from io import BytesIO
from PIL import Image

from django.core.files import File


class CompressedImage(File):
    def __init__(self, file, name=None, max_width=300, max_height=200):
        self.src_fname = getattr(file, 'name', 'Image')
        super().__init__(self.__compressed(file, max_width, max_height), name=name)

    def __str__(self):
        return self.src_fname

    @staticmethod
    def __compressed(file, max_width, max_height):
        compressed = BytesIO()
        image = Image.open(file)
        image_fmt = image.format
        width, height = image.size
        new_size = (min(max_width, int(max_height * width / height)), max_height)
        image = image.resize(new_size, Image.ANTIALIAS)
        image.save(compressed, format=image_fmt, optimize=True, quality=95)
        compressed.seek(0)
        return compressed
