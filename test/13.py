def function(s):
    result = 0
    dict = {
        "I": 1,
        "a": 4,
        "V": 5,
        "b": 9,
        "X": 10,
        "c": 40,
        "L": 50,
        "d": 90,
        "C": 100,
        "e": 400,
        "D": 500,
        "f": 900,
        "M": 1000
    }
    s = s.replace("IV", "a")
    s = s.replace("IX", "b")
    s = s.replace("XL", "c")
    s = s.replace("XC", "d")
    s = s.replace("CD", "e")
    s = s.replace("CM", "f")

    for i in range(len(s)):
        value = dict[s[i]]
        result += value

    return result

print(function('LVIII'))