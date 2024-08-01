def function(moves):
    result  = {"A","B","Draw","Pending"}
    A = []
    B = []

    for i in range(len(moves)):
        if i % 2 == 0:
            A.append(moves[i])
        else:
            B.append(moves[i])

    if (([0,0] in A and [0,1] in A and [0,2] in A) or
        ([1,0] in A and [1,1] in A and [1,2] in A) or
        ([2,0] in A and [2,1] in A and [2,2] in A) or
        ([0,0] in A and [1,0] in A and [2,0] in A) or
        ([0,1] in A and [1,1] in A and [2,1] in A) or
        ([0,2] in A and [1,2] in A and [2,2] in A) or
        ([0,0] in A and [1,1] in A and [2,2] in A) or
        ([2,0] in A and [1,1] in A and [0,2] in A)):
        return "A"
    if (([0,0] in B and [0,1] in B and [0,2] in B) or
        ([1,0] in B and [1,1] in B and [1,2] in B) or
        ([2,0] in B and [2,1] in B and [2,2] in B) or
        ([0,0] in B and [1,0] in B and [2,0] in B) or
        ([0,1] in B and [1,1] in B and [2,1] in B) or
        ([0,2] in B and [1,2] in B and [2,2] in B) or
        ([0,0] in B and [1,1] in B and [2,2] in B) or
        ([2,0] in B and [1,1] in B and [0,2] in B)):
        return "B"

    if len(moves) == 9:
        return "Draw"
    else:
        return "Pending"

print(function([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))