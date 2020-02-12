f1, f2, po, index = 0, 1, 10**999, 1
while (f2 < po):
    f1, f2 = f2, f1 + f2
    index += 1
print("{}".format(index))