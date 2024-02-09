class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        num_Ys = customers.count("Y")
        num_Ns = n - num_Ys
        answer = [0] * n
        
        for i in range(n):
            answer[i] = num_Ys
            if customers[i] == "Y":
                num_Ys -= 1
        
        answer.append(0)
        answer[-1] += num_Ns
    
        for i in range(n - 1, -1, -1):
            if customers[i] == "N":
                num_Ns -= 1
            answer[i] += num_Ns
            
        return answer.index(min(answer))