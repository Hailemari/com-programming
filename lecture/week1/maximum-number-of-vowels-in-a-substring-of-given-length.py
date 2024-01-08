class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']

        left = 0
        max_num = 0
        for char in s[:k]:
            if char in vowels:
                max_num += 1
        
        curr_num = max_num
        for right in range(k, len(s)):
            if s[left] in vowels:
                curr_num -= 1
            left += 1
            if s[right] in vowels:
                curr_num += 1

            max_num = max(max_num, curr_num)

        return max_num


        