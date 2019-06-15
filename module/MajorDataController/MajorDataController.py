# coding:utf8
import pickle


class MajorDataController:
    def __init__(self,configurator):
        self.file_path = configurator.config['MAJOR_DATA_PATH']
        self.data = None

    def read(self):
        if self.data is None:
            with open(self.file_path,'rb') as f:
                self.data = pickle.load(f)
        return self.data

    def dict_flush(self, data):
        with open(self.file_path, 'wb') as f:
            pickle.dump(data,f)

if __name__ == "__main__":
    with open('D:\\www\\python\\lessWords\\data\\major.pkl','wb') as f:
        data = pickle.dump(None,f)
    with open('D:\\www\\python\\lessWords\\data\\major.pkl','rb') as f:
        data = pickle.load(f)
    print(data)