from candybar.CandyBarImage import CandyBarImage


class CandyBar128:
    PATTERN_128 = {
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

    PATTERN_128A = {
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

    PATTERN_128B = {
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

    DEFAULT_WIDTH = 400
    DEFAULT_HEIGHT = 60
    DEFAULT_SCALE = 1
    IMAGE_TYPE = 'PNG'
    QUIET_SPACE = 10

    # pattern_type = 'B'
    # bar_elements = []

    def __init__(self, contents=None, width=None, height=None, scale=None):
        self._contents = '' if contents is None else contents
        self._width = self.DEFAULT_WIDTH if width is None else width
        self._height = self.DEFAULT_HEIGHT if height is None else height
        self._scale = self.DEFAULT_SCALE if scale is None else scale
        self._mod_sum = 0

    def reset(self):
        self._mod_sum = 0

    def generate_barcode_with_contents(self, contents):
        self._contents = contents
        return self.generate_barcode()

    def generate_barcode(self):
        self.reset()
        mode = self._determine_mode(self._contents)
        bar_elements = self._create_bar_elements(self._contents, mode)
        image_byte_array = self._translate_to_image(bar_elements)
        return image_byte_array

    def _determine_mode(self, contents):
        mode = 'A'
        if len(contents) < 1:
            pass
        for c in contents:
            if mode == 'A' and self.TYPE_A_CHARSET.find(c) > -1:
                mode = 'A'
            elif self.TYPE_B_CHARSET.find(c) > -1:
                mode = 'B'
            else:
                pass
        return mode

    @staticmethod
    def get_module(weights):
        bar_elements = []
        i = 1
        for w in weights:
            bar_elements.append({'width': int(w), 'flip': (i % 2)})
            i += 1
        return bar_elements

    def _get_quiet(self):
        return {'width': self.QUIET_SPACE, 'flip': 0}

    def _get_pattern(self, mode, s):
        if mode == 'A':
            return self.PATTERN_128[self.PATTERN_128A[s]]
        elif mode == 'B':
            return self.PATTERN_128[self.PATTERN_128B[s]]
        else:
            return self.PATTERN_128[self.PATTERN_128B[s]]

    def _get_index(self, mode, s):
        if mode == 'A':
            return self.PATTERN_128A[s]
        elif mode == 'B':
            return self.PATTERN_128B[s]
        else:
            return self.PATTERN_128B[s]

    def _encode_module(self, mode, s, mw):
        pattern = self._get_pattern(mode, s)
        self._mod_sum += mw * self._get_index(mode, s)
        return self.get_module(pattern)

    def _get_mod(self):
        remainder = self._mod_sum % 103
        pattern = self.PATTERN_128[remainder]
        return self.get_module(pattern)

    def _create_bar_elements(self, contents, mode):
        bar_elements = [self._get_quiet()]
        bar_elements.extend(self._encode_module(mode, "Start", 1))
        i = 1
        for c in contents:
            bar_elements.extend(self._encode_module(mode, c, i))
            i += 1
        bar_elements.extend(self._get_mod())
        bar_elements.extend(self._encode_module(mode, "Stop", 1))
        bar_elements.append(self._get_quiet())
        return bar_elements

    def _translate_to_image(self, bar_elements):
        all_weights = 0
        for m in bar_elements:
            all_weights += m['width']
        si = CandyBarImage(all_weights, int(all_weights * 0.15))
        for m in bar_elements:
            pixels = int(m['width'] * self._scale)
            if m['flip'] == 1:
                si.add_bar(pixels)
            else:
                si.add_space(pixels)
        return si.scale_and_convert_to_byte_array(self._width, self._height)
