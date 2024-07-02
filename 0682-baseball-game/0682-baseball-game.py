class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op.isdigit() or (op[0] == '-' and op[1:].isdigit()):
                stack.append(int(op)) 
            
            elif op == "D":
                if stack:
                    stack.append(stack[-1] * 2)
            elif op == "C":
                if stack:
                    stack.pop()
            elif op == "+":
                if len(stack) >= 2:
                    stack.append(stack[-1] + stack[-2])
            
        return sum(stack)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # stack = []
        # for ele in operations:
        #     if ele.isdigit() or (ele[0] == '-' and ele[1:].isdigit()):
        #         stack.append(int(ele))
        #     elif ele == 'C':
        #        if stack:
        #         stack.pop()
        #     elif ele == 'D':
        #         if stack:
        #             stack.append(stack[-1] * 2)
        #     elif ele == "+":
        #         if len(stack) >= 2:
        #             stack.append(stack[-1] + stack[-2])
                    
        # return sum(stack)
