#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a new node into a sorted singly linked list
 * @head: pointer to the pointer of the first node of the list
 * @number: integer value to store in the new node
 *
 * Return: pointer to the new node or NULL (failure)
*/
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_nd = NULL;
    listint_t *cnt = *head;
    listint_t *prv = NULL;

    new_nd = malloc(sizeof(listint_t));
    if (new_nd == NULL)
        return NULL;
    new_nd->n = number;
    new_nd->next = NULL;

    if (*head == NULL || number < cnt->n)
    {
        new_nd->next = *head;
        *head = new_nd;
        return new_nd;
    }

    while (cnt != NULL && number > cnt->n)
    {
        prv = cnt;
        cnt = cnt->next;
    }

    new_nd->next = cnt;
    prv->next = new_nd;

    return new_nd;
}
