import math
from Operator import is_op, find

class Tokenizer:
    """Takes an expression in infix notation and converts it to the Reverse
       Polish Notation (RPN) using Dijkstra's Shunting Yard Algorithm"""
       
    # Shunting yard algorithm
    def shunting(self, exp):
        stack = []
        output = []
        tempString = ""
        # Get rid of all spaces for easier computation
        exp = exp.replace(' ','')
        # Mathematical Sin, Cos, Tan functions, decimals and PI are allowed
        validChars = set("sincostanpi.")
        functions = {"sin", "cos", "tan"}
        
        for i in exp:
            # Store chars to see if they're number, function or constant 
            if i.isdigit() or i in validChars:
                tempString += i

            # If tempString is a function, push it onto the stack
            elif tempString in functions:
                stack.append(tempString)

            elif is_op(i):
                # Token transition from number to operator. Get the number
                if len(tempString) > 0:
                    if tempString == "pi":
                        tempString = math.pi
                    output.append(float(tempString))
                    tempString = ""

                # Find what operator it is
                op = find(i)        
                while len(stack) > 0 and i != "(" and i != ")" and \
                      ((op.ass == "l" and (op.pre <= find(stack[-1]).pre)) or \
                       (op.ass == "r" and (op.pre < find(stack[-1]).pre))):
                    output.append(stack.pop())

                if i != ")":
                    stack.append(i)

                elif i == ")":
                    while len(stack) > 0 and stack[-1] != "(":
                        output.append(stack.pop())

                    if stack[-1] == "(":
                        stack.pop()

                    if len(stack) == 0:
                        print("Error: Mismatched parantheses!")
                        break
            else:
                print("Invalid input!")
                break

            print("Output: ", output)
            print("Stack: ", stack)
        
        if len(tempString) > 0:
            if tempString == "pi":
                tempString = math.pi
            output.append(float(tempString))

        while len(stack) > 0:
            output.append(stack.pop())
        
        return output
