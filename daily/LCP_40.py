def function(cards,cnt):
    cards.sort(reverse=True)
    ans = 0
    tmp = 0
    odd = even = -1
    end = len(cards) - cnt
    for i in range(cnt):
        tmp += cards[i]
        if cards[i] % 2 == 1:
            odd = cards[i]
        else:
            even = cards[i]
    if tmp % 2 == 0:
        return tmp
    for i in range(cnt, len(cards)):
        if cards[i] % 2 == 1:
            if even != -1:
                ans = max(ans, tmp - even + cards[i])
        else:
            if odd != -1:
                ans = max(ans, tmp - odd + cards[i])

    return ans

print(function([1,2,8,9],3))