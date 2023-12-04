class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good_num_len = 1
        good_num_list = []

        for i in range(1, len(num)):
            if num[i] == num[i - 1]:
                good_num_len += 1
                if good_num_len == 3:
                    good_num_list.append(num[i])

                else:
                    continue
            else:
                good_num_len = 1

        if len(good_num_list):
            return str(max([int(num) for num in good_num_list])) * 3
        else:
            return ""
        

