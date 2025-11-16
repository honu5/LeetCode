class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if sum(arr)%3!=0:
            return False
        tri=sum(arr)/3
        val=0
        n=0
        for i in range(len(arr)):
            if n==2:
                return True
            val+=arr[i]
            if val==tri:
                n+=1
                val=0
        return False
            