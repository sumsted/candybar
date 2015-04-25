from candybar.CandyBarImagePdf417 import CandyBarImagePdf417
from candybar.PatternPdf417 import PatternPdf417

# TODO clean up into testable units, fails class test - 2 methods and one is __init__() :P


class CandyBarPdf417:
    DATA_CODE_WORD_COLUMNS = 3

    def __init__(self):
        pass

    def encode(self, contents):

        # high level encoding of contents, including sub-mode transitions
        codes = []
        current_sub_mode = PatternPdf417.START_SUBMODE
        for c in list(contents):
            if c not in PatternPdf417.SUBMODE_MAP[current_sub_mode]:
                for check_sub_mode, charset in PatternPdf417.SUBMODE_MAP.items():
                    if c in charset and check_sub_mode != current_sub_mode:
                        for sub_mode, latch in PatternPdf417.SUBMODE_TRANSITIONS[current_sub_mode + "_" + check_sub_mode]:
                            codes.append(PatternPdf417.SUBMODE_MAP[sub_mode][latch])
                        current_sub_mode = check_sub_mode
            codes.append(PatternPdf417.SUBMODE_MAP[current_sub_mode][c])

        # round length to even
        if (len(codes) % 2) > 0:
            codes.append(PatternPdf417.CHARACTER_PAD)
        code_words = []
        # we'll store the cw length here after we calculate padding
        code_words.append(0)
        for i in range(0, len(codes), 2):
            value = PatternPdf417.get_code_word_value(codes[i], codes[i + 1])
            code_words.append(value)

        # calculate security level and cw length for error correction
        security_level = PatternPdf417.security_level(len(code_words))
        security_level_length = PatternPdf417.security_level_length(security_level)

        # calculate pad length and number of rows
        pad_length = self.DATA_CODE_WORD_COLUMNS - ((len(code_words) + security_level_length) %
                                                    self.DATA_CODE_WORD_COLUMNS)
        num_rows = (len(code_words) + security_level_length + pad_length) // self.DATA_CODE_WORD_COLUMNS
        code_words[0] = len(code_words) + pad_length

        # apply pad code words to data code words
        for i in range(pad_length):
            code_words.append(PatternPdf417.CODE_WORD_PAD)

        # generate error correction and apply to data code words
        for error_correction_code_word in PatternPdf417.error_correction(security_level, code_words):
            code_words.append(error_correction_code_word)

        # initialize grid
        pattern_grid = []
        code_word_index = 0
        for r in range(num_rows):
            pattern_grid.append([])
            pattern_grid[r].append(PatternPdf417.START_PATTERN)
            pattern_grid[r].append(PatternPdf417.get_pattern(r, PatternPdf417.get_left(security_level, r, num_rows,
                                                                                       self.DATA_CODE_WORD_COLUMNS)))
            for j in range(self.DATA_CODE_WORD_COLUMNS):
                pattern_grid[r].append(PatternPdf417.get_pattern(r, code_words[code_word_index]))
                code_word_index += 1
            pattern_grid[r].append(PatternPdf417.get_pattern(r, PatternPdf417.get_right(security_level, r, num_rows,
                                                                                        self.DATA_CODE_WORD_COLUMNS)))
            pattern_grid[r].append(PatternPdf417.STOP_PATTERN)

        # render
        image = CandyBarImagePdf417(self.DATA_CODE_WORD_COLUMNS + 4, num_rows)
        for i in range(num_rows):
            for j in range((4 + self.DATA_CODE_WORD_COLUMNS)):
                for module in list(pattern_grid[i][j]):
                    image.add_module(module == "1")
            image.new_row()
        return image.convert_to_byte_array()