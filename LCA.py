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
    trace = []
    pathsA = find_all_paths(G,root,a)
    pathsB = find_all_paths(G,root,b)
    tracer.append(pathsA)
    tracer.append(pathsB)
    i = 0
    while(i<len(pathsA)):
        pathsA[i].reverse()
        i+=1

    j=0
    while(j<len(pathsB)):
        pathsB[j].reverse()
        j+=1
    maxHeight = 0
    i=0
    for pathA in tracer[0]:
        for pathB in tracer[1]:
            i = 1
            while(i <= len(pathA) and i <= len(pathB)):
                if(pathB[-i]!=pathA[-i]):
                    break
                i = 1 + i
                if i>maxHeight:
                    maxHeight=i
                    print("New LCA " + str(pathA[-i+1]))
                    lc = pathA[-i+1]
                elif i==maxHeight and lc!=pathA[-i+1]:
                    temp = lc
                    lc = []
                    lc.append(temp)
                    lc.append(pathA[-i+1])
        return lc

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
