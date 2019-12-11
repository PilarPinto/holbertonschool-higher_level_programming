#include "lists.h"
#include<stdio.h>

/**
 *insert_node - inserts a number into a sorted singly linked list.
 *
 *@head: pointer that point to head of list
 *@number: element to store inside new node
 *Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *element, *guide;

	element = NULL;

	if (!head)
		return (NULL);

	element = malloc(sizeof(listint_t));
	if (!element)
		return (NULL);

	/* element->n = number; */
	(*element).n = number;
	guide = *head;
	if (*head == NULL)
	{
		*head = element;
		element->next = NULL;
	}
	else if (number < guide->n)
	{
		element->next = guide;
		*head = element;
	}
	else
	{
		while (guide->next && number > guide->next->n)
		{
			guide = guide->next;
		}
		element->next = guide->next;
		guide->next = element;
	}

	return (element);
}
