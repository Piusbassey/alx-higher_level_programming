#include "lists.h"
/**
 * print_listint - Prints all elements of a listint_t list.
 * @h: Pointer to head of list.
 * Return: Number of nodes.
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n;

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf("%i\n", current->n);
        current = current->next;
        n++;
    }
    return (n);
}

/**
 * add_nodeint - Adds a new node at the beginning of a listint_t list.
 * @head: Pointer to a pointer of the start of the list.
 * @n: Integer to be included in node.
 * Return: Address of the new element or NULL if it fails.
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
    listint_t *new;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = *head;
    *head = new;

    return (new);
}

/**
 * free_listint - Frees a listint_t list.
 * @head: Pointer to list to be freed.
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}

/**
 * check_cycle - Checks if a singly linked list has a cycle.
 * @h: Pointer to the head of the list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *h)
{
    listint_t *slow, *fast;

    if (h == NULL)
        return 0;

    slow = fast = h;

    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast)
            return (1);
    }
    return (0);
}
