import os
from module.initial.init import init, start

if __name__ == "__main__":
    if init():
        from module.access.access import main
        print(start)
        # exit()
        start(main)
