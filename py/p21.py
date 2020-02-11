sum, sum2, sum3 = 0, 0, 0
for i in range(2, 10000):
	sum = 0
	for j in range(1, i):
		if i % j == 0:
			sum += j
	sum2 = 0
	for j in range(1, sum):
		if sum % j == 0:
			sum2 += j
	if sum2 == i and i != sum:
		sum3 += i
print("%d" % sum3)