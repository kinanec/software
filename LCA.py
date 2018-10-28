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
    if(not graph.has_node(b)):
        print(str(b) + " does not exist in the graph.")
        return None
    
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_node(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
