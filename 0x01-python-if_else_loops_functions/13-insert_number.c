#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - adds a node to a sorted linked list
 * @head: the head of the linked list
 * @number: integer value of new node
 *
 * Return: address of new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node_crawler, *prev_node;
	int n, node_counter = 1;
	listint_t *new_node = (listint_t *)malloc(sizeof(listint_t));

	if (*head == NULL || new_node == NULL)
		return (NULL);

	node_crawler = *head;
	new_node->n = number;

	while (node_crawler)
	{
		n = node_crawler->n;
		if (n > number)
		{
			new_node->next = node_crawler;
			if (node_counter == 1)
			{
				*head = new_node;
				return (*head);
			}
			prev_node->next = new_node;
			return (*head);
		}
		else
		{
			prev_node = node_crawler;
			node_crawler = node_crawler->next;
			node_counter += 1;
		}
	}
	prev_node->next = new_node;
	return (*head);
}
