from NPCs import NPC, Enemy

class Level1():
    def __init__(self, player):
        self.Height, self.Width = 10, 10

        #Entities:
        self.Jerry = NPC("Jerry", [5, 5], [
            "Hey there,",
            "How you doing?",
            "Good?",
            "That means no one's told you yet.",
            "Go to the school to figure out everything you want to know."
        ])

        self.Nathan = NPC("Nathan", [3, 6], [
            "I don' know nothin'",
            "Get away from me."
        ])

        self.Richard = Enemy("Richard", [2, 2], [
            "YOU WILL DIE!!!", 
            "YOU KNOW WHYYY!!!"
        ], 12, {"PUNCH": 3})

        self.Joel = Enemy("Joel", [2, 4], [
            "I hate you,",
            "Prepare to die"
        ], 5, {"KICK": 5})

        self.NPCList = [self.Jerry, self.Nathan]
        self.EnemyList = [self.Richard, self.Joel]

        self.update(player)
        self.draw()
        

    def update(self, player):
        self.Layout = [
            ["  ", "  ", "--", "  ", "  ", "  ", "  ", "  ", "--", "''"],
            ["  ", "--", "  ", "  ", "  ", "  ", "  ", "--", "  ", "  "],
            ["  ", "--", "  ", "  ", "  ", "  ", "  ", "--", "  ", "  "],
            ["  ", "''", "--", "  ", "  ", "  ", "--", "  ", "''", "  "],
            ["''", "  ", "--", "  ", "  ", "  ", "  ", "--", "  ", "  "],
            ["  ", "  ", "--", "  ", "  ", "  ", "  ", "--", "  ", "  "],
            ["  ", "--", "  ", "  ", "  ", "  ", "  ", "--", "''", "  "],
            ["  ", "--", "  ", "  ", "  ", "  ", "--", "  ", "  ", "  "],
            ["  ", "--", "  ", "  ", "  ", "  ", "--", "''", "  ", "  "],
            ["''", "  ", "--", "  ", "  ", "--", "  ", "  ", "  ", "  "]
        ]

        for i in self.NPCList: #Check Collision w/ NPCs
            if player.Location == i.Location:
                i.speak(player)
                if player.Direction == "UP":
                    player.Move(location_diff = [0, 1])
                elif player.Direction == "DOWN":
                    player.Move(location_diff = [0, -1])
                elif player.Direction == "LEFT":
                    player.Move(location_diff = [1, 0])
                elif player.Direction == "RIGHT":
                    player.Move(location_diff = [-1, 0])

            self.Layout[i.Location[1]][i.Location[0]] = "PP"

        for i in self.EnemyList: #Check Collision w/ Enemies
            if player.Location == i.Location:
                result = i.fight(player)
                if result == "EDead":
                    self.EnemyList.remove(i)
                    continue
                if player.Direction == "UP":
                    player.Move(location_diff = [0, 1])
                elif player.Direction == "DOWN":
                    player.Move(location_diff = [0, -1])
                elif player.Direction == "LEFT":
                    player.Move(location_diff = [1, 0])
                elif player.Direction == "RIGHT":
                    player.Move(location_diff = [-1, 0])

            self.Layout[i.Location[1]][i.Location[0]] = "EE"

        self.Layout[player.Location[1]][player.Location[0]] = "@@" #Set Player initial position

    def draw(self):
        print()
        for i in self.Layout:
            print(*i)

if __name__ == "__main__":
    from Player import Player

    player = Player(2, [2, 2])
    level = Level1(player)
    level.update(player)
    level.draw()
    
