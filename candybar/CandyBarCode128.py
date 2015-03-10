from CandyBarImage import CandyBarImage


class CandyBar128:
    pattern_128 = {
        0: "212222", 1: "222122", 2: "222221", 3: "121223", 4: "121322", 5: "131222", 6: "122213", 7: "122312",
        8: "132212", 9: "221213",
        10: "221312", 11: "231212", 12: "112232", 13: "122132", 14: "122231", 15: "113222", 16: "123122", 17: "123221",
        18: "223211", 19: "221132",
        20: "221231", 21: "213212", 22: "223112", 23: "312131", 24: "311222", 25: "321122", 26: "321221", 27: "312212",
        28: "322112", 29: "322211",
        30: "212123", 31: "212321", 32: "232121", 33: "111323", 34: "131123", 35: "131321", 36: "112313", 37: "132113",
        38: "132311", 39: "211313",
        40: "231113", 41: "231311", 42: "112133", 43: "112331", 44: "132131", 45: "113123", 46: "113321", 47: "133121",
        48: "313121", 49: "211331",
        50: "231131", 51: "213113", 52: "213311", 53: "213131", 54: "311123", 55: "311321", 56: "331121", 57: "312113",
        58: "312311", 59: "332111",
        60: "314111", 61: "221411", 62: "431111", 63: "111224", 64: "111422", 65: "121124", 66: "121421", 67: "141122",
        68: "141221", 69: "112214",
        70: "112412", 71: "122114", 72: "122411", 73: "142112", 74: "142211", 75: "241211", 76: "221114", 77: "413111",
        78: "241112", 79: "134111",
        80: "111242", 81: "121142", 82: "121241", 83: "114212", 84: "124112", 85: "124211", 86: "411212", 87: "421112",
        88: "421211", 89: "212141",
        90: "214121", 91: "412121", 92: "111143", 93: "111341", 94: "131141", 95: "114113", 96: "114311", 97: "411113",
        98: "411311", 99: "113141",
        100: "114131", 101: "311141", 102: "411131", 103: "211412", 104: "211214", 105: "211232", 106: "2331112",
        -1: "211133",
    }

    pattern_128A = {
        " ": 0, "!": 1, "\"": 2, "#": 3, "$": 4, "%": 5, "&": 6, "'": 7, "(": 8, ")": 9,
        "*": 10, "+": 11, ",": 12, "-": 13, ".": 14, "/": 15, "0": 16, "1": 17, "2": 18, "3": 19,
        "4": 20, "5": 21, "6": 22, "7": 23, "8": 24, "9": 25, ":": 26, ";": 27, "<": 28, "=": 29,
        ">": 30, "?": 31, "@": 32, "A": 33, "B": 34, "C": 35, "D": 36, "E": 37, "F": 38, "G": 39,
        "H": 40, "I": 41, "J": 42, "K": 43, "L": 44, "M": 45, "N": 46, "O": 47, "P": 48, "Q": 49,
        "R": 50, "S": 51, "T": 52, "U": 53, "V": 54, "W": 55, "X": 56, "Y": 57, "Z": 58, "[": 59,
        "\\": 60, "]": 61, "^": 62, "_": 63, "NUL": 64, "SOH": 65, "STX": 66, "ETX": 67, "EOT": 68, "ENQ": 69,
        "ACK": 70, "BEL": 71, "BS": 72, "HT": 73, "LF": 74, "VT": 75, "FF": 76, "CR": 77, "SO": 78, "SI": 79,
        "DLE": 80, "DC1": 81, "DC2": 82, "DC3": 83, "DC4": 84, "NAK": 85, "SYN": 86, "ETB": 87, "CAN": 88, "EM": 89,
        "SUB": 90, "ESC": 91, "FS": 92, "GS": 93, "RS": 94, "US": 95, "FNC 3": 96, "FNC 2": 97, "Shift B": 98,
        "Code C": 99,
        "Code B": 100, "FNC 4": 101, "FNC 1": 102, "Start": 103, "Stop": 106, "unused": 107,
    }

    pattern_128B = {
        " ": 0, "!": 1, "\"": 2, "#": 3, "$": 4, "%": 5, "&": 6, "'": 7, "(": 8, ")": 9,
        "*": 10, "+": 11, ",": 12, "-": 13, ".": 14, "/": 15, "0": 16, "1": 17, "2": 18, "3": 19,
        "4": 20, "5": 21, "6": 22, "7": 23, "8": 24, "9": 25, ":": 26, ";": 27, "<": 28, "=": 29,
        ">": 30, "?": 31, "@": 32, "A": 33, "B": 34, "C": 35, "D": 36, "E": 37, "F": 38, "G": 39,
        "H": 40, "I": 41, "J": 42, "K": 43, "L": 44, "M": 45, "N": 46, "O": 47, "P": 48, "Q": 49,
        "R": 50, "S": 51, "T": 52, "U": 53, "V": 54, "W": 55, "X": 56, "Y": 57, "Z": 58, "[": 59,
        "\\": 60, "]": 61, "^": 62, "_": 63, "`": 64, "a": 65, "b": 66, "c": 67, "d": 68, "e": 69,
        "f": 70, "g": 71, "h": 72, "i": 73, "j": 74, "k": 75, "l": 76, "m": 77, "n": 78, "o": 79,
        "p": 80, "q": 81, "r": 82, "s": 83, "t": 84, "u": 85, "v": 86, "w": 87, "x": 88, "y": 89,
        "z": 90, "{": 91, "|": 92, "}": 93, "~": 94, "DEL": 95, "FNC 3": 96, "FNC 2": 97, "Shift A": 98, "Code C": 99,
        "FNC4": 100, "Code A": 101, "FNC 1": 102, "Start": 104, "Stop": 106, "unused": 107,
    }

    TYPE_A_CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !\"#$%&'()*+,-./:;<=>?@[\\]^_"
    TYPE_B_CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !\"#$%&'()*+,-./:;<=>?@[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

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
