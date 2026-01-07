class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n==0:
            return True
        if len(flowerbed)==1 and flowerbed[0]==0 and n==1:
            return True 
        if len(flowerbed)<=2:
            if sum(flowerbed)!=0 or n>(len(flowerbed)//2):
                return False
            else:
                return True

        if flowerbed[0]==0 and flowerbed[1]==0:
            n-=1
            flowerbed[0]=1
        if flowerbed[-1]==0 and flowerbed[-2]==0:
            n-=1
            flowerbed[-1]=1
        
        for i in range(1,len(flowerbed)-1):
            if n<=0:
                return True
            if flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]!=1:
                flowerbed[i]=1
                n-=1
        return n==0

    