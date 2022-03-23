def knapsack_DP(C, w, v, n):
    # Initially filling the table with 0s 
    dp = [[0 for x in range(C+1)] for x in range(n+1)]

    # Builidng the table dp[][] using the formula 
    for i in range(n + 1):
        for j in range(C + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif w[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]] + v[i-1])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][C] 


v = [1, 2, 5, 6]
w = [2, 3, 4, 5]
C = 8
n = 4

print("Total profit:", knapsack_DP(C, w, v, n))

# Output:
# Total profit: 8