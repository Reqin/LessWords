# coding:utf8
from Component import *


class Procesor:
    my_dict = MyDict()
    word_line = WordLine(my_dict)

    def __init__(self, config):
        self.data_manager = LDController(config['DATA_FILE_MAJOR'])

    def search(self,word):
        pass