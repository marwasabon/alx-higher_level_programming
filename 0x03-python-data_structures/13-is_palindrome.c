#include "lists.h"
/**
 * is_palindrome:checks if a singly linked list is a palindrome.
 * @head: pointer to pointer of first node of listint_t list.
 * Return: 1 if the list is plaindrome or 0 if its not.
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL)
	{
		return (1);
	}
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow->next = prev;
		prev = slow;
	}
	if (fast)
	{
		slow = slow->next;
	}
	listint_t *current = slow;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	listint_t *left = *head;
	listint_t *right = prev;

	while (right)
	{
		if (left->n != right->n)
		{
			return (0);
		}
		left = left->next;
		right = right->next;
	}
	return (1);
}
