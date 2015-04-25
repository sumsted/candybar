from PIL import Image
from PIL import ImageDraw
import io


class CandyBarImagePdf417:

    DEFAULT_WIDTH = 120
    DEFAULT_HEIGHT = 500
    MODULE_WIDTH = 2
    MODULE_HEIGHT = 6
    IMAGE_TYPE = "PNG"

    def __init__(self, columns, rows):
        self._width = (columns*17+1+4)*self.MODULE_WIDTH
        self._height = rows * self.MODULE_HEIGHT
        self._image_byte_array = []
        self._image = Image.new('RGBA', (self._width, self._height), 'white')
        self._draw = ImageDraw.Draw(self._image)
        self._current_x = 2
        self._current_y = 0

    def add_module(self, is_black):
        color = 'black' if is_black else 'white'
        d = (self._current_x, self._current_y,
             self._current_x + self.MODULE_WIDTH, self._current_y + self.MODULE_HEIGHT)
        self._draw.rectangle(d, color)
        self._current_x += self.MODULE_WIDTH

    def new_row(self):
        self._current_x = 2
        self._current_y += self.MODULE_HEIGHT

    def rescale(self, scaled_width, scaled_height):
        return self._image.resize((scaled_width, scaled_height), Image.NEAREST)

    def scale_and_convert_to_byte_array(self, scaled_width, scaled_height):
        return self._convert(self.rescale(scaled_width, scaled_height))

    def convert_to_byte_array(self):
        self._image_byte_array = self._convert(self._image)
        return self._image_byte_array

    def _convert(self, render_image):
        fp = io.BytesIO()
        render_image.save(fp, self.IMAGE_TYPE)
        iba = fp.getvalue()
        fp.close()
        return iba