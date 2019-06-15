from module.initial.init import init

if __name__ == "__main__":
    if init():
        from module.access.access import main
        main()
