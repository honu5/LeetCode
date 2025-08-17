class Solution(object):
    def minimumTotal(self, triangle):
        dp=triangle[-1]
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                dp[j]=triangle[i][j] + min(dp[j+1],dp[j])
        return dp[0]

        