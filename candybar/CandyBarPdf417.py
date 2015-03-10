from candybar.CandyBarImagePdf417 import CandyBarImagePdf417
from candybar.PatternPdf417 import PatternPdf417

# TODO clean up into testable units

class CandyBarPdf417:
    DATA_CODE_WORD_COLUMNS = 3

    def __init__(self):
        pass

    def encode(self, contents):

        # high level encoding of contents
        contents_list = list(contents)
        current_mode = "UPP"
        if (len(contents_list) % 2) > 0:
            contents_list.append("T_PUN")
        code_words = []
        code_words.append(0)
        for i in xrange(0, len(contents_list), 2):
            value = PatternPdf417.get_code_word_value(contents_list[i], contents_list[i + 1])
            code_words.append(value)

        # calculate security level and cw length for error correction
        security_level = PatternPdf417.security_level(len(code_words))
        security_level_length = PatternPdf417.security_level_length(security_level)

        # calculate pad length and number of rows
        pad_length = self.DATA_CODE_WORD_COLUMNS - ((len(code_words) + security_level_length) %
                                                    self.DATA_CODE_WORD_COLUMNS)
        num_rows = (len(code_words) + security_level_length + pad_length) / self.DATA_CODE_WORD_COLUMNS
        code_words[0] = len(code_words) + pad_length

        # apply pad code words to data code words
        for i in xrange(pad_length):
            code_words.append(PatternPdf417.DATA_WORD_PAD)

        # generate error correction and apply to data code words
        for error_correction_code_word in PatternPdf417.error_correction(security_level, code_words):
            code_words.append(error_correction_code_word)

        # initialize grid
        low_level_grid = []
        code_word_index = 0
        for r in xrange(num_rows):
            low_level_grid.append([])
            low_level_grid[r].append(PatternPdf417.START_PATTERN)
            low_level_grid[r].append(PatternPdf417.get_pattern(r, PatternPdf417.get_left(security_level, r, num_rows,
                                                                                         self.DATA_CODE_WORD_COLUMNS)))
            for j in xrange(self.DATA_CODE_WORD_COLUMNS):
                low_level_grid[r].append(PatternPdf417.get_pattern(r, code_words[code_word_index]))
                code_word_index += 1
            low_level_grid[r].append(PatternPdf417.get_pattern(r, PatternPdf417.get_right(security_level, r, num_rows,
                                                                                          self.DATA_CODE_WORD_COLUMNS)))
            low_level_grid[r].append(PatternPdf417.STOP_PATTERN)

        # render
        image = CandyBarImagePdf417(self.DATA_CODE_WORD_COLUMNS + 4, num_rows)
        for i in xrange(num_rows):
            for j in xrange((4 + self.DATA_CODE_WORD_COLUMNS)):
                for module in list(low_level_grid[i][j]):
                    image.add_module(module == "1")
            image.new_row()
        return image.convert_to_byte_array()