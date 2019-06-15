# coding:utf8
import urllib.request as urq
from lxml import etree
from ISpider import ISpider

class BaidufanyiSpider(ISpider):
    def __init__(self, configurator):
        self.url_start = configurator.config['']

    def __get_url(self,word):
        return self.url_start + str(word)

    def __crawl(self,word):
        url = self.__get_url(word)
        return urq.urlopen(url).read().decode('utf8')

    def parse(self, word):
        xpath_rule = '//*[@id="left-result-container"]/div[1]/div/div[1]/div[1]/div[1]/h3'
        text = self.__crawl(word)
        htmlTree = etree.HTML(text)
        text = htmlTree.xpath(xpath_rule)
        print(text)
        exit

