input =[ 
            [ 1, 2, 3,], 
            [ 4, 5, 6 ], 
            [ 7, 8, 9 ]
        ] 
rows=3
columns=3

solution1=[[] for i in range(rows+columns-1)] 
for i in range(rows): 
    for j in range(columns): 
        sum=i+j 
        if(sum%2 ==0): 
            solution1[sum].insert(0,input[i][j]) 
        else: 
            solution1[sum].append(input[i][j]) 
for i in solution1: 
    for j in i: 
        print(j,end=" ")