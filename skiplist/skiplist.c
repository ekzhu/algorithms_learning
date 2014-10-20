#include <stdlib.h>
#include <stdio.h>
#include <limits.h>
#include <string.h>

#include "skiplist.h"

int slist_height = 0;

/**
 * Allocate memory and initialize the given node
 */
void init_node(Node **node, int key_value) {
	*node = malloc(sizeof(Node));
	(*node)->next = NULL;
	(*node)->below = NULL;
	(*node)->key = key_value;
}

Node* make_skiplist() {
	Node *topleft, *topright;

	init_node(&topright, INT_MAX);
	init_node(&topleft, INT_MIN);

	topleft->next = topright;
	return topleft;
}

void free_skiplist(Node *slist) {
	Node *curr, *curr_first, *temp;

	curr_first = slist;
	while (curr_first) {
		curr = curr_first;
		curr_first = curr_first->below;
		while (curr) {
			temp = curr;
			curr = curr->next;
			free(temp);
		}
	}
}

Node* search(Node *slist, int key) {
	Node *curr;

	curr = slist;
	while (curr->below) {
		curr = curr->below;
		while (key >= curr->next->key) {
			curr = curr->next;
		}
	}
	return curr;
}

void insert(Node *slist, int key) {
	Node *prev, *next, *node, *above;
	int height = 0, i, height_diff, curr_height;

	// Find out what is the maximum height
	// for the inserted key
	do {
		height++;
	} while (rand() % 2);

	if ((height_diff = height - slist_height) >= 0) {
		// Update the skip list height by inserting new rows
		// under the top row.
		for (i = 0; i < height_diff + 1; i++) {
			// Create a new row
			init_node(&prev, INT_MIN);
			init_node(&next, INT_MAX);
			prev->next = next;

			// Insert this row under the top row
			prev->below = slist->below;
			next->below = slist->next->below;
			slist->below = prev;
			slist->next->below = next;
		}
		slist_height = height + 1;
	}

	// Insert the new node
	prev = slist;
	curr_height = slist_height;
	while (prev->below) {
		prev = prev->below;
		curr_height--;
		// Keep going until we reach the node's height
		if (curr_height > height) {
			continue;
		}
		while (key >= prev->next->key) {
			prev = prev->next;
		}
		// Insert node at this row
		init_node(&node, key);
		node->next = prev->next;
		prev->next = node;
		// Point the above row's node's next to this node
		if (curr_height < height) {
			above->below = node;
		}
		// Save the node at the current row
		above = node;
	}
}

void delete(Node *slist, int key) {
	Node *curr, *prev, *temp;

	curr = slist;
	// Find the first occurance of the key
	while (curr->below) {
		curr = curr->below;
		prev = curr;
		while (key >= curr->next->key) {
			prev = curr;
			curr = curr->next;
		}
		// If found at the current row
		if (curr->key == key) {
			// Delete all nodes below the curr
			while (curr && prev) {
				// Move prev to just one before curr
				while (prev->next != curr) {
					prev = prev->next;
				}
				// By-pass the curr node
				prev->next = curr->next;
				temp = curr;
				// Move down a level
				curr = curr->below;
				prev = prev->below;
				// Delete
				free(temp);
			}
			break;
		}
	}
}

void print_skiplist(Node *slist, int height) {
	Node *curr, *curr_first;

	curr_first = slist;
	while (curr_first) {
		curr = curr_first;
		// Print all node at this row
		printf("-nil->");
		curr = curr->next;
		while (curr->next) {
			printf("%d->", curr->key);
			curr = curr->next;
		}
		// Print the last one
		printf("nil\n");
		curr_first = curr_first->below;
	}
}

int main() {
	Node* slist = make_skiplist();
	int key;
	char operation[4];

	print_skiplist(slist, slist_height);
	while (1) {
		printf("Available operations: add [key], del [key], ext 0\n");
		scanf("%s %d", operation, &key);
		if (strcmp(operation, "ext") == 0) {
			printf("Bye\n");
			break;
		}
		if (strcmp(operation, "add") == 0) {
			insert(slist, key);
		}
		if (strcmp(operation, "del") == 0) {
			delete(slist, key);
		}
		print_skiplist(slist, slist_height);
	}
	free_skiplist(slist);
	return 0;
}
