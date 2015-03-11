from unittest import TestCase
from candybar.CandyBarPdf417 import CandyBarPdf417

__author__ = 'scott'


class TestCandyBarPdf417(TestCase):
    def test_encode_alpha(self):
        file_written = False
        pdf417 = CandyBarPdf417()
        bc = pdf417.encode('BAR CODES ARE SUPER DUPER FUN')
        of = open('./test_pdf_417_1.png', 'wb')
        for b in bc:
            of.write('%c' % b)
            file_written = True
        of.close()
        self.assertTrue(file_written, "Unable to generate barcode")

    def test_encode_lower(self):
        file_written = False
        pdf417 = CandyBarPdf417()
        bc = pdf417.encode('bar codes are super duper fun')
        of = open('./test_pdf_417_2.png', 'wb')
        for b in bc:
            of.write('%c' % b)
            file_written = True
        of.close()
        self.assertTrue(file_written, "Unable to generate barcode")

    def test_encode_mixed(self):
        file_written = False
        pdf417 = CandyBarPdf417()
        bc = pdf417.encode('123 bars times 295 bars EQUALS 36285')
        of = open('./test_pdf_417_2.png', 'wb')
        for b in bc:
            of.write('%c' % b)
            file_written = True
        of.close()
        self.assertTrue(file_written, "Unable to generate barcode")

    def test_encode_punctuation(self):
        file_written = False
        pdf417 = CandyBarPdf417()
        bc = pdf417.encode('123 bars * 295 bars = 36,285')
        of = open('./test_pdf_417_3.png', 'wb')
        for b in bc:
            of.write('%c' % b)
            file_written = True
        of.close()
        self.assertTrue(file_written, "Unable to generate barcode")
