# create your dictionary here
objects_dict = {}

for el in objects:
    try:
        objects_dict[el] = hash(el)
    except TypeError:
        continue
