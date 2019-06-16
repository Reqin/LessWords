# coding:utf8
import pickle


class MajorDataController:
    def __init__(self, configurator):
        self.file_path = configurator.config['MAJOR_DATA_PATH']
        self.data = None

    def read(self):
        if self.data is None:
            with open(self.file_path, 'rb') as f:
                self.data = pickle.load(f)
        return self.data

    def flush(self, data=dict()):
        self.data = data
        with open(self.file_path, 'wb') as f:
            pickle.dump(data, f)
        
