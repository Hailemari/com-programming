class Solution:
    def sortSentence(self, s: str) -> str:
        words = {}

        for word in s.split():
            words[word] = int(word[-1])
        values = words.values()

        helper = [0] * len(values)

        for word, idx in words.items():
            helper[idx - 1] = word[:-1]
        

        return " ".join(helper)

