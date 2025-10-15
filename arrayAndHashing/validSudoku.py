from collections import defaultdict
boards= [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

# output is true
cols=[set() for _ in range(9)]  
rows=[set() for _ in range(9)]
threeSpace=defaultdict(set)
valid=True
for i in range(9):
    if not valid:
        break
    for j in range(9):
        c=boards[i][j]
        if c==".":
            continue
        if c in cols[j] or c in rows[i] or c in threeSpace[(i//3,j//3)]:
            valid=False
            break
        cols[j].add(c)
        rows[i].add(c)
        threeSpace[(i//3,j//3)].add(c)
print(valid)