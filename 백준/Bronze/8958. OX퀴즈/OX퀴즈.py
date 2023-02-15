n = int(input())
arr = [list(map(str, input())) for _ in range(n)]

total_score = {}
count = 0

for i in range(len(arr)):
    total_score.setdefault(i, [])
    count = 0
    for j in range(len(arr[i])):        
        if arr[i][j] == "O":
            count = count + 1
            total_score[i].append(count)
            
        else:
            count = 0
            
    print(sum(total_score[i]))   