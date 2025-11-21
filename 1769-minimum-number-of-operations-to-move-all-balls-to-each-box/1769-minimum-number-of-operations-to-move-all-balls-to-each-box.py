class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        n = len(boxes)
      
        
        left_cost = [0] * n
      
        
        right_cost = [0] * n
      
        
        balls_count = 0
        for i in range(1, n):
           
            if boxes[i - 1] == '1':
                balls_count += 1
            
            left_cost[i] = left_cost[i - 1] + balls_count
      
       
        balls_count = 0
        for i in range(n - 2, -1, -1):
            
            if boxes[i + 1] == '1':
                balls_count += 1
            
            right_cost[i] = right_cost[i + 1] + balls_count
      
        
        return [left + right for left, right in zip(left_cost, right_cost)]
