import hashlib
from unittest import TestCase
from candybar.CandyBarCode128 import CandyBar128


class TestCandyBar128(TestCase):

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
        cb128 = CandyBar128('', 400, 60)
        bs = cb128.generate_barcode_with_contents('bars are fun!')
        self.write_file('./test_code_128_1.png', bs)
        self.assertEqual("4a71dcae60be7c94a471167f931d8698981759d9b24c8fd9cd40d516",
                         self.sha2_check(bs),
                         "Unable to generate barcode")

    def test_generate_barcode(self):
        cb128 = CandyBar128('bars are super fun!', 400, 60)
        bs = cb128.generate_barcode()
        self.write_file('./test_code_128_2.png', bs)
        self.assertEqual("44794d5a206ef9d016ed926b0d8fc1bae68c783cb4ff37da3ccec085",
                         self.sha2_check(bs),
                         "Unable to generate barcode")
