from collections import deque
import re
infix = ": * 3 + 12 * (4 - 2)"
#
# inp = [i for i in re.split('(\D)', infix) if i not in " "]
# print(inp)
#
#
# gen = (True if i.isalnum() or i in "-+*/()" else False for i in inp)
# print(gen)
# print(all(gen))

# exp ="4 * (2 + 3"
# print(not ((re.search('[a-zA-Z0-9]', exp[-1])) or (exp.count("(") == exp.count(")"))
#             or all((True if i.isalnum() or i in "-+*/()" else False for i in exp))))

# print([True if i.isalnum() or i in " -+*/()" else False for i in "8 * 3 + 12 * (4 - 2)"])

while True:
    inp = input().lstrip()
    print(inp)