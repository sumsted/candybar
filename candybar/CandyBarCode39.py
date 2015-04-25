from candybar.CandyBarImage import CandyBarImage


class CandyBar39:
    START_STOP_PATTERN = "010010100"

    PATTERN_39 = {
        0: "000110100", 1: "100100001", 2: "001100001", 3: "101100000", 4: "000110001", 5: "100110000", 6: "001110000",
        7: "000100101", 8: "100100100", 9: "001100100",

        10: "100001001", 11: "001001001", 12: "101001000", 13: "000011001", 14: "100011000", 15: "001011000",
        16: "000001101", 17: "100001100", 18: "001001100", 19: "000011100",

        20: "100000011", 21: "001000011", 22: "101000010", 23: "000010011", 24: "100010010", 25: "001010010",
        26: "000000111", 27: "100000110", 28: "001000110", 29: "000010110",

        30: "110000001", 31: "011000001", 32: "111000000", 33: "010010001", 34: "110010000", 35: "011010000",
        36: "010000101", 37: "110000100", 38: "011000100",

        39: "010101000", 40: "010100010", 41: "010001010", 42: "000101010"
    }

    CODE_39_CHARACTERS = {
        "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0, "A": 10, "B": 11, "C": 12,
        "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18, "J": 19, "K": 20, "L": 21, "M": 22, "N": 23, "O": 24,
        "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29, "U": 30, "V": 31, "W": 32, "X": 33, "Y": 34, "Z": 35, "-": 36,
        ".": 37, " ": 38, "$": 39, "/": 40, "+": 41, "%": 42
    }

    DEFAULT_WIDTH = 400
    DEFAULT_HEIGHT = 60
    DEFAULT_SCALE = 1.0
    IMAGE_TYPE = 'PNG'
    QUIET_ZONE = 10

    def __init__(self, contents, width=None, height=None, scale=None):
        self._contents = contents
        self._width = self.DEFAULT_WIDTH if width is None else width
        self._height = self.DEFAULT_HEIGHT if height is None else height
        self._scale = self.DEFAULT_SCALE if scale is None else scale

    def _reset(self):
        self._contents = ''

    def generate_barcode_with_contents(self, contents):
        self._reset()
        self._contents = contents
        return self.generate_barcode()

    def generate_barcode(self):
        self._determine_type(self._contents)
        bar_elements = self._create_bar_elements(self._contents)
        image_byte_array = self._translate_to_image(bar_elements)
        return image_byte_array

    def _determine_type(self, contents):
        pass

    def _create_bar_elements(self, contents):
        bar_elements = [self.START_STOP_PATTERN]
        i = 1
        for c in contents:
            if c in self.CODE_39_CHARACTERS:
                bar_elements.append(self.PATTERN_39[self.CODE_39_CHARACTERS[c]])
            else:
                bar_elements.append(self.PATTERN_39[self.CODE_39_CHARACTERS['-']])
            i += 1
        bar_elements.append(self.START_STOP_PATTERN)
        return bar_elements

    def _translate_to_image(self, bar_elements):
        all_weights = self.QUIET_ZONE * 2
        for p in bar_elements:
            for m in p:
                all_weights += (int(m) + 1)
            all_weights += 1
        candy_bar_image = CandyBarImage(all_weights, int(all_weights * 0.15), self.IMAGE_TYPE)
        candy_bar_image.add_space(self.QUIET_ZONE * self._scale)
        for p in bar_elements:
            black = True
            for m in p:
                pixels = (int(m) + 1) * self._scale
                if black:
                    candy_bar_image.add_bar(pixels)
                else:
                    candy_bar_image.add_space(pixels)
                black = False if black else True
            candy_bar_image.add_space(1 * self._scale)
        image_byte_array = candy_bar_image.scale_and_convert_to_byte_array(self._width, self._height)
        return image_byte_array