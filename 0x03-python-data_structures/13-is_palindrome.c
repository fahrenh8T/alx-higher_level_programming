#include "lists.h"
#include <stddef.h>
/**
 * reverse_listint - reverses a linked list of integers
 * @head: pointer to the first node of the list
 *
 * Return: pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *crrnt = *head;
	listint_t *nxt;
	listint_t *prv = 0;

	while (crrnt)
	{
		nxt = crrnt->next;
		crrnt->next = prv;
		prv = crrnt;
		crrnt = nxt;
	}
	*head = prv;

	return (*head);
}

/**
 * is_palindrome - checks if a linked list of integers is a palindrome
 * @head: pointer to a pointer to the first node of the list
 *
 * Return: 1 (if palindrome), 0 (otherwise)
 */
int is_palindrome(listint_t **head)
{
	listint_t *tempo, *rvs, *midp;
	size_t size = 0, index;

	if (*head == 0 || (*head)->next == 0)
		return (1);

	tempo = *head;
	while (tempo)
	{
		size++;
		tempo = tempo->next;
	}

	tempo = *head;
	for (index = 0; index < (size / 2) - 1; index++)
		tempo = tempo->next;

	if ((size % 2) == 0 && tempo->n != tempo->next->n)
		return (0);

	tempo = tempo->next->next;
	rvs = reverse_listint(&tempo);
	midp = rvs;

	tempo = *head;
	while (rvs)
	{
		if (tempo->n != rvs->n)
			return (0);
		tempo = tempo->next;
		rvs = rvs->next;
	}

	reverse_listint(&midp);

	return (1);
}
