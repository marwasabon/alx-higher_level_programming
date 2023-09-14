#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>
/**
 * print_dlistint - prints all the elements of a dlistint_t list.
 * @h: the linked list
 * Return: number of nodes in the linked list.
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t i;

	if (!h)
		return (0);

	while (h->prev != NULL)
		h = h->prev;

	for (i = 0; h != NULL; i++)
	{
		printf("%d\n", h->n);
		h = h->next;
	}
	return (i);
}
