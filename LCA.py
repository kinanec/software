import networkx as nx
G = nx.DiGraph()
G.add_nodes_from([1, 10])
G.add_edges_from([(1,2), (1,3), (1,5), (2,4), (2,5), (3,6), (3,7), (4,8), (5,9), (6,10)])

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
    trace = []
    pathsA = find_all_paths(G,root,a)
    pathsB = find_all_paths(G,root,b)
    tracer.append(pathsA)
    tracer.append(pathsB)
    

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
