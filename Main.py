import sys
import time
import Operator
import Tokenizer
import Evaluator

def main(argv=None):
    t = Tokenizer.Tokenizer()
    e = Evaluator.Evaluator()
    if len(argv) == 1:
        try:
            argv = input("Enter an expression: ")
        except [IOError, ValueError]:
            result = "You've entered an invalid expression!"
    else:
        argv = sys.argv[1]
    rpn = t.shunting(argv)
    result = e.evaluate(rpn)
    print(result)

if __name__ == '__main__':
    main(sys.argv)
    
