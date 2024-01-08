from time import sleep
from random import choice
from Entity import Entity

class NPC(Entity):
    def __init__(self, name, location, diologue, health = 100):
        Entity.__init__(self, name, health, location)

        self.Diologue = diologue

    def speak(self, player):
        print()
        for i in self.Diologue:
            print(self.Name + ": " + i)
            sleep(0.5)
        print()

class Enemy(NPC):
    def __init__(self, name, location, diologue, health, moveset = {}):
        NPC.__init__(self, name, location, diologue, health)

        self.Moveset = moveset
        self.TotHealth = self.Health

    def fight(self, player):
        self.speak(player)
        print("You have started to fight " + self.Name)

        phealthper = player.Health / 10
        ehealthper = self.Health / self.TotHealth

        print("Player Health:")
        print("|" * round(20 * phealthper))
        print(self.Name, "Health:")
        print("|" * round(20 * ehealthper))
        print()

        while player.Health > 0 and self.Health > 0:
            for i in player.Moveset:
                print(i , player.Moveset[i])

            pmove = input("What Move? ").upper()
            if pmove not in player.Moveset:
                print()
                continue
            self.Health -= player.Moveset[pmove]
            print("You did the move:", pmove)
            print("Dealing" , player.Moveset[pmove] , "damage")
            print()

            emove = choice(list(self.Moveset.keys()))
            player.Health -= self.Moveset[emove]
            print(self.Name, "did the move:", emove)
            print("Dealing", self.Moveset[emove], "damage")
            print()

            phealthper = player.Health / 10
            ehealthper = self.Health / self.TotHealth

            print("Player Health:")
            print("|" * round(20 * phealthper))
            print(self.Name, "Health:")
            print("|" * round(20 * ehealthper))
            print()
        
        if self.Health < 1:
            print("YOU WON!!!")
            return "EDead"
        elif player.Health < 1:
            print("YOU LOST!!!")
            return "PDead"