def function(operations):
    num = 0
    List = []
    for i in operations:
        if i == "C":
            del List[-1]
        elif i == "D":
            List.append(2*List[-1])
        elif i == "+":
            List.append(List[-1] + List[-2])
        else:
            List.append(int(i))

    for i in List:
        num += i

    return num

print(function(["5","-2","4","C","D","9","+","+"]))