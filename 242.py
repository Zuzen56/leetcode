def function(s,t):
    result = False
    if len(s) != len(t):
        return result
    i =0
    j = 0
    while i < len(s) and s != "":
        change = False
        while j < len(t):
            if s[i] == t[j]:
                s = s[:i] +s[i+1:]
                t = t[:j] +t[j+1:]
                change = True
                j = 0
                break
            j += 1
        if  change == False:
            return result

    return True


print(function('anagram','nagaram'))