import pytest
import LCA

# class test_LCA(unittest.TestCase):

#test result for no input
def test_answer():
    assert LCA.findLCA(None, None, None) == None
