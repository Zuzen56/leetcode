def function(s):
    length = 0
    for i in range(len(s) - 1 ,0,-1):
        if s[i] == " ":
            s = s[:i]
        else:
            break
    for i in range(len(s) - 1 ,-1,-1):
        if s[i] != " ":
            length +=1
        else:
            break

    return length

print(function("h   "))