from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        heap = []

        heapq.heappush(heap, intervals[0].end)

        for interval in intervals[1:]:

            if heap[0] <= interval.start:
                heapq.heappop(heap)

            heapq.heappush(heap, interval.end)

        return len(heap)