'''
Initial Approach
'''
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        counter = 0
        
        current_index = 0
        while current_index < len(timeSeries):
            duration_left = duration

            while duration_left > 0:
                counter += 1

                if current_index + 1 < len(timeSeries) and timeSeries[current_index + 1] <= timeSeries[current_index] + duration - 1:       
                    counter += timeSeries[current_index + 1] - timeSeries[current_index] - 1
                    duration_left = duration
                    current_index += 1
                else:
                    duration_left -= 1 
            
            current_index += 1
        
        return counter
            
'''
Optimized Approach
'''
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total_time = 0

        for i in range(0, len(timeSeries) - 1):
            if timeSeries[i+1] - timeSeries[i] + 1 <= duration:
                total_time += timeSeries[i+1] - timeSeries[i]
            else:
                total_time += duration

        total_time += duration
        return total_time