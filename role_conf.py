from img import gen_img_path

main_config = {
    'name': 'which',
    'width': 50,
    'height': 100,
    'can_move': False,
    'imgs': gen_img_path('which'),
    'click': 0,
    'x': 100,
    'y': 100,
    'hp': 10,
    'dead': False,
    'dmg': 0,
    'speed': 1000,
    'last_att': None,
    'att_tp': 'short',
    'mouse': None,
    'role': 'main',
    'monster': [],
    'img': None
}

death_config =  {
    'name': 'death',
    'width': 100,
    'height': 100,
    'can_move': False,
    'imgs': gen_img_path('death'),
    'click': 0,
    'x': 250,
    'y': 250,
    'hp': 10,
    'dead': False,
    'dmg': 0,
    'speed': 1000,
    'last_att': None,
    'att_tp': 'short',
    'mouse': None,
    'role': 'monster',
    'main': None,
    'img': None
}
