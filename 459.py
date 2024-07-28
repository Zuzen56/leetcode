def function(s):
    for i in range(len(s) // 2) :
        s1 = s[:i+1]
        s2 = s1
        if len(s)%len(s1) == 0:
            while len(s1) <= len(s):
                s1 = s1 + s2
                if s1 == s:
                    return True
        else:
            continue
    return False

def func(s):
    print(s.find(s,1),len(s))
    print((s+s).find(s,1))
    return (s + s).find(s, 1) != len(s)


print(func("abab"))