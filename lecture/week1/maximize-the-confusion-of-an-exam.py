class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0

        j = k
        max_num1 = 0
        for right in range(len(answerKey)):
            if answerKey[right] != "T":
                j -= 1
        
            
            while j < 0:
                if answerKey[left] == "F":
                    j += 1
                left += 1

            max_num1 = max(max_num1, right - left + 1)
            
        left2 = 0
        i = k
        max_num2 = 0
        for right in range(len(answerKey)):
            if answerKey[right] != "F":
                i -= 1

            while i < 0:
                if answerKey[left2] == "T":
                    i += 1
                left2 += 1
            
            max_num2 = max(max_num2, right - left2 + 1)

        return max(max_num1, max_num2)