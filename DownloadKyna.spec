# -*- mode: python -*-

block_cipher = None

added_files = [('.\\ffmpeg', 'ffmpeg'), ('.\\logo', 'logo')]

a = Analysis(['DownloadKyna.py'],
             pathex=['E:\Language\Python\kyna\Download_Kyna'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='DownloadKyna',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True, icon='kyna.ico')
