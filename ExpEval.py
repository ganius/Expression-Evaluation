import sys
import Operator
import Tokenizer
import Evaluator

def main():
    t = Tokenizer.Tokenizer()
    e = Evaluator.Evaluator()
    try:
        exp = str(input("Enter expression: "))
        rpn = t.shunting(exp)
        result = e.evaluate(rpn)
        print(result)
    except IOError:
        print("I/O error")

if __name__ == '__main__':
    main()
