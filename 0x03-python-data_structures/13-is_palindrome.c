#include "lists.h"
#include <stdio.h>
#include <stddef.h>

void rev(listint_t **head);
int comp_lists(listint_t *head, listint_t *mid, int len);
/**
 * is_palindrome - to check if a list is palindrome
 * @head: point to the pointer of the 1st node
 * Return: 0 if there is no palindrome 1 if it exists
 */

int is_palindrome(listint_t **head)
{
	int len, k;
	listint_t *temp;
	listint_t *mid;

	if (head == NULL || *head == NULL)
		return (1);
	temp = *head;
	mid = *head;
	for (len = 0; temp != NULL; len++)
		temp = temp->next;
	len = len / 2;
	for (k = 1; k < len; k++)
		mid = mid->next;
	if (len % 2 != 0 && len != 1)
	{
		mid = mid->next;
		len = len - 1;
	}
	rev(&mid);
	k = comp_lists(*head, mid, len);
	return (k);
}
/**
 * comp_lists - to compare to lists
 * @head: pointer to the head node
 * @mid: poiter to the mid node
 * @len: length of the lift
 * Return: 0 or 1
 */
int comp_lists(listint_t *head, listint_t *mid, int len)
{
	int k;

	if (head == NULL || mid == NULL)
		return (1);
	for (k = 0; k < len; k++)
	{
		if (head->n != mid->n)
			return (0);
		head = head->next;
		mid = mid->next;
	}
	return (1);
}
/**
 * rev - reverse a list
 * @head: pointer to the head to reverse
 */
void rev(listint_t **head)
{
	listint_t *current;
	listint_t *nxt;
	listint_t *prev;

	if (head == NULL || *head == NULL)
		return;
	prev = NULL;
	current = *head;
	while (current != NULL)
	{
		nxt = current->next;
		current->next = prev;
		prev = current;
		current = nxt;
	}
	*head = prev;
}
