#include "lists.h"
#include <stdio.h>

int count_nodes(const listint_t *h);

int compare_list(listint_t *l1, listint_t *l2, int n);

int compare_odd(listint_t *head, int nodes);

int compare_even(listint_t *head, int nodes);

/**
 * count_nodes - counts nodes
 * @h: pointer to head of list
 * Return: number of nodes
 */

int count_nodes(const listint_t *h)
{
	const listint_t *current;
	int n;

	current = h;
	n = 0;

	while (current != NULL)
	{
		current = current->next;
		n++;
	}
	return (n);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: beginning if the singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	/*listint_t *crawler; * *first_half, *second_half;*/
	int nodes, is_p;

	/* Empty list is a palindrome */
	if (*head == NULL)
		return (1);

	nodes = count_nodes(*head);
	/* List with one item is a palindrome */
	if (nodes == 1)
		return (1);

	/* Determine if nodes are even or odd */
	if (nodes % 2 == 0) /* even */
		is_p = compare_even(*head, nodes);
	else
		is_p = compare_odd(*head, nodes);

	/*nodes_split = (nodes / 2);

	first_half = crawler = *head;

	for (i = 1; i < nodes_split; ++i)
		crawler = crawler->next;

	second_half = crawler->next;
	crawler->next = NULL;

	if (compare_list(first_half, second_half, nodes_split) == 0)
		return (0);
	return (1);*/
	return (is_p);
}


/**
 * compare_list - compares the value of two linked lists
 * @l1: the first linked list
 * @l2: the second linked list
 * @n: the number of nodes in each list
 *
 * Return: 1 if all the nodes have thesame value for both linked lists
 */

int compare_list(listint_t *l1, listint_t *l2, int n)
{
	int i, j, n1, n2;
	listint_t *c1, *c2;

	c1 = l1;
	c2 = l2;

	for (i = 0; i < n; i++)
	{
		n1 = c1->n;
		for (j = 0; j < (n - i - 1); j++)
			c2 = c2->next;

		n2 = c2->n;

		if (n1 != n2)
			return (0);

		c1 = c1->next;
		c2 = l2;
	}
	free_listint(l2);
	return (1);
}


/**
 * compare_odd - checks if an odd numbered linked list is a palindrome
 * @head: the pointer to the linked list
 * @nodes: the number of nodes in the linked list
 *
 * Return: 1 if it is a palindrome or 0 if not
 */

int compare_odd(listint_t *head, int nodes)
{
	listint_t *crawler, *temp; /* *first_half, *second_half;*/
	int i, jump = nodes / 2;
	int sum = 0;
	crawler = head;

	for (i = 0; i < nodes; i++)
	{
		temp = crawler;
		if (i == jump)
		{
			if (temp->n != crawler->next->n)
				return (0);
			crawler = crawler->next;
		}
		else if (i < jump)
		{
			sum += crawler->n;
			crawler = crawler->next;
		}
		else if (i > jump)
		{
			sum -= crawler->n;
			crawler = crawler->next;
		}
	}
	if (sum == 0)
		return (1);
	return (0);
}


/**
 * compare_even - checks if an even numbered linked list is a palindrome
 * @head: the pointer to the linked list
 * @nodes: the number of nodes in the linked list
 *
 * Return: 1 if it is a palindrome or 0 if not
 */

int compare_even(listint_t *head, int nodes)
{
	listint_t *crawler;
	int i, half = (nodes / 2) - 1;
	int sum = 0;
	crawler = head;

	for (i = 0; i < nodes; i++)
	{
		if (i <= half)
		{
			sum += crawler->n;
			crawler = crawler->next;
		}
		else if (i > half)
		{
			sum -= crawler->n;
			crawler = crawler->next;
		}
	}
	if (sum == 0)
		return (1);
	return (0);
}

