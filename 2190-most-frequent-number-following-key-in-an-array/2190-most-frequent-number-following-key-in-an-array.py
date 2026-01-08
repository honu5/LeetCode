class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        
        sub = []
        for i in range(len(nums) - 1):
            if nums[i] == key:
                sub.append(nums[i + 1])

        count = Counter(sub)
        most = count.most_common()
        return most[0][0]
        