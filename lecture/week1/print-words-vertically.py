class Solution:
    def printVertically(self, s: str) -> List[str]:
        res = []

        s = s.split(' ')
        words_len = [len(word) for word in s]
        max_len = max(words_len)
        
        for i in range(max_len):
            curr_word = ""
            for j in range(len(s)):
                if i > len(s[j]) - 1:
                    curr_word += " "
                else:
                    
                    curr_word += s[j][i]
            
            res.append(curr_word)


        res = [word.rstrip() for word in res]
        return res


        