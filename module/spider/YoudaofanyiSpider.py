# coding:utf8
import urllib.request as urq
from lxml import etree
from module.spider.ISpider import ISpider


class YoudaofanyiSpider(ISpider):
    def __init__(self, configurator):
        self.config = configurator.config['SPIDER']['YOUDAOFANYI']

    def __cawl(self, word):
        url = self.config['URL_START'] + str(word)
        response = urq.urlopen(url).read().decode('utf8')
        return response

    def parse(self, word):
        r_tree = etree.HTML(self.__cawl(word))
        name = r_tree.xpath(self.config['XPATH_RULE']['name'])
        interpretation = r_tree.xpath(
            self.config['XPATH_RULE']['interpretation'])
        example_sentences = r_tree.xpath(self.config['XPATH_RULE']['example_sentences'])
        word_dict = {
            'name':name,
            'interpretation':interpretation,
            'example_sentences':example_sentences
        }
        return word_dict

if __name__ == "__main__":
    import sys
    sys.path.append('D:\\www\\python\\lessWords')
    from module.configurator.Configurator import Configurator
    c = Configurator('D:\\www\\python\\lessWords\\data\\config.pkl')
    s = YoudaofanyiSpider(c)
    print(s.parse('test'))