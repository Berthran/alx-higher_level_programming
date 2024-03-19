#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: beginning if the singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
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
