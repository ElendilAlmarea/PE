#include "p.h"

int	main(void)
{
	int	i;
	int	j;

	i = 0;
	while (++i)
	{
		j = 1;
		while (++j < 21)
			if (i % j)
				break ;
		if (j == 21)
			break ;
	}
	printf("nb = %d\n", i);
	return (0);
}
