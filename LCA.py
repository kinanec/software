# A binary tree node
class Node:
    # Constructor to create a new binary node
    def __init__(self, key):
        self.key =  key
        self.left = None
        self.right = None

# Finds the path from root node to given root of the tree.
# Stores the path in a list path[], returns true if path
# exists otherwise false
def findPath( root, p, x):

    # Baes Case
    if root is None:
        return False

    # Store this node is path vector. The node will be
    # removed if not in path from root to x
    p.append(root.key)

    # See if the x is same as root's key
    if root.key == x :
        return True

    # Check if x is found in left or right sub-tree
    if ((root.left != None and findPath(root.left, p, x)) or
            (root.right!= None and findPath(root.right, p, x))):
        return True

    # If not present in subtree rooted with root, remove
    # root from path and return False

    p.pop()
    return False

# Returns LCA if node n1 , n2 are present in the given
# binary tre otherwise return -1
def findLCA(root, n1, n2):

    if(root is None or n1 is None or n2 is None):
        return None

    # To store paths to n1 and n2 fromthe root
    p1 = []
    p2 = []
    # Find paths from root to n1 and root to n2.
    # If either n1 or n2 is not present , return -1
    if (not findPath(root, p1, n1) or not findPath(root, p2, n2)):
        return -1

    # Compare the paths to get the first different value
    i = 0
    while(i < len(p1) and i < len(p2)):
        if p1[i] != p2[i]:
            break
        i += 1
    return p1[i-1]

# #test if returns negative result when isEmpty() performed on a non empty tree:
# def test_answer():
#     root = Node(7)
#     root.left = Node(3)
#     root.right = Node(10)
#     assert isEmpty(root) == 1
#
# #test if isEmpty() returns positive result if tree is empty
# def test_answer1():
#     root = None
#     assert isEmpty(root) == 0
#
# #basic example to test LCA for a binary tree of height one
# def test_answer2():
#     root = Node(7)
#     root.left = Node(3)
#     root.right = Node(10)
#     assert findLCA(root, 3, 10).key == 7
#
# #test to see how program handles a node that isnt in the tree
# def test_answer3():
#     root = Node(7)
#     root.left = Node(3)
#     root.right = Node(10)
#     root.left.left = Node(2)
#     root.left.left.right = Node(4)
#     assert findLCA(root, 2, 5).key ==



    # root = Node(7)
    # root.left = Node(3)
    # root.right = Node(10)
    # root.left.left = Node(2)
    # root.left.left.right = Node(4)
    # root.left.right = Node(5)
    # root.left.right.right = Node(6)
    # root.right.left = Node(8)
    # root.right.right = Node(14)
    # print ("LCA(4,5) = ", findLCA(root, 4, 5).key)
    # print ("LCA(4,6) = ", findLCA(root, 4, 6).key)
    # print ("LCA(3,4) = ", findLCA(root, 3, 4).key)
    # print ("LCA(2,4) = ", findLCA(root, 2, 4).key)
