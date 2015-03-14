from unittest import TestCase
from candybar.CandyBarPdf417 import CandyBarPdf417
import hashlib
__author__ = 'scott'


class TestCandyBarPdf417(TestCase):

    @staticmethod
    def sha2_check(bs):
        m = hashlib.sha224()
        for b in bs:
            m.update(b)
        print m.hexdigest()
        return m.hexdigest()

    @staticmethod
    def write_file(file_name, bs):
        of = open(file_name, 'wb')
        for b in bs:
            of.write('%c' % b)
        of.close()

    def test_encode_phrase_alpha(self):
        pdf417 = CandyBarPdf417()
        bs = pdf417.encode('BAR CODES ARE SUPER DUPER FUN')
        self.write_file('./test_pdf_417_1.png', bs)
        self.assertEqual("e7597a4ceabe55beca7305621e270aae85583abc00e10c2baa2de7bb",
                         self.sha2_check(bs),
                         "Unable to generate barcode")

    def test_encode_phrase_lower(self):
        pdf417 = CandyBarPdf417()
        bs = pdf417.encode('bar codes are super duper fun')
        self.write_file('./test_pdf_417_2.png', bs)
        self.assertEqual("7da658234d8e9b65172689dd38ec1ab4fbc471e4a0dc38915350757b",
                         self.sha2_check(bs),
                         "Unable to generate barcode")

    def test_encode_phrase_mixed(self):
        pdf417 = CandyBarPdf417()
        bs = pdf417.encode('123 bars times 295 bars EQUALS 36285')
        self.write_file('./test_pdf_417_3.png', bs)
        self.assertEqual("65bf8a29d042b112c9808d0ba8f4317e8d9a041e05936730f4091816",
                         self.sha2_check(bs),
                         "Unable to generate barcode")

    def test_encode_phrase_punctuation(self):
        pdf417 = CandyBarPdf417()
        bs = pdf417.encode('123 bars * 295 bars = 36,285')
        self.write_file('./test_pdf_417_4.png', bs)
        self.assertEqual("cd4a350b67e4504e39a5da80f3345e46f1ddf62297d98fdc6d86456c",
                         self.sha2_check(bs),
                         "Unable to generate barcode")

    def test_encode_alpha(self):
        pdf417 = CandyBarPdf417()
        bs = pdf417.encode('ABCDEFGHIJKLMNOPQRSTUVWXYZ ')
        self.write_file('./test_pdf_417_5.png', bs)
        self.assertEqual("6b25f884f5e80674fcc88522359cc9dc8c815b1ada596996fbb67b4e",
                         self.sha2_check(bs),
                         "Unable to generate barcode")

    def test_encode_lower(self):
        pdf417 = CandyBarPdf417()
        bs = pdf417.encode('abcdefghijklomnopqrstuvwxyz')
        self.write_file('./test_pdf_417_6.png', bs)
        self.assertEqual("35b5586d7c53ae4248fd8393411d87c78b0a82e186172438a2bed52e",
                         self.sha2_check(bs),
                         "Unable to generate barcode")

    def test_encode_mixed(self):
        pdf417 = CandyBarPdf417()
        bs = pdf417.encode('0123456789&\r\t,:#-.$/+%*=^')
        self.write_file('./test_pdf_417_7.png', bs)
        self.assertEqual("7e627ed52493e8d45445cd9eff49137f7e43d6245b3d638fefa2297e",
                         self.sha2_check(bs),
                         "Unable to generate barcode")

    def test_encode_punctuation(self):
        pdf417 = CandyBarPdf417()
        bs = pdf417.encode(';<>@[\\]_`~!\r\t,:\n-.$/\"|*()?{}\'')
        self.write_file('./test_pdf_417_8.png', bs)
        self.assertEqual("4f82a98ec98dfa04b4432ba04ae665d75b772e17787d56d94d0479d1",
                         self.sha2_check(bs),
                         "Unable to generate barcode")

    def test_encode_transitions(self):
        pdf417 = CandyBarPdf417()
        bs = pdf417.encode('AaA0A;aAa0a;0A0a0;')
        self.write_file('./test_pdf_417_9.png', bs)
        self.assertEqual("7cda4b19ad2a40ae127b1e357c789d14228702cc437863eef77c2ec9",
                         self.sha2_check(bs),
                         "Unable to generate barcode")

