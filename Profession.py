import random

class Profession:

    def __init__(self,nickname,health,damage,energy):
        self.nickname = nickname
        self.health = health
        self.damage = damage
        self.energy = energy

    def attack(self):
        if self.energy > 0:
            self.energy -= 2
            return random.randint(1,self.damage)
        else:
            print("You need to wait round to gain your energy back...")
            return 0

    def lost_hp(self,amount):
        self.health -= amount
        if self.health < 0:
            print(f'{self.nickname} died.')

    def __str__(self):
        return self.nickname

    def energy_regen(self):
        chance_to_regen = random.randint(1,3)
        if chance_to_regen == 2:
            return random.randint(1,4)
        else:
            print("You've got no luck today.")
            return 0


    def is_alive(self):
        if self.health <= 0:
            return False
        else:
            return True

