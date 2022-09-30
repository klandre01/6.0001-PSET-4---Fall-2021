# Problem Set 4a
# Name: Karen Andre
# Collaborators: None
# Time spent: 1:00

from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the tests named data_representation should pass.
tree1 = Node(8, Node(2, Node(1), Node(5)), Node(10)) #TODO
tree2 = Node(7, Node(2, Node(1), Node(5, Node(4), Node(6))), Node(9, Node(8), Node(10))) #TODO
tree3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(19), Node(26)))) #TODO

def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    # TODO: Remove pass and write your code here
    left_height = 0
    right_height = 0
    if (tree.get_left_child() == None and tree.get_right_child() == None):
        return 0
    else:
        if (tree.get_left_child() == None):
            left_height += 0
        else:
            left_height = 1 + find_tree_height(tree.get_left_child())
        if (tree.get_right_child() == None):
            right_height += 0
        else:
            right_height = 1 + find_tree_height(tree.get_right_child())
    return max(right_height, left_height)



def is_heap(tree,compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    # TODO: Remove pass and write your code here
    if (tree.get_left_child() == None and tree.get_right_child() == None):
        return True
    else:
        if (tree.get_left_child() == None):
            left_is_heap = True
        elif (not compare_func(tree.get_left_child().get_value(), tree.get_value())):
            left_is_heap = False
        else:
            left_is_heap = is_heap(tree.get_left_child(), compare_func)
        if (tree.get_right_child() == None):
            right_is_heap = True
        elif (not compare_func(tree.get_right_child().get_value(), tree.get_value())):
            right_is_heap = False
        else:
            right_is_heap = is_heap(tree.get_right_child(), compare_func)
    return (left_is_heap and right_is_heap)



if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    pass
