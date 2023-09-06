#include "lists.h"
/**
* check_cycle - chech the liked list if it has cycle or not
* @list: the lineed list
* Return: 0 if its true 1 if false
*/
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}

	return (0);

}
