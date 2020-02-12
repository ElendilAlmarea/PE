abundant, sum_abundant = [], [0] * 56250
sum1 = 0
for i in range(2, 28124):
	sum1 = 1
	for j in range(2, i):
		if i % j == 0:
			sum1 += j
	if i < sum1:
		abundant.append(i)
for a1 in abundant:
	for a2 in abundant:
		sum_abundant[a1 + a2] = 1
sum1 = 0
for i in range(1, 28124):
	if sum_abundant[i] == 0:
		sum1 += i
print("{}".format(sum1))