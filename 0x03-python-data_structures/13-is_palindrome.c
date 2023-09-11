#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to pointer of first node of listint_t list.
 * Return: 1 if the list is plaindrome or 0 if its not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *temp;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		temp = slow;
		slow = slow->next;
		temp->next = prev;
		prev = temp;
	}

	if (fast != NULL)
		slow = slow->next;

	while (slow != NULL)
	{
		if ((*head)->n != slow->n)
			return (0);
		*head = (*head)->next;
		slow = slow->next;
	}

	return (1);
}
