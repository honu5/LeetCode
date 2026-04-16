from collections import Counter

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        if s == goal:
            return len(set(s)) < len(s)
        
        val = 0
        diff = []
        
        for i in range(len(s)):
            if s[i] != goal[i]:
                val += 1
                diff.append(i)
        
        if val == 2:
            i, j = diff
            return s[i] == goal[j] and s[j] == goal[i]
        
        return False