from colliding_object import colliding_object

class pedestrian(colliding_object):
    def __init__(self, image_fname:str, loc:tuple[int, int]=(0,0)):
        self.hit = False
        super().__init__(image_fname, loc)

    def on_collision(self, vehicle, rules):
        # change the image and store that it has been hit
        if not(self.hit):
            self.hit = True
            self.change_image("images/added/blood.png")