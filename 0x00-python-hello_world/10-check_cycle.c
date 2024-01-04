#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - a function that checks the cycle of a linked list
 * @list: list to be checkd
 * Return: New head
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *k, *l;

	if (!list || !list->next)
		return (0);
	k = list;
	l = list;
	while (k != NULL && l != NULL && k->next != NULL)
	{
		l = l->next;
		k = k->next->next;
		if (l == k)
		{
			return (1);
		}
	}
	return (0);
}
