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
            m.update(str(b).encode())
        print(m.hexdigest())
        return m.hexdigest()

    @staticmethod
    def write_file(file_name, bs):
        of = open(file_name, 'wb')
        of.write(bs)
        of.close()

    def test_generate_barcode_with_contents(self):
        cb39 = CandyBar39('', 400, 60)
        bs = cb39.generate_barcode_with_contents('BARS ARE FUN')
        self.write_file('./test3.png', bs)
        bs = cb39.generate_barcode_with_contents('ABCDEFG')
        self.write_file('./test_code_39_1.png', bs)
        bs = cb39.generate_barcode_with_contents('1234567890')
        self.write_file('./test_code_39_2.png', bs)
        bs = cb39.generate_barcode_with_contents('HIJKLMNOPQRSTU')
        self.write_file('./test_code_39_3.png', bs)
        bs = cb39.generate_barcode_with_contents('UVWXYZ-. $/+%')
        self.write_file('./test_code_39_4.png', bs)
