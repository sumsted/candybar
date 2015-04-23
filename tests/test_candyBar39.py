import hashlib
from unittest import TestCase
from candybar.CandyBarCode39 import CandyBar39


class TestCandyBar39(TestCase):
    def test_generate_barcode_with_contents(self):
        self.fail()

    @staticmethod
    def sha2_check(bs):
        m = hashlib.sha224()
        for b in bs:
            m.update(b)
        print(m.hexdigest())
        return m.hexdigest()

    @staticmethod
    def write_file(file_name, bs):
        of = open(file_name, 'wb')
        for b in bs:
            of.write('%c' % b)
        of.close()

    def test_generate_barcode_with_contents(self):
        cb128 = CandyBar39('', 400, 60)
        bs = cb128.generate_barcode_with_contents('BARS ARE FUN!')
        self.write_file('./test_code_39_1.png', bs)
        # self.assertEqual("1810affbf4bb715df8281d8fd50a149530e5a16b39263b5b7682107a",
        #                  self.sha2_check(bs),
        #                  "Unable to generate barcode")

    def test_generate_barcode(self):
        cb128 = CandyBar39('BARS ARE SUPERFUN', 400, 60)
        bs = cb128.generate_barcode()
        self.write_file('./test_code_39_2.png', bs)
        # self.assertEqual("b8bbc79352c639d3f5ce9308062e2f2fbe22ed411dc080dd8607a561",
        #                  self.sha2_check(bs),
        #                  "Unable to generate barcode")
