"""BattleShip game by Rob Farlow and David MacLean"""
from random import randint
aiboat = [randint(0, 5), randint(0, 5)]
aiboard = []
playerguess = [1,3]
row = ["0","0","0","0","0"]
def aiboard():
    for i in range(5):
        aiboard.append(row)
        print(" ".join(aiboard[i]))

def aiguess():
    aiguess = [randint(0, 5),randint(0, 5)]
    if userBoat == aiguess :
        print("Fuck you! You Lost")
    else:
        p
    return aiguess





