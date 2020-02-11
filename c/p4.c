#include "p.h"

int	main(void)
{
	int	nb1;
	int	nb2;
	int	res;
	int	final;

	final = 0;
	nb1 = 1000;
	while (--nb1 > 0)
	{
		nb2 = 1000;
		while (--nb2 > 0)
		{
			res = nb1 * nb2;
			if (res > 100000)
			{
				if (res / 100000 == res % 10 && (res - res / 100000 * 100000) / 10000 == res % 100 / 10 && res % 10000 / 1000 == res % 1000 / 100)
				{
					if (res > final)
					{
						final = res;
					}
				}
			}
		}
	}
	printf("nb1 = %d\n", final);
	return (0);
}
