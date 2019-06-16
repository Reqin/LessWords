import os
from module.initial.init import init, start

if __name__ == "__main__":
    if init():
        from module.access.access import main
        start(main)
