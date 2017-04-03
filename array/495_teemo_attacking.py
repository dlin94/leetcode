class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        total = 0
        for i in range(0, len(timeSeries)):
            if i == len(timeSeries)-1:
                total += duration
            else:
                total += min(timeSeries[i+1] - timeSeries[i], duration)
        return total
