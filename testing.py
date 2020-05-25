'''import  itertools
player_choice = itertools.cycle([1,2])


for i in range(10):
    print(next(player_choice))

#iterable:a thing we can iterate over

#iterator:a special object with next method


 x=
game_size=3

print("   0  1  2")

s="   "+"  ".join(str(i) for i in range(game_size))
print(s)'''

import numpy as np

print(np.zeros(5))

diction={"key1":15,"key2":16}
print(diction["key1"])
game_size=3
'''game=[]
for i in range(ame_size):
    row=[]
    for i in range(ame_size):
        row.append(0)
    game.append(row)'''
game_size=input("what size ")
game=[[0 for i in range(game_size)] for i in range(game_size)]
print(game)
