# coding:utf8
from abc import ABCMeta, abstractclassmethod, abstractmethod


class ISpider(metaclass=ABCMeta):
    @abstractclassmethod
    def parse(self, word):
        '''
        接收需要查询的单词，返回查询到单词的释义、例句等信息
        :return:
        '''
