#include "p.h"

int	main(void)
{
	int		i;
	int		j;
	int		count;
	int		nb;
	int		primes[1000000];
	double	sum;

	nb = 2000000;
	count = 1;
	primes[0] = 2;
	i = 2;
	while (++i < nb)
	{
		j = -1;
		while (++j < count)
		{
			if (i % primes[j] == 0)
				break ;
		}
		if (j == count)
			primes[count++] = i;
	}
	sum = 0;
	i = -1;
	while (++i < count)
		sum += primes[i];
	printf("sum = %f\n", sum);
	return (0);
}
