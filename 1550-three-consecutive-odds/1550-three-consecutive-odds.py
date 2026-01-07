class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr)<=2:
            return False
        if len(arr)==3 and len(set(arr))==1:
            return True
        for i in range(len(arr)-2):
            found=True
            arrs=arr[i:i+3]
            for j in arrs:
                if j%2==0:
                    found=False
                    continue
                    
            if found==True:
                return True
        return False
                
        