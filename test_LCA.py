import pytest
import LCA

# class test_LCA(unittest.TestCase):

#test result for no input
def test_answer():
    assert LCA.findLCA(None, None, None) == None

#test when both nodes are the root node
def test_answer1():
    root = LCA.Node(1)
    assert LCA.findLCA(root,1,1) == 1

#test when value is not in the tree
def test_answer2():
    root = LCA.Node(6)
    root.left = LCA.Node(4)
    assert LCA.findLCA(root, 2,10) == -1

#test for n1 is root.left and root.right
    root.right = LCA.Node(10)
    assert LCA.findLCA(root, 4,10) == 6

#test to make recursion happen
    root.left.left = LCA.Node(2)
    root.left.right = LCA.Node(5)
    root.right.left = LCA.Node(7)
    root.right.right = LCA.Node(11)
    assert LCA.findLCA(root, 2,11) == 6
    assert LCA.findLCA(root, 7,11) == 10

# test where one n1 is root and n2 is another tree element
    assert LCA.findLCA(root, 6,10) == 6
