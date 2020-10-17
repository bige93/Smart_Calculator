from collections import deque
import re


def mult(exp):
    x, y = exp.split("*")
    res = str(float(x) * float(y))
    return res


def div(exp):
    x, y = exp.split("/")
    res = str(float(x) / float(y))
    return res


def plus(exp):
    x, y = exp.split("+")
    res = str(float(x) + float(y))
    return res


def minus(exp):
    x, y = exp.split("-")
    res = str(float(x) - float(y))
    return res


def to_postfix(infix):
    stack = deque()
    postfix = []
    infix_list = [i for i in re.split('(\D)', infix) if i not in " "]

    def higher_precedence(i, j):
        if i in "*/":
            i = 2
        else:
            i = 1
        if j in "*/":
            j = 2
        else:
            j = 1
        return i > j

    def lower_or_equal_precedence(i, j):
        if i in "*/":
            i = 2
        else:
            i = 1
        if j in "*/":
            j = 2
        else:
            j = 1
        return i <= j

    for c in infix_list:
        if c.isalnum():
            postfix.append(c)
        elif len(stack) == 0 or stack[-1] == "(":
            stack.append(c)
        elif c in "+-*/":
            if higher_precedence(c, stack[-1]):
                stack.append(c)
            elif lower_or_equal_precedence(c, stack[-1]):
                while len(stack) != 0 and (stack[-1] != "(" or higher_precedence(stack[-1], c)):
                    postfix.append(stack.pop())
                stack.append(c)
        elif c == "(":
            stack.append(c)
        elif c == ")":
            while stack[-1] != "(":
                postfix.append(stack.pop())
            stack.pop()
    while stack:
        postfix.append(stack.pop())
    return postfix


def to_infix(postfix):
    stack = deque()
    for c in postfix:
        if c.isalnum():
            if c.isalpha():
                try:
                    stack.append(my_dict[c])
                except KeyError:
                    print(f'Variable "{c}" not found')
                    break
            else:
                stack.append(c)
        elif c in "+":
            y = stack.pop()
            x = stack.pop()
            _ = x + c + y
            stack.append(plus(_))
        elif c == "-":
            y = stack.pop()
            x = stack.pop()
            _ = x + c + y
            stack.append(minus(_))
        elif c == "*":
            y = stack.pop()
            x = stack.pop()
            _ = x + c + y
            stack.append(mult(_))
        elif c == "/":
            y = stack.pop()
            x = stack.pop()
            _ = x + c + y
            stack.append(div(_))
    result = float(stack.pop())
    return round(result)


def normalize():
    global inp
    if not any((True if i.isalpha() else False for i in inp)):
        inp = inp.split()
        for i in inp:
            if "-" in i:
                if len(i) % 2 == 0:
                    inp[inp.index(i)] = "+"
                else:
                    inp[inp.index(i)] = "-"
            elif "+" in i:
                inp[inp.index(i)] = "+"
        inp = "".join(inp)


def not_valid(exp):
    if not exp.count("(") == exp.count(")"):
        return True
    elif not all((True if i.isalnum() or i in " -+*/()" else False for i in exp)):
        return True
    elif exp[-1] != ")" and not exp[-1].isalnum():
        return True
    elif len(exp.split()) == 3 and (exp.split()[1] in "*" or "/") and len(exp.split()[1]) > 1:
        return True
    elif len(exp) == 2 and not exp.isnumeric():
        return True
    else:
        return False


my_dict = {}
while True:
    inp = input().lstrip()
    if "=" in inp or inp.isalpha():
        if inp.isalpha():
            try:
                print(my_dict[inp.strip()])
                continue
            except KeyError:
                print("Unknown variable")
                continue
        expression = inp.split("=")
        if not expression[0].strip().isalpha():
            print("Invalid identifier")
        elif not (expression[1].strip().isdigit() or expression[1].strip().isalpha()) or len(expression) > 2:
            print("Invalid assignment")
        else:
            if expression[1].strip() in my_dict.keys():
                my_dict[expression[0].strip()] = my_dict[expression[1].strip()]
            else:
                if expression[1].strip().isalpha():
                    print("Unknown variable")
                else:
                    my_dict[expression[0].strip()] = expression[1].strip()
        continue

    if inp:
        if inp[0] == "/":
            if inp == '/exit':
                print("Bye!")
                exit(0)
            elif inp == '/help':
                print("The program calculates the sum of numbers")
                continue
            else:
                print("Unknown command")
                continue
        elif inp[0] == "+" or inp[0] == "-":
            print(inp)
            continue

        if not_valid(inp):
            print("Invalid expression")
            continue
        else:
            normalize()
            print(to_infix(to_postfix(inp)))
            continue
    else:
        pass
