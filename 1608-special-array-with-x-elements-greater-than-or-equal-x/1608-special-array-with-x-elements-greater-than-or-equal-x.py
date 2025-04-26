class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        if nums[0]==100:
            return 100
        for i in range(max(nums)):
            cnt=0
            for j in range(len(nums)):
                if nums[j]>=i:
                    cnt+=1
            if i==cnt:
                return i
        return -1
        