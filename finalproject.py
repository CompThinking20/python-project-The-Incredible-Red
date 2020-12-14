import random

class Player(object):
    # gives a rating system of how good eacch player is at each task
    def __init__(self, name, passing, setting, hitting):
        self.name = name
        self.passing = passing
        self.setting = setting
        self.hitting = hitting
# This is the first player, more will come as the project moves along
devyn = Player("Devyn Cobb", 6, 5, 8)
morgan = Player("Morgan Fox", 9, 6, 4)
kayla = Player("Kayla Benezs", 8, 8, 7)
# This rating system will be taken into consideration when the random number for each task is given out and will allow to program to decide if the next task will be successful
#Ultimately I want to create a game that will show the results of a volleyball match played with players out of their normal positions
#This program will take a value agrument of how well each player can perform a certain task and it will return the results of if the home team got a kill or lost the point

def play (back, set, hit):
#The code below sets up the random number generator for each event that occurs. further below is the code that determines whether or not the players can perform their task correctly.
    back_quality = random.randint(1, 10) * back.passing
    print ("Pass Quality is " + str(back_quality))
    set_quality = random.randint(1, 10) * set.setting
    print ("Set Quality is " + str(set_quality))
    hit_quality = random.randint(1, 10) * hit.hitting
    print ("Hit Quality is " + str(hit_quality))

#These if/else statements tell the program whether the ball should achieve the desired move or if it should be dropped based on the random numbers the program produces for us.
    if (back_quality > 5):
        print (back.name + " passed the ball!")
    else:
        print (back.name + " dropped the ball!")

    if (set_quality > back_quality):
        print (set.name + " set the ball!")
    else:
        print (set.name + " dropped the ball!")

    if (hit_quality > set_quality):
        print (hit.name + " hit the ball!")
    else:
        print (hit.name + " dropped the ball!")

play(devyn, morgan, kayla)
#This works for the most part, I am trying to get the code to stop running if the ball is dropped before the last person, or the hitter touches the ball. Work in progress.

while i

    if i == dropped
        break
    print("Good Game!")
