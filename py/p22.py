abundant, sum_abundant = [], []
sum1 = 276
for i in range(2, 28124):
	print("{}".format(i))
	sum1 = 1
	for j in range(2, i):
		if (i % j == 0):
			sum1 += j
	if i < sum1:
		abundant.append(i)
sum1 = 0
for a1 in abundant:
	for a2 in abundant:
		sum_abundant.append(a1 + a2)
sorted(sum_abundant)
for i in range(0, len(sum_abundant) - 1):
	if sum_abundant[i] == sum_abundant[i + 1]:
		del sum_abundant[i]
for i in range(0, len(sum_abundant) - 1):
	if sum_abundant[i + 1] - sum_abundant[i] != 1:
		insert(i + 1, 0)
for i in range(24, 28124):
	if not bool(abundant[i - 24]):
		sum += i
print("{}".format(sum1))