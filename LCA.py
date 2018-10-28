import networkx as nx
G = nx.DiGraph()

def findLCA(graph, root, a, b):

    if(root is None or a is None or b is None):
        return None
    if (a == root or b == root):
        return root
    if(not graph.has_node(a)):
        print(str(a) + " does not exist in the graph.")
        return None
    
