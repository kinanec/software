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
