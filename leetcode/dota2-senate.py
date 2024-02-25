class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        
        radiant_queue = deque()
        dire_queue = deque()

        for i, senator in enumerate(senate):
            if senator == 'R':
                radiant_queue.append(i)
            else:
                dire_queue.append(i)


        while radiant_queue and dire_queue:
            radiant_index = radiant_queue.popleft()
            dire_index = dire_queue.popleft()

            if radiant_index < dire_index:
                radiant_queue.append(radiant_index + n)
            else:
                dire_queue.append(dire_index + n)

        return "Radiant" if len(radiant_queue) else "Dire"