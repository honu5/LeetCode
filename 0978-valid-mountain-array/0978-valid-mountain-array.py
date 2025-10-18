class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if arr==sorted(arr) or arr==sorted(arr,reverse=True):
            return False
        
        for i in range(1,len(arr)):
            if arr[i]<arr[i-1]:
                let=i
                break
        if len(arr[let:len(arr)])!=len(set(arr[let:len(arr)])) or  len(arr[0:let])!=len(set(arr[0:let])):
            return False
            return False
        

        for i in range(let,len(arr)):
            if arr[i]>=arr[i-1]:
                return False
        return True
        