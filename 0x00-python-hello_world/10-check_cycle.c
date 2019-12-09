#include "lists.h"
/**
 * check_cycle - Check if a lopp exist in the linked list
 * @list: Is the pointer to the structure
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_p = list;
	listint_t *fast_p = list;

	fast_p = fast_p->next;

	while (slow_p != NULL && fast_p != NULL && fast_p->next != NULL)
	{
		if (fast_p == slow_p)
			return (1);
		fast_p = fast_p->next->next;
		slow_p = slow_p->next;
	}
	return (0);
}
