count = 0
for i in range(0, 10):
    for ii in range(0, 10):
        if ii == i:
            continue
        for iii in range(0, 10):
            if iii == i or iii == ii:
                continue
            for iiii in range(0, 10):
                if iiii == i or iiii == ii or iiii == iii:
                    continue
                for iiiii in range(0, 10):
                    if iiiii == i or iiiii == ii or iiiii == iii or iiiii == iiii:
                        continue
                    for iiiiii in range(0, 10):
                        if iiiiii == i or iiiiii == ii or iiiiii == iii or iiiiii == iiii or iiiiii == iiiii:
                            continue
                        for iiiiiii in range(0, 10):
                            if iiiiiii == i or iiiiiii == ii or iiiiiii == iii or iiiiiii == iiii or iiiiiii == iiiii or iiiiiii == iiiiii:
                                continue
                            for iiiiiiii in range(0, 10):
                                if iiiiiiii == i or iiiiiiii == ii or iiiiiiii == iii or iiiiiiii == iiii or iiiiiiii == iiiii or iiiiiiii == iiiiii or iiiiiiii == iiiiiii:
                                    continue
                                for iiiiiiiii in range(0, 10):
                                    if iiiiiiiii == i or iiiiiiiii == ii or iiiiiiiii == iii or iiiiiiiii == iiii or iiiiiiiii == iiiii or iiiiiiiii == iiiiii or iiiiiiiii == iiiiiii or iiiiiiiii == iiiiiiii:
                                        continue
                                    for iiiiiiiiii in range(0, 10):
                                        if iiiiiiiiii == i or iiiiiiiiii == ii or iiiiiiiiii == iii or iiiiiiiiii == iiii or iiiiiiiiii == iiiii or iiiiiiiiii == iiiiii or iiiiiiiiii == iiiiiii or iiiiiiiiii == iiiiiiii or iiiiiiiiii == iiiiiiiii:
                                            continue
                                        count += 1
                                        if count == 1000000:
                                            print("{}{}{}{}{}{}{}{}{}{}".format(i, ii, iii, iiii, iiiii, iiiiii, iiiiiii, iiiiiiii, iiiiiiiii, iiiiiiiiii))
                                            exit()