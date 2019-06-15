# coding:utf8
from module.core.Component import MyDict, Word
from module.MajorDataController.MajorDataController import MajorDataController
from module.spider.YoudaofanyiSpider import YoudaofanyiSpider
from module.configurator.Configurator import Configurator
from module.window.MyGUI import MyGUI
from module.initial.init import init, CONFIG_PATH


class Processor:
    configurator = Configurator(CONFIG_PATH)
    majorDataController = MajorDataController(configurator)
    spider = YoudaofanyiSpider(configurator)
    myDict = MyDict(majorDataController)
    word = Word(myDict, spider)

    def __init__(self):
        self.word.name = self.word.name

    def get_word(self, name):
        self.word.name = name


def main():
    p = Processor()
    MyGUI(p)

