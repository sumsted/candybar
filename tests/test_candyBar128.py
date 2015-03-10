from unittest import TestCase
from candybar.CandyBarCode128 import CandyBar128


class TestCandyBar128(TestCase):
    def test_generate_barcode_with_contents(self):
        file_written = False
        cb128 = CandyBar128('', 400, 60)
        bc = cb128.generate_barcode_with_contents('bars are fun!')
        of = open('./test1.png', 'wb')
        for b in bc:
            of.write('%c' % b)
            file_written = True
        of.close()
        self.assertTrue(file_written, "Unable to generate barcode")

    def test_generate_barcode(self):
        file_written = False
        cb128 = CandyBar128('bars are super fun!', 400, 60)
        bc = cb128.generate_barcode()
        of = open('./test2.png', 'wb')
        for b in bc:
            of.write('%c' % b)
            file_written = True
        of.close()
        self.assertTrue(file_written, "Unable to generate barcode")
