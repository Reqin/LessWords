# -*- coding: UTF-8 -*-
import os
import pickle

ROOT_PATH = os.path.abspath(os.path.curdir)
DATA_PATH = ROOT_PATH + os.path.sep + 'data' + os.path.sep
CONFIG_PATH = DATA_PATH + 'config.pkl'
MAJOR_DATA_PATH = DATA_PATH + 'major.pkl'
ICONS_PATH = ROOT_PATH + os.path.sep + \
    'img' + os.path.sep + 'icons' + os.path.sep


def init(force = False):
    a = os.path.exists(DATA_PATH)
    b = os.path.exists(CONFIG_PATH)
    c = os.path.exists(MAJOR_DATA_PATH)
    if a and b and c and not force:
        return True
    config = {
        'ROOT_PATH': ROOT_PATH,
        'DATA_PATH': DATA_PATH,
        'CONFIG_PATH': CONFIG_PATH,
        'MAJOR_DATA_PATH': MAJOR_DATA_PATH,
        'SPIDER': {
            'YOUDAOFANYI': {
                'URL_START': 'http://dict.youdao.com/w/',
                'XPATH_RULE': {
                    'name': '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/h2/span/text()',
                    'interpretation': '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/ul/li/text()',
                    'example_sentences': '//*[@class="examples"]/p/text()'
                }
            }
        },
        'ICONS':{
            'app': ICONS_PATH + 'app.ico',
            'search_0': ICONS_PATH + 'search_0.png',
            'fill_0': ICONS_PATH + 'fill_48x35_0.png',
            'go_pre_0':ICONS_PATH + 'go_previous_0.png',
            'go_next_0':ICONS_PATH + 'go_next_0.png'
        }
    }
    if not os.path.exists(DATA_PATH):
        os.mkdir(DATA_PATH)
    with open(MAJOR_DATA_PATH, 'wb') as f:
        pickle.dump(dict(), f)
    with open(CONFIG_PATH, 'wb') as f:
        pickle.dump(config, f)
    return True

if __name__ == "__main__":
    init(True)