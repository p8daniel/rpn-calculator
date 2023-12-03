import math

operators = {
    # Common operators
    "+": lambda stack: stack.append(stack.pop() + stack.pop()),
    "-": lambda stack: stack.append(-stack.pop() + stack.pop()),
    "*": lambda stack: stack.append(stack.pop() * stack.pop()),
    "/": lambda stack: stack.append(1 / stack.pop() * stack.pop()),
    "^": lambda stack: stack.append(math.pow(*([stack.pop() for _ in range(2)][::-1]))),
    "%": lambda stack: stack.append(stack.pop() % 1),
    "++": lambda stack: stack.append(stack.pop() + 1),
    "--": lambda stack: stack.append(stack.pop() - 1),
    "/-/": lambda stack: stack.append(-stack.pop()),
    # Numeric operators
    "abs": lambda stack: stack.append(abs(stack.pop())),
    "flr": lambda stack: stack.append(math.floor(stack.pop())),
    "cos": lambda stack: stack.append(math.cos(math.radians(stack.pop()))),
    "lg": lambda stack: stack.append(math.log10(stack.pop())),
    "min": lambda stack: stack.append(min(stack.pop(), stack.pop())),
    "sin": lambda stack: stack.append(math.sin(math.radians(stack.pop()))),
    "ctg": lambda stack: stack.append(1 / math.tan(math.radians(stack.pop()))),
    "ln": lambda stack: stack.append(math.log(stack.pop())),
    "sqr": lambda stack: stack.append(stack.pop() ** 2),
    "eps": lambda stack: stack.append(2 ** (-52)),
    "log": lambda stack: stack.append(math.log(*([stack.pop() for _ in range(2)][::-1]))),
    "pi": lambda stack: stack.append(math.pi),
    "sqrt": lambda stack: stack.append(math.sqrt(stack.pop())),
    "exp": lambda stack: stack.append(math.exp(stack.pop())),
    "max": lambda stack: stack.append(max(stack.pop(), stack.pop())),
    "tg": lambda stack: stack.append(math.tan(math.radians(stack.pop()))),
}


def rpn_calculator(expression) -> float | None:
    """Reverse Polish Notation Calculator"""
    stack = []

    for token in expression.strip().split():
        try:
            stack.append(float(token))
            continue
        except ValueError:
            pass
        if token in operators:
            operators[token](stack)
        else:
            raise ValueError("Invalid operator: {}".format(token))

    return stack.pop() if stack else None
