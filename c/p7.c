#include "p.h"

int	main(void)
{
	int		i;
	int		j;
	int		count;
	int		nb;
	int		primes[1000000];

	nb = 1000000;
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
	if (count >= 10000)
		printf("res = %d\n", primes[10000]);
	else
		printf("increase nb\n");
	return (0);
}
