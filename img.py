import os

PWD = os.getcwd()
POST_FIX = ['att', 'std']
IMG_FOLD = 'img'

def gen_img_path(name):
    res = {}
    for attr in POST_FIX:
        _name = '_'.join([name, attr])
        path = os.path.join(PWD, IMG_FOLD, _name)
        res[attr] = path + '.jpg'
    return res

class ImgManager():

    def __init__(self):
        self.which = gen_img_path('which')
        self.death = gen_img_path('death')
