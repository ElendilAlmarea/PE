#include "p.h"

int	main(void)
{
	int		i;
	int		j;
	int		divider;
	int		sum;

	sum = 0;
	i = 0;
	while (++i)
	{
		sum += i;
		if (sum % 60)
			continue;
		divider = 0;
		j = 0;
		while (++j <= sum)
		{
			if (sum % j == 0)
				divider++;
			if (divider > 500)
			{
				printf("sum = %d\n", sum);
				return (0);
			}
		}
	}
	return (0);
}
