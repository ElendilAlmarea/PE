#include "p.h"

int	main(void)
{
	int	nb1;
	int	nb2;
	int	tmp;
	int	sum;

	nb1 = 0;
	nb2 = 1;
	sum = 0;
	while (nb2 <= 10)
	{
		tmp = nb1;
		nb1 = nb2;
		nb2 = tmp + nb2;
		if (nb2 % 2 == 0)
			sum += nb2;
	}
	printf("sum = %d\n", sum);
	return (0);
}
