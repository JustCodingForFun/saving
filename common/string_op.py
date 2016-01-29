import re

__author__ = 'Chris'


class StringOp:
    def __init__(self):
        pass

    @staticmethod
    def get_price(string):
        """
        :param string: **$xx.xx**
        :return: xx.xx
        """
        pl = re.findall('\d+\.\d+', string)
        return float(pl[0])
