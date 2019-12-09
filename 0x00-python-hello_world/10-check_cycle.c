#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has a cycle in it
 * @list: singly linked list
 * Return: see below
 * 1. if there's no cycle, return 0
 * 2. if there's a cycle return 1
 */
int check_cycle(listint_t *list)
{
	/* declare variables to the head of linked list */
	listint_t *turtle = list;
	listint_t *rabbit = list;
	/**
	 * 1. if linked list is not  NULL
	 * 2. loop through the turtle linked list one by one
	 * 3. loop through the rabbit linked list ahead by one
	 * 4. when the two loops meets, return 1
	 * 5. if not, return 0
	 */
	while (turtle && rabbit && rabbit->next)
	{
		turtle = turtle->next;
		rabbit = rabbit->next->next;
		if (turtle == rabbit)
		{
			return (1);
		}
	}
	return (0);
}
