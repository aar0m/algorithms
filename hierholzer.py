"""
///
///                 Ch.2 Graphs - Hierholzers Algorithm
///                 Personal Project By Aaron Ramos 2025
///
/// Implementation of Hierholzers Algorithm, which finds Eulerian circuits in directed graphs.
/// 
///
/// @hierholzer.py
/// @author Aaron Ramos (ramosaaron2@gmail.com)
///
"""

# Eulerian path exists if node has (outdegree) - (indegree) = 1 
# and another has (indegree) - (outdegree) = 1, while
# all other nodes have equal indegrees/outdegrees

# 1. Pick some starting node
# 2. Follow node until return to starting node
# 3. If there is vertex (node) that is in tour but has edge not in path, 
#    start another path from that vertex until we return to it
# 4. Repeat Step 3 until all possible nodes are visited, then splice into first path

class Node:
    def __init__(self, val):
        self.val = val
        self.indeg = []
        self.outdeg = []

class Graph:
    def __init__(self, root):
        self.root = root
        self.nodeList = [root]
        self.sol = []
        self.numEdges = 0
    
    def addNode(self, node):
        if node not in self.nodeList:
            self.nodeList.append(node)
        else:
            print(f"{node} is already in the graph")

    def addEdge(self, node1, node2): # Creates a directed edge between node1 and node2
        node1.outdeg.append(node2)
        node2.indeg.append(node1)
        self.numEdges += 1

    def dfs(self, startNode): # Depth-first search
        while len(startNode.outdeg) != 0:
            temp = startNode.outdeg[-1]
            startNode.outdeg.pop()
            self.dfs(temp)
        
        self.sol.append(startNode.val)

    def hiezholzer(self, startNode):
        self.dfs(startNode)

        if len(self.sol) != self.numEdges+1:
            print("Algorithm failed")
        else:
            for i in self.sol[::-1]:
                print(i, end=" ")

    def printNodes(self):
        valList = []
        for i in self.nodeList:
            valList.append(i.val)
        
        print(f"{valList}, {len(valList)} nodes in graph")
    
    def printGraph(self):
        print("Graph:", end="")
        for i in self.nodeList:
            print(f"\n{i.val} ->", end=" ")
            for j in i.outdeg:
                print(f"{j.val},", end="")
        print("\n")


def main():
    g = Graph(Node("AT"))
    g.addNode(Node("TG"))
    g.addNode(Node("GG"))
    g.addNode(Node("GC"))
    g.addNode(Node("CG"))
    g.addNode(Node("GT"))
    g.addNode(Node("CA"))
    g.addNode(Node("AA"))

    g.addEdge(g.nodeList[0], g.nodeList[1])
    g.addEdge(g.nodeList[1], g.nodeList[2])
    g.addEdge(g.nodeList[1], g.nodeList[3])
    g.addEdge(g.nodeList[2], g.nodeList[3])
    g.addEdge(g.nodeList[3], g.nodeList[4])
    g.addEdge(g.nodeList[3], g.nodeList[6])
    g.addEdge(g.nodeList[4], g.nodeList[5])
    g.addEdge(g.nodeList[5], g.nodeList[1])
    g.addEdge(g.nodeList[6], g.nodeList[7])
    g.addEdge(g.nodeList[7], g.nodeList[0])


    # g.printNodes() # Prints nodes in Graph
    g.printGraph()   # Prints graph
    
    print("Desired output using Hierholzerʻs Algorithm:")
    print("AT TG GC CG GT TG GG GC CA AA AT")

    print("\nOutput using Hierholzerʻs Function:")
    g.hiezholzer(g.nodeList[0])

if __name__ == "__main__":
    main()