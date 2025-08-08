from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = nums[:min(len(nums), k + 1)]  
        
        if len(set(window)) != len(window):  
            return True
        
        for i in range(1, len(nums) - k):  
            window.pop(0)  
            if k + i < len(nums): 
                window.append(nums[k + i])  

            
            if len(set(window)) != len(window):  
                return True

        return False

