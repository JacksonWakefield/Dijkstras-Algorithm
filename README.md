# Dijsktras-Algorithm
This is Dijkstra's Pathfinding Algorithm based on a 2 dimensional grid (with all weights as 1) written in Python. Running the executable will give you a json dump of all the information about each node in the grid.


# Description (also at the top of the python file)
the purpose of this class is to create a full dijkstras graph with appropriate weights attached. 
creating a new instance of dijkstras takes in width and height, and automatically runs the algorithm
from __init__. To access the output of the algorithm you can call self.nodes, which returns a 
2d array of the node class (the "node" class contains references to its
position, weight, and its traceback node). Creating an instance of the class also 
automatically outputs its data into a JSON file called
data.txt
