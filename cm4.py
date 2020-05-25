
import itertools

#game = [[1,1,1],
 #       [0,0,0],
  #      [0,0,1]]


def win(current_game):

    def allsame(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False


    #horizontal
    for row in game:
        if allsame(row):
            print(f"winner {row[0]} is horizontal")
            return True


    #vertical
    for col in range(len(game)):

        check = []
        for row in game:

            check.append(row[col])

        if allsame(check):
            print(f"winner {check[0]} is vertical")
            return True


    #diagona;
    diags = []
    for x in range(len(game)):
        diags.append(game[x][x])

    if allsame(diags):
        print(f"winner {diags[0]} is diagonaly")
        return True

    diags = []
    cols = reversed(range(len(game)))
    rows = range(len(game))
    for row, col in zip(rows, cols):
        diags.append(game[row][col])

    if allsame(diags):
        print(f"winner {diags[0]} is diagonaly")
        return True

    return False


def g_b(game_map,player=0,row=0,column=0,just_display=False):
    try:
        if game_map[row][column!=0]:
            print("this position is occupied")
            return game_map,False
        print("   "+"  ".join(str(i) for i in range(len(game_map))))
        if not just_display:
            game_map[row][column]=player
        for count,i in enumerate(game_map):
            print(count,i)
        return game_map,True
    except IndexError as e:
        print(e)
        return game_map,False
    except Exception as e:
        print("wrong")
        return game_map,False
#game=g_b(game,1,2,0)




play=True
players=[1,2]
while play:
    game_size = int(input("what size "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    print(game)

    game_won=False
    game,_=g_b(game,just_display=True)
    player_choice=itertools.cycle([1,2])
    while not game_won:
        current_player=next(player_choice)
        print(f"current player {current_player}")
        played=False
        while not played:
            column_c=int(input("which column "))
            row_c = int(input("which row "))
            game,played = g_b(game,current_player,row_c,column_c)
        if win(game):
            game_won=True
            again=input("would you like to play again? y/n")
            if again.lower()=='y':
                print("restarting")
            elif again.lower()=='n':
                print("bye")
                play=False
            else:
                print("not a valid answer")
                play=False