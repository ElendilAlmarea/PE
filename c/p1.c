#include "p.h"

int	main(void)
{
	int	sum;
	int	i;

	sum = 0;
	i = 0;
	while (++i < 1000)
	{
		if (i % 3 == 0)
			sum += i;
		else if (i % 5 == 0)
			sum += i;
	}
	printf("sum = %d\n", sum);
	return (0);
}
