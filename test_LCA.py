import pytest
import LCA
import networkx as nx


#test result for no input
def test_answer1():
    assert LCA.findLCA(None, None, None, None) == None

#test when both nodes are the root node
def test_answer2():
    G = nx.DiGraph()
    G.add_node(1)
    assert LCA.findLCA(G,1,1,1) == 1

#test when value is not in the tree
def test_answer3():
    G = nx.DiGraph()
    G.add_nodes_from([1,3])
    assert LCA.findLCA(G, 1, 2,10) == None

#test for a root and two child nodes
def test_answer4():
    G = nx.DiGraph()
    G.add_nodes_from([1,3])
    G.add_edges_from([(1,2),(1,3)])
    assert LCA.findLCA(G, 1, 2,3) == 1

#test when a is not in the graph
def test_answer5():
    G = nx.DiGraph()
    G.add_nodes_from([1,3])
    assert LCA.findLCA(G, 1, 4,3) == None

#test when b is not in the graph
def test_answer6():
    G = nx.DiGraph()
    G.add_nodes_from([1,3])
    assert LCA.findLCA(G, 1, 3, 4) == None

#general testing of a big DAG
def test_answer7():
    G = nx.DiGraph()
    G.add_nodes_from([1, 10])
    G.add_edges_from([(1,2), (1,3), (1,5), (2,4), (2,5), (3,6), (3,7), (4,8), (5,8), (5,9), (5,10), (6,10)])
    assert LCA.findLCA(G, 1, 2, 7) == 1
    assert LCA.findLCA(G, 1, 7, 6) == 3
    assert LCA.findLCA(G, 1, 4, 7) == 1
    assert LCA.findLCA(G, 1, 4, 5) == 2
