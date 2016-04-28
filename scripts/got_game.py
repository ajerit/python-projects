#
# Adolfo Jeritson
# Example of a adventure-type game with game of thrones
# 2015
#

from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print("This scene is not yet configured. Subclass it and implement enter().")
        exit(1)
	
	
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

		
class Death(Scene):

    quips = [
        "You died.  You lost the game of thrones.",
         "The Mad King is is a better player than you, shame.",
         "You shouldn't have trusted Littlefinger.",
         "See you in the seven hells."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        print("The Targaryen Dynasty is dead because of you.")
        print("Try again :(")
        exit(1)		
		
		
class ThroneHall(Scene):

    def enter(self):
        print("\n")
        print("The Rebellion has reached King's Landing. You must escape.")
        print("You're the last Targaryen alive, and you must scape the Red Keep.")
        print("Your mission is to get the wildfire from the Castle's Armory,")
        print("put it in the Small Council Room, and blow up the castle after getting into a")
        print("ship to the Free Cities.")
        print("\n")
        print("You're running down the Throne Hall to the Castle's Armory when")
        print("a Lannister soldier jumps out, scarlet red banner, with a golden lion and a sharp sword")
        print("pointing at you.  He's blocking the door to the")
        print("Armory and about to slay you with his sword.")

        action = input("[attack!/dodge!/run!]> ")

        if action == "attack!":
            print("\n")
            print("You quickly draw your Valyrian Steel Sword and attack the")
            print("Lannister soldier. He reacts faster and deflects your attack with his shield.")
            print("Some soldiers nearby hear the noise and surround you, you're out numbered.")
            print("You try to fight against them, but they are too much for you.")
            print("Then, The Mountain appears and slays you with his gigantic sword.")
            print("Thats all, the last Targaryen is dead.")
            return 'death'

        elif action == "dodge!":
            print("\n")
            print("Like a world class Braavosi you dodge, weave, slip and slide right")
            print("as the Lannister sword slide past your head and body.")
            print("In the middle of your artful dodge your foot slips and you")
            print("bang your head on one of the dragon skulls in the Hall. You pass out.")
            print("You wake up shortly after only to die as Robert Baratheon slays your head")
            print("in a public execution.")
            return 'death'

        elif action == "run!":
            print("\n")
            print("You dont think twice and start running through the castle. You know it by heart.")
            print("Lucky for you, the Lannister soldier has never been in the Red Keep.")
            print("After several minutes of going through secret passages, you've lost the soldier.")
            print("You now can take the secret corridor that ends in the Castle's Armory full of wildfire.")
            print("When you reach the door, you notice some bodies in the floor, but the fight was over,")
            print("the corridor is empty, and you go into the Armory.")
            return 'castle_armory'

        else:
            print("\n")
            print("IT IS NOT KNOWN!")
            return 'throne_hall'		
		
		
class CastleArmory(Scene):

    def enter(self):
        print("\n")
        print("You go in quietly into the Armory, knowing that there might be a soldier hiding.")
        print("But it's dead quiet, too quiet. Not even the other sounds of the castle can be heard.")
        print("You see the shelves full of wildfire behind a metal grid with an Ancient Valyrian security system.")
        print("The only way of opening it is getting right a combination of three numbers in the metal bars,")
        print("then the Magic of Old Valyria will make the grid disappear. But if you get it")
        print("wrong after 10 times then the Magic will lock it forever and you can't get the wildfire.")
        print("\n")
        code = "111" #str(randint(1,9)) + str(randint(1,9)) + str(randint(1,9))
        guess = input("[Combination]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("\n")
            print("THE MAGIC OF OLD VALYRIA DOESN'T RECOGNIZE THE COMBINATION!")
            guesses += 1
            guess = input("[Combination]> ")

        if guess == code:
            print("\n")
            print("The grid magically disappears and you can take the wildfire you need.")
            print("You grab several pots and run as fast as you can to the")
            print("Small Council Room, a special place in the castle that will trigger its destruction.")
            return 'fight_scene'
        else:
            print("\n")
            print("The numbers disappear into the metal, you can't keep guessing, its over.")
            print("The magic has locked the wildfire from you. The last chance is gone.")
            print("You decide to sit there, and finally the Lannister soldiers find you, then take")
            print("you to the Black Cells, waiting to be executed by the new King's Justice, Ser Ilyn Payne.")
            return 'death'
			

class Fight(Scene):
	
	enemies = [
		"Ser Jaime Lannister", 
		"Ser Amory Lorch", 
		"Ser Roland Crakehall",
		"Ser Gregor Clegane",
		"Ser Addam Marbrand",
		"Ser Ilyn Payne"
		]
	
	good_attacks = [
		"You made a good attack! He es wounded, keep going.",
		"Your sword pierces his armor and you wound him.",
		"Your swords clashes with his sword in mid-air, but you prevail and wound him.",
		"You caught your enemy off-guard and made a serious injury to him.",
		"Your Valyrian Steel cuts his sword and you damage him.",
		"Your enemy loses his stance and you manage to wound him."
		"His sword gets stuck on the ceiling, you make your move."
		"You wound him, he looks tired, your victory is close."
		]
	
	def enter(self):
		vs = self.enemies[randint(0, len(self.enemies)-1)]	
		print("\n")
		print("After grabbing the wildfire and running through the castle, you find ",vs)
		print("You must fight for your survival, take your Valyrian Steel Sword and make a move!")
		
		your_health = 150
		enemy_health = 150
		victory = False
		
		while your_health > 0 and not victory:
			print("\n")
			move = input("[slay!/defend!/bluff!] > ")
			
			if move == "slay!":
				print("\n")
				print("You attack ", vs, "with your sword.")
				damage1 = randint(30,60)
				enemy_health = enemy_health - damage1
				damage2 = randint(10,30)
				your_health = your_health - damage2
				print(self.good_attacks[randint(0, len(self.good_attacks)-1)])
				print("But be carefull, he is and skilled swordsman and your attack also damages you.")
					
			elif move == "defend!":
				damage1 = randint(20,50)
				your_health = your_health - damage1
				damage2 = randint(10,20)
				enemy_health = enemy_health - damage2
				print("\n")
				print("You use your sword to deflect his attack.")
				print("You get a small wound from the defense. Be carefull")
				print("Still, you manage to inflict a little damage to him.")
				
			elif move == "bluff!":
				print("\n")
				print("You make a bluff move, and dodge an attack from ", vs,", keep going.")
			
			else:
				print("\n")
				print("That's not a valid move, try again.")
			
			
			if enemy_health <= 0 and your_health > 0:
				victory = True
				print("\n")
				print("Thank the seven goods! You killed ", vs,"and now you can continue!")
				return 'small_council'
				break
			
			elif your_health <= 0:
				print("\n")
				print("Oh no, ", vs," has defeated you in combat. You die.")
				return 'death'
				break
				
			if your_health >= enemy_health:
				print("\n")
				print("You're winning! Go!")
			else:
				print("\n")
				print("You're losing, calm down and focus!")	
			
			
class CouncilRoom(Scene):

    def enter(self):
        print("\n")
        print("You burst onto the Small Council Room with the wildfire pots")
        print("under your arm and surprise 5 Lannister soldiers who are trying to")
        print("sack important documents. They haven't pulled their swords out yet,")
        print("as they see the wildfire pots under your arm and don't want to set them off")
        print("\n")

        action = input("[throw the wildfire/slowly place the wildfire]> ")

        if action == "throw the wildfire":
            print("\n")
            print("In a panic you throw the wildfire at the group of soldiers")
            print("and make a leap for the door.  but the soldiers catch them before they break,")
            print("and one of them throws a dagger at your back. It's a fatal wound.")
            print("As you die you see Tywin Lannister entering the room, smilling as the")
            print("last Targaryen is finally dead.")
            return 'death'

        elif action == "slowly place the wildfire":
            print("\n")
            print("You slowly place the wildfire in the floor, as the soldiers draw their swords.")
            print("In an adrenaline rush, you go berseck against the five soldiers, killing them all.")
            print("You place the wildfire pots in place, and light a fuse to trigger the explotion.")
            print("You hear steps coming to the room, so you go to a secret scape tunnel.")
            print("It's done. Once lit the fuse it can't be stopped. In minutes the whole castle will explode.")
            return 'narrow_sea'
        else:
            print("\n")
            print("IT IS NOT KNOWN!")
            return "small_council"


class NarrowSea(Scene):

    def enter(self):
        print("\n")
        print("You get to the secret dock hidden in the rocks under the Reed Keep,")
        print("now need to pick one ship to take. Some of them could be damaged")
        print("but you don't have time to look. There's 5 ship, which one do you take?")
        print("\n")
        good_ship = "1"#str(randint(1,5))
        guess = input("[ship #]> ")


        if guess != good_ship:
            print("\n")
            print("You jump into ship",guess,"and try to sail into the Narrow Sea")
            print("The ship goes out into the sea, then you notice")
            print("major leaks all around, the ship sinks and you die in the cold waters")
            print("off the Blackwater Rush.")
            return 'death'
        else:
            print("\n")
            print("You jump into ship",guess,"and try to sail into the Narrow Sea")
            print("The ship easily slides out into the waters and go smoothly.")
            print("As you go to the Narrow Sea, you look back at the Reed Keep")
            print("as it explodes in a giant green flame, the other wildfire pots hidden")
            print("in the castle go off as well, killing all the Rebellion leaders and destroying the castle.")
            print("You did it. The Targaryen Dynasty is still alive. Time to plan your revenge.")

            return 'finished'


class Finished(Scene):

    def enter(self):
        print("\n")
        print("You won! Good job. The Targaryen supporters are looking for you.")
        return 'finished'		


class Map(object):

    scenes = {
        'throne_hall': ThroneHall(),
        'castle_armory': CastleArmory(),
        'fight_scene': Fight(),
        'small_council': CouncilRoom(),
        'narrow_sea': NarrowSea(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)		
		

got_map = Map('throne_hall')
got_game = Engine(got_map)
got_game.play()		
