# 다이나믹 프로그래밍

def solve(n, coin, m):
    dp = [0]*(m+1)
    dp[0] = 1 # 금액-코인=0 일때,

    for i in range(n):
        for j in range(coin[i],m+1):
            dp[j] += dp[j-coin[i]]
    return dp[-1]


T = int(input())
for _ in range(T):
    N = int(input())
    coin = list(map(int, input().split())) # N개의 동전, 오름차순
    M = int(input()) # 만들어야 하는 금액
    print(solve(N, coin, M))