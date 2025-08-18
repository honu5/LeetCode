class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        l=0
        r=len(arr)-1
        while l<len(arr):
          if arr[l]==0:
            arr.insert(l+1,0)
            arr.pop()
            l+=2
            r-=1
          else:
            l+=1
        