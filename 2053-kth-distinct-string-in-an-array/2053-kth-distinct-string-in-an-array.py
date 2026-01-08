class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        ans=[]
        count=Counter(arr)
        for i in arr:
            print(count[i])
            if count[i]==1:
                ans.append(i)
            if len(ans)==k:
                return ans[-1]
        return ""
        