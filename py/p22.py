abundant = []
sum1, check, ch = 0, bool(0), bool(0)
for i in range(2, 28124):
	print("{}".format(i))
	sum1 = 1
	for j in range(2, i):
		if (i % j == 0):
			sum1 += j
	if i < sum1:
		abundant.append(i)
sum1 = 0
for i in range(2, 28124):
	print("{}".format(i))
	check = bool(0)
	ch = bool(0)
	for a1 in abundant:
		if check:
			break
		for a2 in abundant:
			if a1 > i and a2 > i:
				check = bool(1)
				ch = bool(1)
			if a2 > i:
				break
			if check:
				break
			if a1 + a2 == i:
				check = bool(1)
	if not check or ch:
		sum1 += i
print("{}".format(sum1))