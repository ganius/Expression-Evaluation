class Operator:
    """An operator class"""
    
    allOperators = []
    
    def __init__(self, associativity, symbol, precedence, operands):
        # left (l) or right (r)
        self.ass = associativity
        self.sym = symbol
        self.pre = precedence
        self.ops = operands
        Operator.allOperators.append(self)

plus = Operator("l", "+", 1, 2)
minus = Operator("l", "-", 1, 2)
divide = Operator("l", "/", 2, 2)
modulus = Operator("l", "%", 2, 2)
multiply = Operator("l", "*", 2, 2)
power_of = Operator("r", "^", 3, 2)
left_paran = Operator("l", "(", -1, 0)
right_paran = Operator("l", ")", -1, 0)

def is_op(symbol):
    for op in Operator.allOperators:
        if op.sym == symbol:
            return True
    return False

def find(symbol):
    for op in Operator.allOperators:
        if op.sym == symbol:
            return op
