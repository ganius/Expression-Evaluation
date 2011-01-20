import math
from Operator import find

class Evaluator:
    """Evaluater class"""
    def evaluate(self, tokenList):
        """Takes an expression in RPN notation and evaluates it"""
        tempStack = []
        print(tokenList)
        try:
            tokenList.reverse()
        except AttributeError:
            result = "Error: Invalid tokens!"
            return result
        
        while len(tokenList) > 0:
            i = tokenList.pop()
            if isFloat(i):
                tempStack.append(i)
            else:
                op = find(i)
                if len(tempStack) < op.ops:
                    print("Error: Insufficient values!")
                    break
                else:
                    value = arithmetic(tempStack.pop(), tempStack.pop(), i)
                    tokenList.append(value)
                
            if len(tokenList) == 1 and tempStack == []:
                result = tokenList[0]
                return result

        if len(tokenList) > 1:
            result = "Error: User input has too many values"
            return result

def arithmetic(num1, num2, op):
    """Arithmetic operations are handled here. No evil eval()"""
    if op == "+":
        value = num2 + num1
    elif op == "*":
        value = num2 * num1
    elif op == "/":
        value = num2 / num1
    elif op == "-":
        value = num2 - num1
    elif op == "^":
        value = math.pow(num2, num1)
    elif op == "%":
        value = num2 % num1
    return value

def isFloat(something):
    try:
        something /= 1
        return True
    except TypeError:
        return False
