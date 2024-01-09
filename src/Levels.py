from NPCs import NPC, Enemy

class Level1():
    def __init__(self, player):
        self.Height, self.Width = 10, 10

        #Entities:

        self.NPCList = []
        self.EnemyList = []

        #Set the first layout
        self.Lay1()

        self.update(player)
        self.draw() 

    def update(self, player):
        self.Layout = [row[:] for row in self.LayoutTemp]

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

    def Lay1(self):
        self.LayoutTemp = [
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

        Johann = NPC("Johann", [5,5], [
            "Yo duuuuuude, ",
            "Its def time."
        ])

        John = Enemy("John", [5, 2], [
            "Yo",
            "Lets fight"
        ], 5, {"KICK": 1})

        self.NPCList = [Johann]
        self.EnemyList = [John]

    def draw(self):
        print("=" * 29)
        for i in self.Layout:
            print(*i)

if __name__ == "__main__":
    from Player import Player

    player = Player(2, [2, 2])
    level = Level1(player)
    level.update(player)
    level.draw()
    
