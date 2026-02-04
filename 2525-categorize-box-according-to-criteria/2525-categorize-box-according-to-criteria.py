class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        """
        :type length: int
        :type width: int
        :type height: int
        :type mass: int
        :rtype: str
        """
        if length>=pow(10,4) or width>=pow(10,4) or height>=pow(10,4) or length*width*height>=pow(10,9):
            if  mass>=100:
                return "Both"
            else:
                return "Bulky"
           

        if mass>=100:
            return "Heavy"
       
        
        return "Neither"
        