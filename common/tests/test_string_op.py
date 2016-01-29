import unittest
from common.string_op import StringOp

__author__ = 'Chris'


class TestStringOp(unittest.TestCase):
    def test_get_price(self):
        string = '<font color="#CC0000">$399.98</font></b> if you buy today!</font>'
        self.assertTrue(399.98 == StringOp.get_price(string))
        string = '>$359.99</span></b></font>\xa0'
        price = StringOp.get_price(string)
        print price
        self.assertTrue(359.99 == price)
