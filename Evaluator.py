import math
from Operator import find

class Evaluator:
    """Yeah"""
    def evaluate(self, tokenList):
        """Takes an expression in RPN notation and evaluates it"""
        tempStack = []
        
        for i in tokenList:
            if isinteger(i):
                tempStack.append(i)
            else:
                op = find(i)
                if len(tempStack) < op.ops:
                    print("Insufficient values!")
                    break
                else:
                    result = arithmetic(tempStack.pop(), tempStack.pop(), i)
                    tokenList.append(result)
                
        if len(tokenList) == 1:
            return tokenList[0]

        elif len(tokenList) > 1:
            print("User input has too many values")

    def arithmetic(self, num1, num2, op):
        """Arithmetic operations are handled here. No evil eval()"""
        if op == "+":
            value = num1 + num2
        elif op == "*":
            value = num1 * num2
        elif op == "/":
            value = num1 / num2
        elif op == "-":
            value = num1 - num2
        elif op == "^":
            value = math.pow(num1, num2)
        elif op == "%":
            value = num1 % num2
        return value

def isinteger(something):
    try:
        something += 1
        return True
    except TypeError:
        return False
