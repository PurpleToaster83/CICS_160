class Player():
    def __init__(self, name, max_health, damage):
        self.name = name
        self.max_health = max_health
        self.curr_health = self.max_health
        self.damage = damage

    def take_damage(self, damage):
        self.curr_health -= damage

class Rogue(Player):
    def __init__(self, name, max_health, damage, dash_distance):
        super().__init__(name, max_health, damage)
        self.dash_distance = dash_distance

    def sneak_attack(self, distance_from_enemy, enemy):
        if distance_from_enemy <= self.dash_distance:
            enemy.take_damage(self.damage * 1.5)
        else:
            enemy.take_damage(self.damage)

    def __add__(self, rogue2):
        self.damage = self.damage + rogue2.damage
        self.curr_health = self.curr_health + rogue2.curr_health
        self.max_health = self.max_health + rogue2.max_health

class Potioneer(Player):
    def __init__(self, name, max_health, damage):
        super.__init__(name, max_health, damage)

    def throw_healing(self, target, heal_num):
        if (target.curr_health + heal_num > target.max_health):
            target.curr_health = target.max_health
        else:
            target.curr_health += heal_num

    def throw_strenght(self, target, strength_num):
        target.damage += strength_num
