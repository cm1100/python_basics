



game = [[0,0,0],
        [0,0,0],
        [0,0,0]]



def g_b(game_map,player=0,row=0,column=0):
    try:

        print("   a  b  c")
        game_map[row][column]=player
        for count,i in enumerate(game_map):
            print(count,i)
        return game_map
    except IndexError as e:
        print(e)
    except Exception as e:
        print("wrong")

game=g_b(game,1,2,0)
#game=g_b(gameb,1,3,0)




