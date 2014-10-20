#include <stdlib.h>
#include <stdio.h>
#include <limits.h>

#include "skiplist.h"

/**
 * Allocate memory and initialize the given node
 */
void init_node(Node **node, int key_value) {
	*node = malloc(sizeof(Node));
	(*node)->next = NULL;
	(*node)->down = NULL;
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
		curr_first = curr_first->down;
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
	while (curr->down) {
		curr = curr->down;
		while (key >= curr->key) {
			curr = curr->next;
		}
	}
	return curr;
}

void insert(Node *slist, int key) {
	Node *new_node;
}

int main() {
	Node* slist = make_skiplist();
	
	Node* found = search(slist, 10);
	printf("%d\n", found->key);

	free_skiplist(slist);
	return 0;
}
