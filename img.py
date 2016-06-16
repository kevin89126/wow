import os

PWD = os.getcwd()
POST_FIX = ['att', 'std']

def gen_img_path(name):
    res = {}
    for attr in POST_FIX:
        _name = '_'.join([name, attr])
        path = os.path.join(PWD, _name)
        res[attr] = path
    return res

class ImgManager():

    def __init__(self):
        which = gen_img_path('which')
        death = gen_img_path('death')
