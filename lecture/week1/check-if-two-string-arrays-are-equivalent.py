class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string1 = ""
        string2 = ""

        for word in word1:
            string1 += word

        for word in word2:
            string2 += word
        
        if len(string1) != len(string2):
            return False
            
        if string1 in string2:
            return True
        else:
            return False
        