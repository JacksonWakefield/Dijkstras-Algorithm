try:
    import json
except:
    print("""In order to run this code, you require the following packages (make sure they are all installed!):
          json
          """)

#the purpose of this class is to create a full dijkstras graph with appropriate weights attached. 
#creating a new instance of dijkstras takes in width and height, and automatically runs the algorithm
#from __init__. To access the output of the algorithm you can call self.nodes, which returns a 
#2d array of the node class (the "node" class contains references to its
#position, weight, and its traceback node). Creating an instance of the class also 
#automatically outputs its data into a JSON file called
#data.txt
class dijkstra():
    
    #class for nodes
    class node():
        def __init__(self, weight, position):
            self.position = position
            self.weight = weight
            self.previous = None
    
    #initializes nodes and other values
    def __init__(self, width, height):
        #init width and height
        self.width = width
        self.height = height
        
        #init nodes 2d array
        self.nodes = [[self.node(100000, (i, j)) for i in range(self.width)] for j in range(self.height)]
        
        #run the official alg. output is stored back into self.nodes
        self.run(self.nodes, self.nodes[0][0])
        
        #package as json file
        with open('data.txt', 'w') as outfile:
            json.dump(self.package(self.nodes), outfile)

    #takes in Q and returns the smallest valued node
    def findSmallestNode(self, Graph):
        smallest = None
        smallest_index = 10000000
        for node in Graph:
            if node.weight <= smallest_index:
                smallest = node
                smallest_index = node.weight
        return smallest

    def getNeighbors(self, Graph, node, radius=1):
        neighbors = []
        neighbors_generic = [
            (0, -1),
            (1, 0),
            (-1, 0),
            (0, 1)
            ]
        for i in range(4):
            pos1 = node.position[0] + neighbors_generic[i][0]
            pos2 = node.position[1] + neighbors_generic[i][1]
            if(pos1 < 0 or pos1 >= len(Graph[0]) or pos2 < 0 or pos2 >= len(Graph)):
                continue
            else:
                neighbors.append(Graph[pos1][pos2])
            
        return neighbors

    def run(self, Graph, source):
        
        
        for row in Graph:
            for node in row:
                node.weight = 100000
                node.previous = None
        
        Graph[0][0].weight = 0
        #need this for json dump
        Graph[0][0].previous = Graph[0][0]
        
        Q = []
        for row in Graph:
            for node in row:
                Q.append(node)
        
        while len(Q) != 0:
            smallest_node = self.findSmallestNode(Q)
            #remove from Q
            Q.remove(smallest_node)
            
            neighbor_nodes = self.getNeighbors(Graph, smallest_node)
            
            for node in neighbor_nodes:
                
                tempdistance = smallest_node.weight + 1
                
                #if(smallest_node.weight == 0):
                    #print(node.weight)
                
                if tempdistance <= node.weight:
                    node.weight = tempdistance
                    node.previous = smallest_node
        return Graph
    
    #package up the json file for integration
    def package(self, finished_graph):
        i = 0
        json_total = {}
        for row in finished_graph:
            for node in row:
                
                json_total[i] = []
                
                json_total[i].append({
                        'positionX': node.position[0],
                        'positionY': node.position[1],
                        'weight': node.weight,
                        'previous': node.previous.position
                    })
                i += 1
        
        return json_total
dij = dijkstra(10, 10)