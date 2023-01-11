import sys
# sys.stdin = open("input.txt")

def solve(n, p, q):
    if n == 1:
        dict[n] = 2
        return dict[n]
    if n in dict:
        return dict[n]
    dict[n] = solve(n//p, p, q) + solve(n//q, p, q)
    return dict[n]

N, P, Q = map(int, input().split())
dict = {0: 1}
solve(N, P, Q)
print(dict[N])