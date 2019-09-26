# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['create_word_cloud.py'],
             pathex=['C:\\Users\\Mystic\\Documents\\Python\\ChineseWordCloud'],
             binaries=[],
             datas=[('C:\\Users\\Mystic\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\site-packages\\wordcloud\\stopwords', 'wordcloud'),
			 ('C:\\Users\\Mystic\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\site-packages\\wordcloud\\DroidSansMono.ttf', 'wordcloud'),
			 ('C:\\Users\\Mystic\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\site-packages\\jieba\\dict.txt', 'jieba'),
			 ('C:\\Users\\Mystic\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\site-packages\\jieba\\analyse\\idf.txt', 'jieba\\analyse'),
			 ('fonts\\STFangSong.ttf','fonts')
			 ],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='create_word_cloud',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          icon='cloud.ico')
