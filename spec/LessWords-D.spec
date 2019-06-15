# -*- mode: python -*-

block_cipher = None

ROOT_PATH = os.path.abspath(os.path.curdir)
ICONS_PATH = ROOT_PATH + os.path.sep + \
    'img' + os.path.sep + 'icons' + os.path.sep
EXEC_ICONS_PATH = 'img' + os.path.sep + 'icons' + os.path.sep

a = Analysis([ROOT_PATH + os.path.sep + 'LessWords.py'],
             pathex=[ROOT_PATH],
             binaries=[],
             datas=[(ICONS_PATH,EXEC_ICONS_PATH)],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='LessWords',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , 
          icon='img\\icons\\app.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='LessWords')
