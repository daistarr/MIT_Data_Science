from tree import Node  # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the tests named data_representation should pass.
tree_1 = Node(8, Node(2, Node(1), Node(6)), Node(10))  #Tree 1 test
tree_2 = Node(7, Node(2, Node(1), Node(5, Node(3), Node(6))), Node(9, Node(8), Node(10)))  #Tree 2 test
tree_3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26)))) #Tree 3 test

def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    
    #base case: if the tree = leaf, height = 0
    if tree.left is None and tree.right is None:
        return 0
    
    left_height = find_tree_height(tree.left) if tree.left is not None else -1 # recursive case: find the height of the left subtree and then, take the max height
    right_height = find_tree_height(tree.right) if tree.right is not None else -1 # recursive case: find the height of the right subtree and then, take the max height
    
    return max(left_height, right_height) + 1 # left/right max height, + 1 to account for the connection between the current node and the deeepest subtree


def is_heap(tree, compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. compare_func(child_value,parent_value) for a max heap would return False if child_value > parent_value and True otherwise
                 compare_func(child_value,parent_value) for a min meap would return False if child_value < parent_value and True otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    if tree is None: #class representing the root node of the tree
        return True
    left = tree.left
    right = tree.right
    if left is not None and not compare_func(left.value, tree.value): #left: compares a child node value to its parent node value
        return False
    if right is not None and not compare_func(right.value, tree.value): #right: compares a child node value to its parent node value
        return False
    return is_heap(left, compare_func) and is_heap(right, compare_func)

if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    pass
