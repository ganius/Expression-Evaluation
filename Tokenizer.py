import math
from Operator import is_op, find

class Tokenizer:
    """Has a single method which tokenizes the given input and returns
    the resulting output. Not to be confused with Britney Spears song!"""
    
    def shunting(self, exp):
        """Takes an expression in infix notation and converts it to the Reverse
        Polish Notation (RPN) using Dijkstra's Shunting Yard Algorithm."""
        stack = []
        output = []
        tempString = ""
        # Get rid of all spaces for easier computation
        exp = exp.replace(' ','')
        # Mathematical Sin, Cos, Tan functions, decimals and PI are allowed
        validChars = set("sincostanpi.")
        validOutput = True
        functions = {"sin", "cos", "tan"}

        # Tokenize the expression char by char
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
                
                # Remove operators from stack onto output according to
                # their associativity and precedence
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
                        output = "Error: Mismatched parantheses!"
                        validOutput = False
                        break
            else:
                output = "Invalid input!"
                validOutput = False
                break

        # Remaining tokens are added to output (if any)
        if len(tempString) > 0 and validOutput:
            if tempString == "pi":
                tempString = math.pi
            output.append(float(tempString))

        # Remaining operators in the stack are added to the output.
        while len(stack) > 0:
            if stack[-1] == "(" or stack[-1] == ")":
                output = "Invalid input!"
                break
            if validOutput:
                output.append(stack.pop())
        
        return output
