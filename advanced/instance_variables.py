import random


class Enemy:
    hp = 200  # static variable for each class instance
    # This function is called when we instantiate a class

    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print("atk low is", self.atkl)

    def getHp(self):
        print("HP is", self.hp)


enemy1 = Enemy(40, 49)
enemy1.getAtk()
enemy1.getHp()

enemy2 = Enemy(75, 90)
enemy2.getAtk()
enemy2.getHp()