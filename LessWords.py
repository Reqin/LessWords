from module.initial.init import init, start
import sys
# sys.setdefaultencoding('utf8')

if __name__ == "__main__":
    if init(True):
        from module.access.access import main
        start(main)
