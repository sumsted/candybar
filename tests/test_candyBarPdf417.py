from unittest import TestCase
from candybar.CandyBarPdf417 import CandyBarPdf417

__author__ = 'scott'


class TestCandyBarPdf417(TestCase):
    def test_encode(self):
        file_written = False
        pdf417 = CandyBarPdf417()
        bc = pdf417.encode('BAR CODES ARE SUPER DUPER FUN')
        of = open('./test_pdf_417_1.png', 'wb')
        for b in bc:
            of.write('%c' % b)
            file_written = True
        of.close()
        self.assertTrue(file_written, "Unable to generate barcode")