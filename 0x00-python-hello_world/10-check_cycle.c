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
	int i, address_counter = 1;
	listint_t *list_crawler;
	char **address_store = (char **)malloc(sizeof(char *) * 1001);

	if (list == NULL || address_store == NULL)
		return (0);
	list_crawler = list;
	address_store[0] = (char *)list_crawler;
	list_crawler = list_crawler->next;

	while (list_crawler)
	{
		for (i = 0; i < address_counter; i++)
		{
			if (address_store[i] == (char *)list_crawler)
			{
				free(address_store);
				return (1); /* Cycle found */
			}
		}
		address_store[address_counter] = (char *)list_crawler;
		address_counter += 1;
		list_crawler = list_crawler->next;
	}
	free(address_store);
	return (0); /* Cycle not found */
}
