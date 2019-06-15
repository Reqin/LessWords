import os,shutil

ROOT_PATH = os.path.abspath(os.path.curdir)
ICONS_PATH = ROOT_PATH + os.path.sep + \
    'img' + os.path.sep + 'icons' + os.path.sep
EXEC_ICONS_PATH = ROOT_PATH + os.path.sep + 'dist' + os.path.sep + 'img' + os.path.sep + 'icons' + os.path.sep

command_line_D = 'pyinstaller spec/LessWords-D.spec'
command_line_F = 'pyinstaller LessWords.py -F -w -i img/icons/app.ico --specpath spec/'

flag = input('输入任意字符回车进行系统性安装，直接回车进行简易安装：')
if flag == '':
    os.system(command_line_F)
    try:
        shutil.copytree(ICONS_PATH,EXEC_ICONS_PATH)
    except FileExistsError:
        print('done')
else:
    os.system(command_line_D)