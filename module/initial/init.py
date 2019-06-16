# -*- coding: UTF-8 -*-
import os, sys
import pickle

ROOT_PATH = os.path.abspath(os.path.curdir)
START_LOCK_PATH = ROOT_PATH + os.path.sep + 'start.lock'
DATA_PATH = ROOT_PATH + os.path.sep + 'data' + os.path.sep
CONFIG_PATH = DATA_PATH + 'config.pkl'
MAJOR_DATA_PATH = DATA_PATH + 'major.pkl'
ICONS_PATH = ROOT_PATH + os.path.sep + \
             'img' + os.path.sep + 'icons' + os.path.sep

def log(info):
    print(info)


def before_start(func):
    if os.path.exists(START_LOCK_PATH):
        info = 'It seems that the program was not shut down correctly last time. You may need to delete the `start. lock` file in the root directory manually before you can run the program correctly.\nmaybe use\n `rm start.lock`'
        log(info)
        exit()
    else:
        try:
            with open(START_LOCK_PATH, 'w'):
                pass
        except Exception:
            log('start warning@' + START_LOCK_PATH)
    return func


def app_exit():
    try:
        os.remove(START_LOCK_PATH)
    except:
        log('lock file warning')
    return True


@before_start
def start(app_main_func):
    app_main_func()
    return app_exit()


def init(force=False):
    a = os.path.exists(DATA_PATH)
    b = os.path.exists(CONFIG_PATH)
    c = os.path.exists(MAJOR_DATA_PATH)
    if a and b and c and not force:
        return True
    config = {
        'ROOT_PATH': ROOT_PATH,
        'START_LOCK': START_LOCK_PATH,
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
        'ICONS': {
            'app': ICONS_PATH + 'app.ico',
            'search_0': ICONS_PATH + 'search_0.png',
            'fill_0': ICONS_PATH + 'fill_48x35_0.png',
            'go_pre_0': ICONS_PATH + 'go_previous_0.png',
            'go_next_0': ICONS_PATH + 'go_next_0.png'
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
