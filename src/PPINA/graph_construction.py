import os
import networkx as nx
import matplotlib.pyplot as plt

# reading the file and make a list of tuples
file_path = "/home/work/PathLinker_2018_human-ppi-weighted-cap0_75.txt"
source="P29218"
target="Q13315"

if not os.path.isfile(file_path):
    raise FileNotFoundError("Please provide a valid input file path, or make sure the input file exists.")

def read_file(file_path):
    try:
        list_of_tuples = []
        with open(file_path, "r") as file:
            data = file.readlines()
            for line in data:
                if line[0] == '#':                    
                    continue
                line = line.split("\t")
                list_of_tuples.append((line[0], line[1], float(line[2])))
        return list_of_tuples
    except FileNotFoundError:
        print("Input file is missing.")
    return read_file
print(f"{read_file(file_path)[0:5]}\n")      
        
#Making a directed graph
graph = nx.DiGraph()
graph.add_weighted_edges_from(read_file(file_path))

# Find the shortest path between two proteins
paths = nx.all_shortest_paths(graph, source=source, target=target)
paths_list = list(paths)  # Convert to a list to reuse

print(f"The shortest path is: {paths_list}\n")

# Calcultae the weight of the shortest paths
def find_shortest_paths(graph, source, target):
    path_details = []
    paths = nx.all_shortest_paths(graph, source=source, target=target)
    for path in paths:
        path_score = 0
        edge_weights = []
        for i in range(len(path) - 1):
            weight = graph[path[i]][path[i + 1]]['weight']
            path_score += weight
            edge_weights.append(weight)
        path_details.append((path, path_score, edge_weights))
    return path_details

path_details = find_shortest_paths(graph, source, target)
print(f"the weight of each path is: {path_details}\n")

# Calculate the total path score for the shortest paths
total_path_score = sum([path_score for _, path_score, _ in path_details])
print(f"The total path score for the shortest paths is: {total_path_score}\n")

# draw the sub-network with the shortest path
shortest_path = paths_list[0]
shortest_path_graph = graph.subgraph(shortest_path)
position = nx.spring_layout(shortest_path_graph)
nx.draw(shortest_path_graph, position, with_labels=True, node_size=600, node_color='skyblue', edge_color='yellow')
labels = nx.get_edge_attributes(shortest_path_graph, 'weight')
nx.draw_networkx_edge_labels(shortest_path_graph, position, edge_labels=labels)
plt.show()
