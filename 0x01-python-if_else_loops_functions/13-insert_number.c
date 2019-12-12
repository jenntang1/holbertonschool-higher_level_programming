#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - function that inserts a number into a list
 * @head: pointer to head
 * @number: integer element to insert into new node
 * Description: 13. Insert in sorted linked list
 * Return: see below
 * 1. upon success, return address of new node
 * 2. upon failure, return NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	current = *head;

	if (head == NULL)
		return (NULL);

	if (*head == NULL)
		new->next = NULL;
		*head = new;
		return (*head);

	if (current->n > number)
		new->next = current;
		*head = new;
		return (new);

	while (current)
		if (current->next)
			if (current->next->n > number)
				new->next = current->next;
				current->next = new;
				return (new);
}
