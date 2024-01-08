from Player import Player
from Levels import Level1

def main():
    running = True
    player = Player(10, [4, 8])
    level1 = Level1(player)

    while running:
        player.Get_Move_Input()
        level1.update(player)
        level1.draw()
        
if __name__ == "__main__":
    main()
    