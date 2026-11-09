def powers(a, b):
    if b <= 0:
        return 1
    res = powers(a, b // 2)
    if b % 2:
        return res * res * a
    else: 
        return res * res


def solve():
    n = int(input())
  
    ans = 2 * (4 * 3 * powers(4, n -3)) + (n - 3) * (4 * 9 * powers(4, n - 4))
    print(ans)


solve()
