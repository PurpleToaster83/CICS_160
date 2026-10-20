from colliding_object import colliding_object

class start(colliding_object):
    def __init__(self, image_fname:str, loc:tuple[int, int]=(0,0)):
        super().__init__(image_fname, loc)

    def on_collision(self, vehicle, rules):
        rules.start()