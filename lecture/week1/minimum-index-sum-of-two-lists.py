class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result_idx = []
        result_word = []
        ans = []

        for i, word1 in enumerate(list1):
            for j, word2 in enumerate(list2):
                if word1 == word2:
                    result_idx.append(i + j)
                    result_word.append(word2)
        
        
        min_idx = min(result_idx)
        for idx, word in zip(result_idx, result_word):
            if idx == min_idx:
                ans.append(word)
        
        return ans
                
                
        