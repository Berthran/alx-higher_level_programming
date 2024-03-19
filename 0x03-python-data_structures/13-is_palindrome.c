#include "lists.h"
#include <stdio.h>
#include <string.h>

int count_nodes(const listint_t *h);

/*int compare_list(listint_t *l1, listint_t *l2, int n);*/

int compare_odd(listint_t *head, int nodes);

int compare_even(listint_t *head, int nodes);

int compare_list(listint_t *head, int n_nodes);

/**
 * count_nodes - counts nodes
 * @h: pointer to head of list
 * Return: number of nodes
 */

int count_nodes(const listint_t *h)
{
	/*const listint_t *current;
	int n;

	current = h;
	n = 0;

	while (current != NULL)
	{
		current = current->next;
		n++;
	}*/
	if (h == NULL)
		return (0);
	return (1 + count_nodes(h->next));
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
	int nodes; /* is_p;*/

	/* Empty list is a palindrome */
	if (*head == NULL)
		return (1);

	nodes = count_nodes(*head);
	/* List with one item is a palindrome */
	if (nodes == 1)
		return (1);

	/* Determine if nodes are even or odd
	if (nodes % 2 == 0)
		is_p = compare_even(*head, nodes);
	else
		is_p = compare_odd(*head, nodes);*/

	/*nodes_split = (nodes / 2);

	first_half = crawler = *head;

	for (i = 1; i < nodes_split; ++i)
		crawler = crawler->next;

	second_half = crawler->next;
	crawler->next = NULL;*/

	if (compare_list(*head, nodes) == 0)
		return (0);
	return (1);
	/*return (is_p);*/
}


/**
 * compare_list - compares the value of two linked lists
 * @head: the pointer to the linked list
 * @n_nodes: the number of nodes in each list
 *
 * Return: 1 if all the nodes have thesame value for both linked lists
 */

int compare_list(listint_t *head, int n_nodes)
{
	int i, j, n1, n2;
	listint_t *c1, *c2, *oddHalf, *evenHalf;
	int jump = n_nodes / 2;
	int half = (n_nodes / 2) - 1;
	char *dtype = NULL;
	c1 = c2 = oddHalf = evenHalf = head;

	if (n_nodes % 2 == 0)
	{
		dtype = "even";
		for (i = 0; i < (half + 1); i++)
			evenHalf = evenHalf->next;
	}
	else
	{
		dtype = "odd";
		for (i = 0; i < (jump + 1); i++)
		       oddHalf = oddHalf->next;
	}

	if (strcmp(dtype, "odd") == 0)
	{
		c2 = oddHalf;

		for (i = 0; i < jump; i++)
		{
			n1 = c1->n;
			for (j = 0; j < (jump - i - 1); j++)
				c2 = c2->next;
			n2 = c2->n;
			if (n1 != n2)
				return (0);
			c1 = c1->next;
			c2 = oddHalf;
		}

	}
	else
	{
		c2 = evenHalf;

		for (i = 0; i < half; i++)
		{
			n1 = c1->n;
			for (j = 0; j < (half - i); j++)
				c2 = c2->next;
			n2 = c2->n;
			if (n1 != n2)
				return (0);
			c1 = c1->next;
			c2 = evenHalf;
		}
	}
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
	listint_t *crawler; /* *first_half, *second_half;*/
	int i, jump = nodes / 2;
	int sum = 0;
	crawler = head;

	for (i = 0; i < nodes; i++)
	{
		if (i == jump)
			crawler = crawler->next;
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

