#include "lists.h"
#include<stdio.h>
/**
 *insert_node - Insert a node in a list
 * @head: Is the point where are the node
 * @number: Is the element number in the node
 * Return:The adress and the insert node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_n *n_node, *guide;

	n_node = NULL;

	if (!head)
		return (NULL);

	n_node = malloc(sizeof(listint_t));
	if (!n_node)
		return (NULL);

	n_node->n = number;
	guide = *head;

	if (*head == NULL)
	{
		*head = n_node;
		n_node->next = NULL;
	}
	else if (number < guide->n)
	{
		n_node->next = guide;
		*head = n_node;
	}
	else
	{
		while (guide->next && number > guide->next->n)
			guide = guide->next;

		n_node->next = guide->next;
		guide->next = n_node;

	}

	return (n_node);
}
