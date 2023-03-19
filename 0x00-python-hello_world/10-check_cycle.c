#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if singly linked list has a cycle in it
 * @list: pointer to beginnig of the list
 *
 * Return: 1, if there's a circle, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	int i, node_counter = 1;
	listint_t *node_crawler, *temp_node, *reset_node;

	if (list == NULL)
		return (0);
	node_crawler = temp_node = reset_node = list;
	node_crawler = list->next;

	while (node_crawler)
	{
		for (i = 0; i < node_counter; i++)
		{
			if (temp_node == node_crawler)
				return (1); /* Cycle found */
			temp_node = temp_node->next;
		}
		temp_node = reset_node;
		node_counter += 1;
		node_crawler = node_crawler->next;
	}
	return (0); /* Cycle not found */
}
