#include "p.h"

int	main(void)
{
	int		nb[10000];
	double	i;
	double	count;
	double	max;
	double	nb_max;
	double	n;
	double	rly;

	i = -1;
	while (++i < 10000)
		nb[(int)i] = 0;
	max = 0;
	i = 0;
	while (++i < 1000000)
	{
		printf("%f\n", i);
		n = i;
		count = 0;
		while (n != 1)
		{
			if (n < 10000)
			{
				if (nb[(int)n])
				{
					if (i < 10000)
						nb[(int)i] = nb[(int)n] + count;
					break ;
				}
			}
			rly = n;
			while (rly > 2147483647.0)
				rly -= 2147483646;
			if ((int)rly % 2)
				n = 3 * n + 1;
			else
				n = n / 2;
			count++;
		}
		if (n == 1)
			if (i < 10000)
				nb[(int)i] = count;
		if (count > max)
		{
			nb_max = i;
			max = count;
		}
	}
	printf("%f\n", nb_max);
	return (0);
}
