from sys import exit
from random import  randint
class Scene(object):
    '''场景'''
    def enter(self):
        print("this scene is not yet configured.subclass it and implement enter().")
        exit(1)


class Engine(object):
    '''引擎'''

    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene=self.scene_map.opening_scene()

        while True:
            print('\n-------')
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
    '''死亡'''
    quips= [
        "you died .you kinda suck at this你死了，你干得很烂",
        "your mom would be proud...ifshe were smarter你妈妈会为你感到骄傲的…她是聪明的",
        "such a luser",
        "i have a small puppy that's better at this.我有一只小狗，它更擅长这个"
    ]
    def enter(self):
        print(Death.quips[randint(0,len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):
    '''中央走廊'''

    def enter(self):
        print("the gothons of planet percal #25 have invaded your ship and destroyed第25号行星的恶魔入侵并摧毁了你的飞船")
        print("your entire crew. you are the last surviving member and your last全体船员。你是最后一个幸存的成员，也是最后一个")
        print("mission is to get the neutron destruct bomb from the weapons armory")
        action = input(">")
        if action == "shoot":
            print("quick on the draw you yank out your blaster and fire it at the gothon")
            print("you are dead .then he eats you")

            return 'death'
        elif action == "dodge!":
            print ("your head and eats you")
            return 'death'
        elif action == "tell a joke":
            print("you tell the one Gothon joke you know")
            return 'laser_weapon_armory'
        else:
            print("DOSE NOT COMPUTE")
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    '''激光武器库'''

    def enter(self):
        print("you do a dive roll into the weapon armory,crouch and scan the room")
        code = "%d%d%d"% (randint(1,9),randint(1,9),randint(1,9))
        guess = input("[keypad]>")
        guesses = 0

        while guess != code and guesses<10:
            print("BZZZEDDD")
            guesses += 1
            guess = input("[keypad]>")

        if guess == code:
            print("the container clicks open and the seal breaks.letting gas nebhaq gur ubhfr ")
            return 'the_bridge'
        else:
            print("the lock buzzes one last time and then you hear a ")
            return 'death'

class TheBridge(Scene):
    '''主控室'''
    def enter(self):
        pass

class EscapePod(Scene):
    '''救生舱'''
    def enter(self):
        pass

class Map(object):
    '''地图'''
    def __init__(self,start_scene):
        pass

    def next_scene(self,scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

