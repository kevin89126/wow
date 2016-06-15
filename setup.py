from setuptools import setup

APP = ['test.py']
DATA_FILES = ['./img/death_std.jpg', './img/death_att.jpg', './img/which_std.jpg', './img/which_att.jpg']
OPTIONS = {'argv_emulation': True}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
