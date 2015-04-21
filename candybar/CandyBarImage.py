from PIL import Image
from PIL import ImageDraw
import io


class CandyBarImage:
    width = 400
    height = 60
    image_byte_array = []
    image_type = "PNG"
    current_position = 0
    image = None
    draw = None

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.setup()

    def setup(self):
        self.image = Image.new('RGBA', (self.width, self.height), 'white')
        self.draw = ImageDraw.Draw(self.image)

    def add_bar(self, bar_width):
        d = (self.current_position, 0, self.current_position + bar_width, self.height + 1)
        self.draw.rectangle(d, 'black')
        self.current_position += bar_width

    def add_space(self, space_width):
        d = (self.current_position, 0, self.current_position + space_width, self.height + 1)
        self.draw.rectangle(d, 'white')
        self.current_position += space_width

    def rescale(self, scaled_width, scaled_height):
        return self.image.resize((scaled_width, scaled_height), Image.NEAREST)

    def scale_and_convert_to_byte_array(self, scaled_width, scaled_height):
        return self._convert(self.rescale(scaled_width, scaled_height))

    def convert_to_byte_array(self):
        self.image_byte_array = self._convert(self.image)
        return self.image_byte_array

    def _convert(self, render_image):
        fp = io.BytesIO()
        render_image.save(fp, self.image_type)
        iba = fp.getvalue()
        fp.close()
        return iba