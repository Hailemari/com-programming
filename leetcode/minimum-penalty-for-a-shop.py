class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        
        total_Y = customers.count("Y")
        total_N = 0
        num_y_arr = [total_Y]
        num_n_arr = [total_N]

        for i in range(n):
            if customers[i] == "Y":
                total_Y -= 1
                num_y_arr.append(total_Y)
            else:
                num_y_arr.append(total_Y)
            
        for i in range(n):
            if customers[i] == "N":
                num_n_arr.append(total_N)
                total_N += 1
            else:
                num_n_arr.append(total_N)
        num_y_arr.append(0)
        num_n_arr.append(total_N)
        ans = []
        for left, right in zip(num_y_arr, num_n_arr):
            ans.append(left + right)
        
        return ans.index(min(ans))

        