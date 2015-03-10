import Image
import ImageDraw
import cStringIO


class CandyBarImage:
    width = 400
    height = 60
    image_byte_array = []
    imageType = "PNG"
    currentPosition = 0
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
        d = (self.currentPosition, 0, self.currentPosition + bar_width, self.height + 1)
        self.draw.rectangle(d, 'black')
        self.currentPosition += bar_width

    def add_space(self, space_width):
        d = (self.currentPosition, 0, self.currentPosition + space_width, self.height + 1)
        self.draw.rectangle(d, 'white')
        self.currentPosition += space_width

    def rescale(self, scaled_width, scaled_height):
        return self.image.resize((scaled_width, scaled_height), Image.NEAREST)

    def scale_and_convert_to_byte_array(self, scaled_width, scaled_height):
        return self._convert(self.rescale(scaled_width, scaled_height))

    def convert_to_byte_array(self):
        self.image_byte_array = self._convert(self.image)
        return self.image_byte_array

    def _convert(self, render_image):
        fp = cStringIO.StringIO()
        render_image.save(fp, self.imageType)
        iba = fp.getvalue()
        fp.close()
        return iba