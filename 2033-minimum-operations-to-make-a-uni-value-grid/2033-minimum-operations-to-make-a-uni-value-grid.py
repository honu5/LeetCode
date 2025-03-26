class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        list1=[num for row in grid for num in row]
        for i in list1:
            if i%x!=0:
                return -1
        list1.sort()
        a=0
        med=list1[len(list1)//2]
        for i in list1:
            a+=(abs(i-med)//x)
        return a