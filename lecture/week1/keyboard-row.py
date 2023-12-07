class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl",  "zxcvbnm"]
        result= []

        for word in words:
            lowercase_word = word.lower()

            if all(char in rows[0] for char in lowercase_word) or \
                all(char in rows[1] for char in lowercase_word) or \
                all(char in rows[2] for char in lowercase_word):

                result.append(word)

        return result