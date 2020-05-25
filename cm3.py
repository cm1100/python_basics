game=[[2,0,1]
      ,[2,1,0],
      [1,2,2]]

'''for col in range(len(game)):

    check=[]
    for row in game:
        print(row[col])
        check.append(row[col])

    if check.count(check[0]) == len(check) and check[0] != 0:
        print("winner")
'''

'''if game[0][0]==game[1][1]=game[2][2] or game[2][0]==game[1][1]==game[2][0]:
    print("winner")'''

diags=[]
for x in range(len(game)):

    diags.append(game[x][x])

print(diags)


diags1=[]
cols=reversed(range(len(game)))
rows=range(len(game))
for row,col in zip(rows,cols):

    diags1.append(game[row][col])
print(diags1)

