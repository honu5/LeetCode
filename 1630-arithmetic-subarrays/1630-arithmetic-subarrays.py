class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        def check(nCh):
            diff = nCh[1] - nCh[0]
            l,r = 1,2
            while r<len(nCh):
                if nCh[r] - nCh[l] != diff:
                    return False
                l+=1
                r+=1
            return True
        ans = []
        for i in range(len(l)):
            curr = nums[ l[i] : r[i]+1 ]
            curr.sort()
            curr = curr[::-1]
            ans.append (check(curr))
        return ans
        