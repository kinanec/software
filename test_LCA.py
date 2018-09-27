import pytest
import LCA

# class test_LCA(unittest.TestCase):

#test result for no input
def test_answer():
    assert LCA.findLCA(None, None, None) == None

def test_answer1():
    root = LCA.Node(1)
    assert LCA.findLCA(root,1,1) == 1
