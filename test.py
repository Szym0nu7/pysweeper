arr = []
cols = 3
rows = 3


for i in range(rows):
    arr.append([])
    for j in range(cols):
        arr[i].append(j)
        
for i in range(rows):
    for j in range(cols):
        print(arr[i][j])