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
	listint_t *node_crawler, *temp_node;

	if (list == NULL)
		return (0);

	node_crawler = temp_node = list;
	node_crawler = list->next;

	if (node_crawler == NULL)
		return (1); /* One node so no cycle */

	if (node_crawler > temp_node)
	{
		while (node_crawler)
		{
			if (node_crawler->next <= temp_node)
				return (1); /* Cycle exits */
			temp_node = node_crawler;
			node_crawler = node_crawler->next;
		}
	}

	else if (node_crawler < temp_node)
	{
		while (node_crawler)
		{
			if (node_crawler->next >= temp_node)
				return (1); /* Cycle exists */
		temp_node = node_crawler;
		node_crawler = node_crawler->next;
		}
	}
	return (0); /* Cycle not found */
}
