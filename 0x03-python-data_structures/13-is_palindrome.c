#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * count_nodes - counts nodes
 * @h: pointer to head of list
 * Return: number of nodes
 */

int count_nodes(const listint_t *h)
{
        const listint_t *current;                                  int n; /* number of nodes */                       
        current = h;
        n = 0;
        while (current != NULL)
        {
                current = current->next;
                n++;
        }                                                          return (n);                                        }


/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: beginning if the singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int i, j,  nodes, nodes_split;
	listint_t *current, *crawler;
	listint_t *list_half;

	if (*head == NULL)
		return (1);

	nodes = count_nodes(*head);
	nodes_split = nodes / 2;
	
	if (nodes % 2 != 0)
		return (0);

	current = *head;
	list_half = (listint_t *)malloc(sizeof(listint_t));

	if (list_half == NULL)
		return (0);
	for (i = 1; i < nodes_split; ++i)
		current = current->next;

	list_half = current->next;
	current->next = NULL;
	/*printf("list_half\n");
	print_listint(list_half);
	printf("Head list\n");
	print_listint(*head);*/

	current = NULL;
	crawler = list_half;

	for (i = 0; i < nodes_split; ++i)
	{
		for (j = 0; j < (nodes_split - i - 1); ++j)
		{
			printf("@ i %d j % d \n", i, j);
			print_listint(crawler++);
		}
		
		current = add_nodeint_end(&crawler, crawler->n);
		printf("\n================\ncurrent list\n");
		print_listint(current);
		crawler = list_half;
	}


	return (1);
}



