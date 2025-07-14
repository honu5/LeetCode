class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        # diff[i] = net change in passenger count at kilometre i
        diff = [0] * 1001          # because 0 ≤ location ≤ 1000

        for num, frm, to in trips:
            diff[frm] += num       # pick up
            diff[to]   -= num       # drop off ( NOTE: to is *exclusive* )

        curr = 0
        for passengers in diff:     # sweep east
            curr += passengers
            if curr > capacity:
                return False
        return True
