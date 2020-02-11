#include "p.h"
/*
int	main(void)
{
	int	digit[10] = {0, 3, 3, 5, 4, 4, 3, 5, 5, 4};
	int	dec[10] = {0, 3, 6, 6, 6, 5, 5, 7, 6, 6};
	int	i;
	int	j;
	int	k;
	int	sum;

	sum = 11;
	i = -1;
	while (++i < 10)
	{
		j = -1;
		while (++j < 10)
		{
			k = -1;
			while (++k < 10)
			{
				sum += digit[i] + 10 + dec[j] + digit[k];
				if (i == 0)
					sum -= 10;
				else if (j == 1 && (k == 4 || k == 6))
					sum += 1;
				else if (i && !j && !k)
					sum -= 3;
			}
		}
	}
	printf("%d\n", sum);
	return (0);
}
*/