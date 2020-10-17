from collections.abc import Hashable
# object_list = [1, 397, 27468, -95, 1309, 397, -539874, -240767, -95, 397]
h_dict = {}

for el in object_list:
    if isinstance(el, Hashable):
        if hash(el) in h_dict:
            h_dict[hash(el)] += 1
        else:
            h_dict[hash(el)] = 1

print(sum([x for x in h_dict.values() if x > 1]))


