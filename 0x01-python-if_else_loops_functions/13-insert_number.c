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
	/* declare variable for new node */
	listint_t *new;
	/* declare variable to hold head */
	listint_t *current = *head;
	/* allocate memory for new node but if it fails, return NULL */
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	/* create new node */
	new->n = number;
	new->next = NULL;
	/* if it's a empty list, then, set new node as head */
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	/* if element given is greater than head, then, make new node head */
	if ((*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	/**
	 * 1. iterate through list to NULL and
	 * 2. if element given is less than the node after it
	 * 3. then, point new node to the node after it
	 * 4. point the current node to the new node
	 */
	while ((current->next != NULL) && (current->next->n < number))
	{
		current = current->next;
	}
	new->next = current->next;
	current->next = new;
	return (new);
}
