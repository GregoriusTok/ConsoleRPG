import msvcrt
from Entity import Entity

class Player(Entity):
    def __init__(self, health, location):
        Entity.__init__(self, "Player", health, location)

        self.Direction = "UP"

        self.Moveset = {"KICK": 5, "PUNCH": 3}

    def Get_Move_Input(self):
        Wkey = 119
        Akey = 97
        Skey = 115
        Dkey = 100

        key_code=0
        while key_code==0:
            key_pressed = msvcrt.kbhit()
            if key_pressed: 
                key_code = ord(msvcrt.getch())
            else: 
                key_code = 0
                continue

            if key_code == Wkey:
                self.Move(location_diff=[0, -1])
                self.Direction = "UP"
            elif key_code == Skey:
                self.Move(location_diff=[0, 1])
                self.Direction = "DOWN"
            elif key_code == Akey:
                self.Move(location_diff=[-1, 0])
                self.Direction = "LEFT"
            elif key_code == Dkey:
                self.Move(location_diff=[1, 0])
                self.Direction = "RIGHT"
            else:
                key_code = 0
                print("Not Direction (WASD)")
                continue

if __name__ == "__main__":
    player = Player(24, [1, 1])

    for i in player.Moveset:
        print(i , player.Moveset[i])