from candybar.CandyBarImage import CandyBarImage


class CandyBar39:

    character_pad = "0"

    start_stop_pattern = "010011100"

    pattern_39 = {
        0: "000111100",
        1: "100100001",
        2: "001100001",
        3: "111100000",
        4: "000110001",
        5: "100110000",
        6: "001110000",
        7: "000100111",
        8: "100100100",
        9: "001100100",

        10: "100001001", # new row
        11: "001001001",
        12: "111001000",
        13: "000111001",
        14: "100011000",
        15: "001111000",
        16: "000001111",
        17: "100001100",
        18: "001001100",
        19: "000011100",

        20: "100000011", # new row
        21: "001000011",
        22: "111000010",
        23: "000010011",
        24: "100010010",
        25: "001110010",
        26: "000000111",
        27: "100000110",
        28: "001000110",
        29: "000011110",

        30: "110000001", # new row
        31: "011000001",
        32: "111000000",
        33: "010010001",
        34: "110010000",
        35: "011110000",
        36: "010000111",
        37: "110000100",
        38: "011000100",

        39: "010101000",
        40: "010100010",
        41: "010001010",
        42: "000101010",
    }

    code_39_characters = {
        "1" : 1,
        "2" : 2,
        "3" : 3,
        "4" : 4,
        "5" : 5,
        "6" : 6,
        "7" : 7,
        "8" : 8,
        "9" : 9,
        "0" : 0,
        "A" : 10,
        "B" : 11,
        "C" : 12,
        "D" : 13,
        "E" : 14,
        "F" : 15,
        "G" : 16,
        "H" : 17,
        "I" : 18,
        "J" : 19,
        "K" : 20,
        "L" : 21,
        "M" : 22,
        "N" : 23,
        "O" : 24,
        "P" : 25,
        "Q" : 26,
        "R" : 27,
        "S" : 28,
        "T" : 29,
        "U" : 30,
        "V" : 31,
        "W" : 32,
        "X" : 33,
        "Y" : 34,
        "Z" : 35,
        "-" : 36,
        "." : 37,
        " " : 38,
        "$" : 39,
        "/" : 40,
        "+" : 41,
        "%" : 42
    }

    contents = ''
    width = 400
    height = 60
    mod_sum = 0
    image_type = 'PNG'
    pattern_type = 'B'
    bar_elements = []
    image_byte_array = []
    quiet = 10

    def __init__(self, contents, width, height):
        self.contents = contents
        self.width = width
        self.height = height

    def reset(self):
        self.mod_sum = 0
        self.bar_elements = []
        self.image_byte_array = []

    def generate_barcode_with_contents(self, contents):
        self.contents = contents
        return self.generate_barcode()

    def generate_barcode(self):
        self.reset()
        self.determine_type()
        self.create_bar_elements()
        self.translate_to_image()
        return self.image_byte_array

    def determine_type(self):
        mode_type = 'A'
        if len(self.contents) < 1:
            pass
        for c in self.contents:
            if mode_type == 'A' and self.TYPE_A_CHARSET.find(c) > -1:
                mode_type = 'A'
            elif self.TYPE_B_CHARSET.find(c) > -1:
                mode_type = 'B'
            else:
                pass
        self.pattern_type = mode_type

    def add_module(self, weights):
        i = 1
        for w in weights:
            self.bar_elements.append({'width': int(w), 'flip': (i % 2)})
            i += 1

    def add_quiet(self):
        self.bar_elements.append({'width': self.quiet, 'flip': 0})

    def get_pattern(self, s):
        if self.pattern_type == 'A':
            return self.pattern_128[self.pattern_128A[s]]
        elif self.pattern_type == 'B':
            return self.pattern_128[self.pattern_128B[s]]
        else:
            return self.pattern_128[self.pattern_128B[s]]

    def get_index(self, s):
        if self.pattern_type == 'A':
            return self.pattern_128A[s]
        elif self.pattern_type == 'B':
            return self.pattern_128B[s]
        else:
            return self.pattern_128B[s]

    def encode_module(self, s, mw):
        pattern = self.get_pattern(s)
        self.add_module(pattern)
        self.mod_sum += mw * self.get_index(s)

    def add_mod(self):
        remainder = self.mod_sum % 103
        pattern = self.pattern_128[remainder]
        self.add_module(pattern)

    def create_bar_elements(self):
        self.add_quiet()
        self.encode_module("Start", 1)
        i = 1
        for c in self.contents:
            self.encode_module(c, i)
            i += 1
        self.add_mod()
        self.encode_module("Stop", 0)
        self.add_quiet()

    def translate_to_image(self):
        all_weights = 0
        for m in self.bar_elements:
            all_weights += m['width']
        si = CandyBarImage(all_weights, int(all_weights * 0.15))
        scale = 1.0
        for m in self.bar_elements:
            pixels = int(m['width'] * scale)
            if m['flip'] == 1:
                si.add_bar(pixels)
            else:
                si.add_space(pixels)

        self.image_byte_array = si.scale_and_convert_to_byte_array(self.width, self.height)
