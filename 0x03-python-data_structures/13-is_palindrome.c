#include "lists.h"
#include <stdio.h>
#include <string.h>

int count_nodes(const listint_t *h, int count);

/*int compare_list(listint_t *l1, listint_t *l2, int n);*/

int compare_odd(listint_t *head, int nodes);

int compare_even(listint_t *head, int nodes);

int compare_list(listint_t *head, int n_nodes);

listint_t *reverse_list(listint_t **head);

/**
 * count_nodes - counts nodes
 * @h: pointer to head of list
 * Return: number of nodes
 */
int count_nodes(const listint_t *h, int count)
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
		return (count);
	/*return (1 + count_nodes(h->next));*/
	return count_nodes(h->next, count + 1);
}

/**
 * reverse_list - reverses the nodes in a singly linked list
 * @head: the starting position of the linked list
 *
 * Return: a reversed linked list
 */

int is_palindrome(listint_t **head)
{
	listint_t *current, *prev, *next;
	int num[2048], i = 0, j = 0, split, m, n;

	if (*head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (1);

	prev = next = NULL;
	current = *head;

	while (current !=  NULL)
	{
		num[i++] = current->n;
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	split = i / 2;

	while (prev != NULL && j < split)
	{
		m = num[j];
                n = prev->n;
                if (m != n)
                        return (0);
                prev = prev->next;
		j++;
        }
	return (1);
}


/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: beginning if the singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

/*{
	*listint_t *crawler; * *first_half, *second_half;*/
	/*int nodes = 0;*/
	/*int i, j;
	static listint_t *reverse;
	listint_t *forward, *backward;
	(void)reverse;

	* Empty list is a palindrome *
	if (*head == NULL)
		return (1);

	*nodes = count_nodes(*head);*/
	/*nodes = count_nodes(*head, nodes);*/
	/* List with one item is a palindrome */
	/*if ((*head)->next == NULL)
		return (1);

	*head = reverse_list(head);
	exit(98);
	backward = reverse;

	while (*head != NULL)
	{
		printf("head->n = %d\n", (*head)->n);
		*head = (*head)->next;
	}
	while (reverse != NULL)
        {
                printf("reverse->n = %d\n", reverse->n);
                reverse = reverse->next;
        }
	exit(98);

	while (forward != NULL)
	{
		i = forward->n;
		j = backward->n;
		printf("i = %d, j = %d\n", i, j);
		if (i != j)
			return (0);
		forward = forward->next;
		backward = backward->next;
	}
	return (1);

	* Determine if nodes are even or odd
	if (nodes % 2 == 0)
		is_p = compare_even(*head, nodes);
	else
		is_p = compare_odd(*head, nodes);*/

	/*nodes_split = (nodes / 2);

	first_half = crawler = *head;

	for (i = 1; i < nodes_split; ++i)
		crawler = crawler->next;

	second_half = crawler->next;
	crawler->next = NULL;

	if (compare_list(*head, nodes) == 0)
		return (0);
	return (1);
	return (is_p);*/


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

