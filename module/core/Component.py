# coding:utf8
class Name(str):
    def __init__(self, value='abandon'):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value
        # print(instance.my_dict.value)
        # exit()
        if not instance.my_dict.search(self.value):
            # crawling
            result = instance.spider.parse(value)
            # crawled
            if result['name'] != []:
                instance.my_dict.add_word(result)
            else:
                instance.name = 'abandon'
                return
        instance.interpretation = instance.my_dict.value[
            self.value]['interpretation']
        instance.example_sentences = instance.my_dict.value[
            self.value]['example_sentences']


class Interpretation:
    def __init__(self):
        self.value = None

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value


class ExampleSentences:
    def __init__(self):
        self.value = None

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value


class MyDict:
    def __init__(self, dataController):
        self.dataController = dataController
        self.value = self.dataController.read()
        if not isinstance(self.value, dict):
            self.value = dict()
            self.dataController.dict_flush(self.value)

    def search(self, word_name):
        result = None
        if word_name in self.value.keys():
            result = self.value[word_name]
        return result

    def add_word(self, word):
        self.value[word['name'][0]] = word
        self.dataController.dict_flush(self.value)


class Word:
    name = Name()
    interpretation = Interpretation()
    example_sentences = ExampleSentences()

    def __init__(self, my_dict, spider):
        self.my_dict = my_dict
        self.spider = spider
# class Word:
#     my_dict = MyDict()
#     name = Name()
#     interpretation = Interpretation()
#     example_sentences = ExampleSentences()

#     def __init__(self, manager,spider):
#         self.manager = manager
#         self.spider = spider
