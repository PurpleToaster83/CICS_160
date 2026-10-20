from colliding_object import colliding_object

class tree(colliding_object):
    def __init__(self, image_fname:str, loc:tuple[int, int]=(0,0)):
        super().__init__(image_fname, loc)

    def on_collision(self, vehicle, rules):
        # tell the vehicle that it crashed
        if not(vehicle.get_crashed()):
            vehicle.crash()