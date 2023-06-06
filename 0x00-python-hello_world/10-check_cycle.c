#include "lists.h"
/**
 * check_cycle - checks if a singly inked list has a cycle
 * @list: pointer to the head of the list
 *
 * Return: 1 (if there is a cycle), 0 (otherwise)
*/
int check_cycle(listint_t *list)
{
	struct listint_s *snail;
	struct listint_s *hare;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	snail = list;
	hare = list->next;
	while (hare != NULL && hare->next != NULL)
	{
		if (snail == hare)
		{
			return (1);
		}

		snail = snail->next;
		hare = hare->next->next;
	}

	return (0);
}
