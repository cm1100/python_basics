game=[[1,1,1]
      ,[0,2,0],
      [2,2,0]]

print(game)


def win(current_game):
    for row in game:
        print(row)
        '''not_match=False
        for item in row:
            if item!=row[0]:
                not_match=True

        if not not_match:
            print("winner")'''

        if row.count(row[0])==len(row) and row[0]!=0:
            print("winner")



win(game)