import sys
import math

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    out = []
    idx = 1
    for _ in range(t):
        a = int(data[idx])
        b = int(data[idx+1])
        idx += 2
        
        g = math.gcd(a, b)
        if b % a == 0:
       
            out.append(str(b * (b // a)))
        else:
            out.append(str((a * b) // g))
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
