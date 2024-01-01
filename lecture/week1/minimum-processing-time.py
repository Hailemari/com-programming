class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        n=len(tasks)
        processorTime.sort()
        tasks.sort()

        i = 0
        res = 0
        while i < len(processorTime):
            if processorTime[i] + tasks[n-1] > res:
                res = processorTime[i] + tasks[n-1]

            i += 1
            n -= 4

        return res
        