class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_dict = {char: i for i, char in enumerate(order)}

        def compare_words(word1, word2):
            for char1, char2 in zip(word1, word2):
                if alien_dict[char1] < alien_dict[char2]:
                    return True
                elif alien_dict[char1] > alien_dict[char2]:
                    return False
                
            return len(word1) <= len(word2)
        
        for i in range(1, len(words)):
            if not compare_words(words[i - 1], words[i]):
                return False
        
        return True