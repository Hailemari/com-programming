class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = ["+", "-", "*", "/"]
        for token in tokens:
            if token in operators:
                top = stack.pop()
                bottom = stack.pop()

                if token == "+":
                    res = bottom + top                
                if token == "-":
                    res = bottom - top                  
                if token == "*":
                    res = bottom * top                
                if token == "/":
                    res = int(float(bottom) / top)
            
                stack.append(res)
            else:
                stack.append(int(token))

        return stack[0]