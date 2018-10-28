import networkx as nx
G = nx.DiGraph()

def findLCA(graph, root, a, b):

    if(root is None or a is None or b is None):
        return None
