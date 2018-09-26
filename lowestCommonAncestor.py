# A binary tree node
class Node:
    # Constructor to create a new binary node
    def __init__(self, key):
        self.key =  key
        self.left = None
        self.right = None

def isEmpty(root):
    #is empty = 0
    if root is None:
        return 0
    #is not empty = 1
    else:
        return 1


def findLCA(root, n1, n2):

    # Base Case
    if root is None:
        return None

    # If either n1 or n2 matches with root's key, report
    #  the presence by returning root (Note that if a key is
    #  ancestor of other, then the ancestor key becomes LCA
    if root.key == n1 or root.key == n2:
        return root

    # Look for keys in left and right subtrees
    left_lca = findLCA(root.left, n1, n2)
    right_lca = findLCA(root.right, n1, n2)

    # If both of the above calls return Non-NULL, then one key
    # is present in once subtree and other is present in other,
    # So this node is the LCA
    if left_lca and right_lca:
        return root

    # Otherwise check if left subtree or right subtree is LCA
    return left_lca if left_lca is not None else right_lca

#test if returns negative result when isEmpty() performed on a non empty tree:
def test_answer():
    root = Node(7)
    root.left = Node(3)
    root.right = Node(10)
    assert isEmpty(root) == 1

#test if isEmpty() returns positive result if tree is empty
def test_answer1():
    root = None
    assert isEmpty(root) == 0
