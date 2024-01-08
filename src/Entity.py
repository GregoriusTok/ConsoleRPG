class Entity():
    def __init__(self, name, health, location):
        self.Name = name
        self.Health = health
        self.Location = location
    
    def Move(self, location_diff = [0,0], nlocation = []):
        if nlocation != []:
            self.Location = nlocation
        if (self.Location[0] + location_diff[0]) > -1 and (self.Location[0] + location_diff[0]) < 10: 
            self.Location[0] += location_diff[0]
        if (self.Location[1] + location_diff[1]) > -1 and (self.Location[1] + location_diff[1]) < 10: 
            self.Location[1] += location_diff[1]

if __name__ == "__main__":
    pass