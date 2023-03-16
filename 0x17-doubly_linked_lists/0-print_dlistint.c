#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * print_dlistint - prints the nodes of a doubly linked list
 * @h: the dlist header
 *
 * Return: the number of nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *dlist_ptr;
	size_t nodes_count = 0;

	if (h == NULL)
		return (0);

	dlist_ptr = h;
	while (dlist_ptr != NULL)
	{
		printf("%d\n", dlist_ptr->n);
		dlist_ptr = dlist_ptr->next;
		nodes_count += 1;
	}
	return (nodes_count);
}
