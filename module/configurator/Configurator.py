# coding:utf8
import pickle
import os


class Config:

    def __get__(self, instance, owner):
        return self

    def __set__(self, instance, value):
        self.value = value
        instance.config_flush(self.value)

    def __getitem__(self, key):
        return self.value[key]

    def __setitem__(self, key, value):
        self.value[key] = value
        self.value = self.value

    def __str__(self):
        return str(self.value)


class Configurator:
    config = Config()

    def __init__(self, file_path):
        self.file_path = file_path
        with open(file_path, 'rb') as f:
            self.config = pickle.load(f)

    def config_flush(self, value):
        with open(self.file_path, 'wb') as f:
            pickle.dump(value, f)


if __name__ == "__main__":
    c = Configurator('D:\\www\\python\\lessWords\\data\\config.pkl')
    print(c.config['MAJOR_DATA_PATH'])
