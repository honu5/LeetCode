class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        odd=[]
        even=[]
        nums=str(num)

        for i in range(len(nums)):
            if int(nums[i])%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        odd.sort(reverse=True)
        even.sort(reverse=True)
        finall=[]
        i=0
        ev=0
        od=0
        if int(nums[0])%2==0:
            start=even
            then=odd
        else:
            start=odd
            then=even

        print(even,odd)
        while i<len(nums):
            if int(nums[i])%2==0  :
                finall.append(even[ev])
                
                ev+=1
            elif int(nums[i])%2==1 and od<len(odd):
                finall.append(odd[od])
               
                od+=1
            i+=1


        val=''.join(finall)
        return int(val)
        
        