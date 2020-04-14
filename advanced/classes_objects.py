import random


class Enemy:
  atkl = 60
  atkh = 80
  # self is like "this" have reference of the enemy object and
  # you can access to its values
  def getAtk(self):
    print(self.atkl)

enemy1 = Enemy()
enemy1.getAtk()

enemy2 = Enemy()
enemy2.getAtk()