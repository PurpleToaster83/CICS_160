from colliding_object import colliding_object

class moving_vehicle(colliding_object):
    def __init__(self, image_fname:str, loc:tuple[int, int]=(0,0)):
        super().__init__(image_fname, loc)

    def set_location(self, loc:tuple[int, int]):
        self.loc = loc
        self.bounding_box.top_left = loc