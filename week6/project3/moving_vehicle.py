from colliding_object import colliding_object

class moving_vehicle(colliding_object):
    def __init__(self, image_fname:str, loc:tuple[int, int]=(0,0), controller=None):
        self.controller = controller
        super().__init__(image_fname, loc)
        self.can_move = True if controller else False
        self.crashed = False

    def set_location(self, loc:tuple[int, int]):
        super().set_location(loc)

    def move_vehicle(self, step):
        if self.can_move:
            pressedKeys = self.controller.arrow_pressed()
            cur_x, cur_y = self.loc
            new_heading = self.heading

            if pressedKeys["up"]:
                cur_y -= step
                new_heading = 90
            elif pressedKeys["down"]:
                cur_y += step
                new_heading = 270
            elif pressedKeys["left"]:
                cur_x -= step
                new_heading = 180
            elif pressedKeys["right"]:
                cur_x += step
                new_heading = 0

            self.set_location((cur_x, cur_y))

            if new_heading != self.heading:
                self.rotate_to(new_heading)

    def crash(self):
        self.crahsed = True

    def get_crashed(self):
        return self.crashed

    def freeze(self):
           self.can_move = False 