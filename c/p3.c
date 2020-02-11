#include "p.h"

int	main(void)
{
	int		i;
	int		j;
	int		count;
	int		primes[1000000];
	int		sqrt_nb;

	sqrt_nb = (int)sqrt(600851475143) + 1;
	count = 1;
	primes[0] = 2;
	i = 2;
	while (++i < sqrt_nb)
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
	while (--count >= 0)
	{
		if (600851475143 % primes[count] == 0)
			break;
	}
	if (count == -1)
		printf("largest prime factor = %d\n", 600851475143);
	else
		printf("largest prime factor is = %d\n", primes[count]);
}