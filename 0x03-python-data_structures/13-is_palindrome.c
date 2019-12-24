#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_helper - function that returns a truth value
 * @head: head of singly linked list
 * @node: node that includes the palindrome to check for
 * Description: 13. Linked list palindrome
 * Return: see below
 * 1. upon success, 1 if it's a palindrome or empty list
 * 2. upon fail, 0 if it isn't a palindrome
 */
int is_helper(listint_t **head, listint_t *node)
{
	int check1 = 0, check2 = 0;
	listint_t *current = node;

	if (head == NULL)
		return (0);
	if (current == NULL)
		return (1);
	check1 = is_helper(head, current->next);
	if (check1 == 0)
		return (0);
	check2 = (current->n == (*head)->n);
	*head = (*head)->next;
	return (check2);
}

/**
 * is_palindrome - function that checks if singly linked list is a palindrome
 * @head: head of singly linked list
 * Description: 13. Linked list palindrome
 * Return: see below
 * 1. upon success, 1 if it's palindrome or empty list
 * 2. upon fail, 0 if it isn't a palindrome
 */
int is_palindrome(listint_t **head)
{
	int check = 0;
		check = is_helper(head, *head);
	return (check);
}
