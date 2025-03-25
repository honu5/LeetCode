class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        c=set()
        last_digits={d for d in digits if d%2==0}
        for num in permutations(digits,3):
            if num[0]!=0 and num[2] in last_digits:
                c.add(num)
        return len(c)
        