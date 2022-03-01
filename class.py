class Music:

     def __init__(self, gospel, rap, rnb ,name):
        self.gospel = gospel
        self.rap = rap          
        self.rnb = rnb
        self.name = name


gospel = ("He'll Take The Pain Away")
name = ("Kirk Franklin")
print(gospel)
print(name)
print(" ")
    
rap = ("What About Me" "," "Long Journey")
name = ( "Boosie Bad A")
print(rap)
print(name)
print(" ")

rnb = ("Don't Get Down" "," "Feel So Good")
name = ("Ne'Yo")
print(rnb)
print(name)

class Sports:
 def __init__(self, teamName, ball, arena,stadium):
        self.teamName = teamName
        self.ball = ball
        self.arena = arena
        self.canPlay = True
        self.stadium = stadium

 def can_play_indoor(self):
        self.canPlay = False

        
ftball = Sports("Falcons", "ftball", "Mercadez", "Atl")
soccor = Sports("Blues", "soccor", "GreenLeaf","New Orleans")
BasketBall = Sports("Hawks", "Basketball", "StateFarm", "GA")

print(ftball.arena)
print(soccor.arena)

BasketBall.can_play_indoor()
print(BasketBall.arena)

