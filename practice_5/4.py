import itertools

for p in itertools.product("01", repeat=8):
    print(''.join(p))

for p in itertools.permutations("012345", 2):
    print(''.join(str(x) for x in p))

for p in itertools.combinations("012334", 2):
    print(''.join(p))