class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        ans=[1]
        if num%2!=0:
            return False
        if num<=100:

            for i in range(2,num//2):
                if num%i==0:
                    if i in ans:
                        break
                    ans.append(i)
                    ans.append(num/i)
        elif num<=10000:
            for i in range(2,num//8):
                if num%i==0:
                    if i in ans:
                        break
                    ans.append(i)
                    ans.append(num/i)
        else:
            for i in range(2,num//32):
                if num%i==0:
                    if i in ans:
                        break
                    ans.append(i)
                    ans.append(num/i)



        print(ans)
        if sum(ans)==num:
            return True
        return False

        