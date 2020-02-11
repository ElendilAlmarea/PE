#include "p.h"

int	main(void)
{
	int	a;
	int	b;
	int	c;
	int	i;
	int	ii;
	int	iii;

	i = 0;
	while (++i < 1000)
	{
		ii = 0;
		while (++ii < 1000)
		{
			iii = 0;
			while (++iii < 1000)
			{
				if (i + ii + iii == 1000)
				{
					if (i * i + ii * ii == iii * iii)
					{
						printf("product = %d\n", i * ii * iii);
						return (0);
					}
				}	
			}
		}
	}
	return (0);
}
