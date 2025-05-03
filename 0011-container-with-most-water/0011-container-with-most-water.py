class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        ans=[]
        while l<r:
            
            ans.append(min(height[l],height[r])*(r-l))
            if height[l]>height[r]:
           
                r-=1
            else: l+=1
        print(ans)
        return max(ans)

        

        