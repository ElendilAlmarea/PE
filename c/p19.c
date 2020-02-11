#include "p.h"

int	main(void)
{
	int	y;
	int	m;
	int	d;
	int	sum;

	sum = 0;
	d = 0;
	y = 0;
	while (++y < 101)
	{
		m = -1;
		while (++m < 12)
		{
			if (d % 7 == 5)
				sum++;
			if (m == 3 || m == 5 || m == 8 || m == 10)
				d += 30;
			else if (m == 1)
			{
				if (y % 4 == 0)
					d += 29;
				else
					d += 28;
			}
			else
				d += 31;
		}
	}
	printf("%d\n", sum);
	return (0);
}
