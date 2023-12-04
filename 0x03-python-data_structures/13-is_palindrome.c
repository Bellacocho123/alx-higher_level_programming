#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 1 if palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int i = 0, j = 0, k = 0, l = 0;
	int arr[10000];

	if (!head || !(*head))
		return (1);
	while (temp)
	{
		arr[i] = temp->n;
		temp = temp->next;
		i++;
	}
	j = i - 1;
	while (k < j)
	{
		if (arr[k] != arr[j])
			l = 1;
		k++;
		j--;
	}
	if (l == 1)
		return (0);
	return (1);
}
