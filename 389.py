def function(s,t):
    for i in s:
        index = t.index(i)
        if index != -1:
            t = t[:index] + t[index+1:]
        else:
            return t
    return t



print(function("a","aa"))