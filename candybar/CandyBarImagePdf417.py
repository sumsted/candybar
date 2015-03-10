import Image
import ImageDraw
import cStringIO

# TODO imaging works but looks a little wanky

class CandyBarImagePdf417:

    width = 120
    height = 500
    module_width = 2
    module_height = 6
    image_byte_array = []
    image_type = "PNG"
    current_x = 2
    current_y = 0
    image = None
    draw = None

    def __init__(self, columns, rows):
        self.width = (columns*17+1+4)*self.module_width
        self.height = rows * self.module_height
        self.setup()

    def setup(self):
        self.image = Image.new('RGBA', (self.width, self.height), 'white')
        self.draw = ImageDraw.Draw(self.image)

    def add_module(self, is_black):
        color = 'black' if is_black else 'white'
        d = (self.current_x, self.current_y,
             self.current_x + self.module_width, self.current_y + self.module_height)
        self.draw.rectangle(d, color)
        self.current_x += self.module_width

    def new_row(self):
        self.current_x = 2
        self.current_y += self.module_height


    def rescale(self, scaled_width, scaled_height):
        return self.image.resize((scaled_width, scaled_height), Image.NEAREST)

    def scale_and_convert_to_byte_array(self, scaled_width, scaled_height):
        return self._convert(self.rescale(scaled_width, scaled_height))

    def convert_to_byte_array(self):
        self.image_byte_array = self._convert(self.image)
        return self.image_byte_array

    def _convert(self, render_image):
        fp = cStringIO.StringIO()
        render_image.save(fp, self.image_type)
        iba = fp.getvalue()
        fp.close()
        return iba