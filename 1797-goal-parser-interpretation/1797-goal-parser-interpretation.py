class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        ans=""
        for i in range(len(command)):
            if command[i]=='G':
                ans+="G"
            elif command[i]=='(' and command[i+1]=='a':
                ans+="al"
            elif command[i]=='(' and command[i+1]==')':
                ans+="o"
            else:
                continue
        return ans
        