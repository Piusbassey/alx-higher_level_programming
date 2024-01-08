#include "lists.h"
/**
 * is_palindrome: Checks whether a list is a palindrome.
 * head: A double pointer to the head of list.
 *
 * Returns: 0 if not palindrome, 1 if it is.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev_slow = NULL, *second_half;

	while (fast != NULL && fast->next != NULL)
	{
		prev_slow = slow;
		slow = slow->next;
		fast = fast->next->next;
	}

	second_half = slow;
	prev_slow->next = NULL; 
	while (second_half != NULL)
	{
		listint_t *next = second_half->next;
		second_half->next = prev_slow;
		prev_slow = second_half;
		second_half = next;
	}

	while (prev_slow != NULL)
	{
		if (prev_slow->n != (*head)->n)
		{
			return (0);
		}
		prev_slow = prev_slow->next;
		*head = (*head)->next;
	}

	second_half = NULL;
	while (slow != NULL)
	{
		listint_t *next = slow->next;
		slow->next = second_half;
		second_half = slow;
		slow = next;
	}
	*head = second_half;

	return (1);
}
