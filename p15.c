#include "p.h"
# define SIZE 515

/*
void	rec(int i, int j, double *res, int size)
{
	if (i < size)
		rec(i + 1, j, res, size);
	if (j < size)
		rec(i, j + 1, res, size);
	if (i == size && j == size)
		(*res)++;
}

int		main(void)
{
	double	res;
	int		size;

	size = 0;
	while (++size < 22)
	{
		res = 0;
		rec(0, 0, &res, size);
		printf("%dx%d grid = %f paths\n", size + 1, size + 1, res);
	}
	return (0);
}

*/

void	rec(int i, int j, double *res, int size, double *grid)
{
	if (grid[(size - i) * SIZE + j])
		*res += grid[(size - i) * SIZE + j];
	else
	{
		if (i < size)
			rec(i + 1, j, res, size, grid);
		if (j < SIZE)
			rec(i, j + 1, res, size, grid);
	}
}

int		main(void)
{
	double	res;
	int		i;
	int		j;
	double	grid[(SIZE + 2) * (SIZE + 2)];

	i = -1;
	while (++i < (SIZE + 2) * (SIZE + 2))
		grid[i] = 0;
	grid[SIZE] = 1.0;
	i= -1;
	while (++i < SIZE)
	{
		j = SIZE + 1;
		while (--j >= 0)
		{
			res = 0;
			rec(0, j, &res, i, grid);
			grid[i * SIZE + j] = res;
		}
		printf("%dx%d grid = %f paths\n\n", i, i, grid[i * SIZE + SIZE - i]);
	}
	return (0);
}
