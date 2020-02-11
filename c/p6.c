#include "p.h"

int	main(void)
{
	int	i;
	int	sqr;
	int	sum;

	sqr = 0;
	sum = 0;
	i = 0;
	while (++i < 101)
	{
		sqr += i * i;
		sum += i;
	}
	sum *= sum;
	printf("result = %d\n", sum - sqr);
	return (0);
}
