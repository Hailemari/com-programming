class Solution:
    def decodeString(self, s: str) -> str:
        
        def helper(s, i):
            decoded_str = ""
            num = 0

            while i < len(s):
                if s[i].isdigit():
                    num = num*10 + int(s[i])
                elif s[i] == '[':
                    i, inner_decoded_str = helper(s, i+1)
                    decoded_str += num * inner_decoded_str
                    num = 0
                elif s[i] == ']':
                    return i, decoded_str
                else:
                    decoded_str += s[i]
                i += 1

            return decoded_str

        return helper(s, 0)