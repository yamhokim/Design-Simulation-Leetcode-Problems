import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        minHeap = []
        numPassengers = 0

        # Sort the trips based on the starting value
        trips.sort(key = lambda trip: trip[1])

        for trip in trips:
            passengers, start, end = trip
            # Minheap has elements and the new trip starts after the shortest trip ends
            while minHeap and start >= minHeap[0][0]:
                numPassengers -= minHeap[0][1]
                heapq.heappop(minHeap)
            
            # Add the current trips passengers to the running total and see if its still valid
            numPassengers += passengers
            if numPassengers > capacity:
                return False
            
            # If the trip is still valid, add it to the minHeap
            heapq.heappush(minHeap, [end, passengers])

        return True
