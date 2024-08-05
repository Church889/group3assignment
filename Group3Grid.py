
#Sam Sameeha Azfer
# 07/04/2024
#Group3

#IMPORTS

import heapq
import csv


#Class for graph
class Graph:
    def __init__(self):
        self.nodes=set()
        self.edges={}
    
    #ADD NODES
    def addNode(self, value):
        self.nodes.add(value)
        if value not in self.edges:
            self.edges[value]={}
    #ADD EDGES
    def addEdge(self, fromNode, toNode, distance):
        self.addNode(fromNode)
        self.addNode(toNode)
        self.edges[fromNode][toNode]=distance
        self.edges[toNode][fromNode]=distance  
    
    #ALROGITHM FOR DIJINKA
    def dijAlgo(self,start):
        distances = {node: float('inf') for node in self.nodes}
        distances[start]=0
        visited = set()
        queue = [(0,start)]
        
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            if current_node in visited:
                continue
            visited.add(current_node)
            
            for neighbour, weight in self.edges[current_node].items():
                distance = current_distance + int(weight)
                if distance<distances[neighbour]:
                    distances[neighbour] = distance
                    heapq.heappush(queue, (distance, neighbour))
        
        return distances

#LOAD DATA FROM GIVEN CSV FILE
def loadnetCSV(filePath):
    graph = Graph()
    with open(filePath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            (fromNode, toNode, distance) = row
            graph.addEdge(fromNode, toNode, distance)
    return graph

def routeRecommendation(graph, startNode, chargingStations):
    shortestPath = {}
    for station in chargingStations:
        shortestPath[station] = graph.dijAlgo(startNode)[station]
    recommendedStation = min(shortestPath, key=shortestPath.get)
    return recommendedStation, shortestPath[recommendedStation]

#OUTPUT
def main():
    filePath = 'blank.csv'
    graph = loadnetCSV(filePath)

    #ENTRY FOR START NODE
    ui=False

    #AUTH VALIDATION
    #positions you can use
    usablePos=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W']
    
    #USER AUTH and what not
    while not ui:
        startNode = input("ENTER START POSITION: 'A'  ---> 'W' --caps only-- : ")
        if startNode in usablePos:
            ui = True
        else:
            print("Please enter a capital letter from A-W")

    #CHARGING STATIONS
    chargingStations=['H','K','Q','T']
    
    #ASSIGN SHORTEST PATHS
    shortestPath = {}

    for station in chargingStations:
        shortestPath[station] = graph.dijAlgo(startNode)[station]
    
    #PRINT OUT SHORTEST PATHS
    print("SHORTEST PATH FROM NODE {} TO CHARGE STATIONS:".format(startNode))
    for station, distance in shortestPath.items():
        print("To {}: {}".format(station, distance))

    #FIND RECOMMENDED ROUTE
    recommendedStation, shortestDistance = routeRecommendation(graph,startNode,chargingStations)

    #PRINT RECOMMENDED ROUTE
    print("Recommended charge station FROM node" + (startNode), "would be! -->", (recommendedStation) +
          "W/ SHORTEST DISTANCE of" + str(shortestDistance) + "UNITS")

if __name__ == "__main__":
    main()
