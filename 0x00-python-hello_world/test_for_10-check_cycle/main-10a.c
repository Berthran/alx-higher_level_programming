#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <time.h>
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
	listint_t *head;
	clock_t start;
	clock_t end;
	clock_t diff;
	int i;

	head = NULL;
	for (i = 0; i < 1001; i++)
		add_nodeint(&head, i);

	start = clock();

	for (i = 0; i < 1000; i++)
	        check_cycle(head);

	end = clock();

	diff = (double)(end - start) / 10;

	if (diff > 40)
	{
		printf("Runtime is %ld\n", diff * 10);
		printf("Runtime too long\n");
	}
	else
	{
		printf("Runtime is %ld\n", diff * 10);
		printf("OK\n");
	}

	free_listint(head);

	return (0);
}
