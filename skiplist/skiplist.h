
typedef struct Node {
	int key;
	struct Node *below;
	struct Node *next;
} Node;

/**
 * Maximum height 
 */

/**
 * Create a skip list, return the top-left
 * node.
 */
Node* make_skiplist();

/**
 * Free all memory allocated by
 * the given skiplist.
 * Given the top-left node.
 */
void free_skiplist(Node *slist);

/**
 * Search for the key, return 
 * the node with largest key value
 * that is less or equal to the given
 * key.
 * The returned node is in the
 * bottom list.
 */
Node* search(Node *slist, int key);

/**
 * Insert a key to the skiplist.
 */
void insert(Node *slist, int key);

/**
 * Delete a key from the skiplist
 */
void delete(Node *slist, int key);
