def function(matrix):
    m = len(matrix)
    n = len(matrix[0])
    print(m,n)
    matrix2 = [[0 for _ in range(m)] for _ in range(n)]
    for i in  range(m ) :
        for j in range(n ) :
            matrix2[j][i]  = matrix[i][j]
    return matrix2

print(function([ [1,2,3],[4,5,6] ]))