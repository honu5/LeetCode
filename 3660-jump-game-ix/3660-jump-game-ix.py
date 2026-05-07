class DSU:
    def __init__(self, n, nums):
        self.par = list(range(n))
        self.sz = [1] * n
        self.compMax = nums[:]

    def findPar(self, u):
        if self.par[u] != u:
            self.par[u] = self.findPar(self.par[u])
        return self.par[u]

    def unionBySize(self, u, v):
        pu = self.findPar(u)
        pv = self.findPar(v)

        if pu == pv:
            return

        if self.sz[pu] < self.sz[pv]:
            pu, pv = pv, pu

        self.par[pv] = pu
        self.sz[pu] += self.sz[pv]

        self.compMax[pu] = max(self.compMax[pu], self.compMax[pv])


class Solution:
    def maxValue(self, nums):
        n = len(nums)

        prefixMax = [0] * n
        suffixMin = [0] * n

        prefixMax[0] = nums[0]
        for i in range(1, n):
            prefixMax[i] = max(prefixMax[i - 1], nums[i])

        suffixMin[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffixMin[i] = min(suffixMin[i + 1], nums[i])

        ds = DSU(n, nums)

        for i in range(n - 1):
            if prefixMax[i] > suffixMin[i + 1]:
                ds.unionBySize(i, i + 1)

        ans = [0] * n

        for i in range(n):
            ans[i] = ds.compMax[ds.findPar(i)]

        return ans