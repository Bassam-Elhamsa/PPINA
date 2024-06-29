import os
import networkx as nx
import matplotlib.pyplot as plt

# reading the file and make a list of tuples
file_path = "/home/work/PathLinker_2018_human-ppi-weighted-cap0_75.txt"

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
print(read_file(file_path)[0:10])      
        
#Making a directed graph
graph = nx.DiGraph()
graph.add_weighted_edges_from(read_file(file_path)[1000:1002], delimiter = "\t")
positions = nx.spring_layout(graph)
nx.draw_networkx_nodes(graph, positions, node_size=1500)
nx.draw_networkx_edges(graph, positions, edgelist=graph.edges, edge_color='k', width=1)
nx.draw_networkx_labels(graph, positions, font_size=10, font_family='sans-serif')
  
    #find the shortest path between two proteins
def shortest_path(file_path, source = "P29218", target = "Q13315"):
    graph = nx.DiGraph()
    graph.add_weighted_edges_from(read_file(file_path))
    try:
        path = nx.shortest_path(graph, source, target)
        return path
    except nx.NetworkXNoPath:
        return "No path found between the two proteins."
    except nx.NodeNotFound:
        return "One or both of the proteins are not in the graph."
    except Exception as e:
        return f"An error occurred: {e}"
print(f"The shortest path is: {shortest_path(file_path)}")

#find the total path score between the two proteins
def total_path_score(file_path, source = "P29218", target = "Q13315"):
    graph = nx.DiGraph()
    graph.add_weighted_edges_from(read_file(file_path))
    try:
        score = nx.shortest_path_length(graph, source, target)
        return score
    except nx.NetworkXNoPath:
        return "No path found between the two proteins."
    except nx.NodeNotFound:
        return "One or both of the proteins are not in the graph."
    except Exception as e:
        return f"An error occurred: {e}"
print(f"The total path score is: {total_path_score(file_path)}")

#find the weight of each interaction in the paths
def weight_of_each_interaction(file_path, source = "P29218", target = "Q13315"):
    graph = nx.DiGraph()
    graph.add_weighted_edges_from(read_file(file_path))
    try:
        path_weight = nx.path_weight(graph, path = nx.shortest_path(graph, source, target), weight = "weight" )
        return path_weight
    except nx.NetworkXNoPath:
        return "No path found between the two proteins."
    except nx.NodeNotFound:
        return "One or both of the proteins are not in the graph."
    except Exception as e:
        return f"An error occurred: {e}"
print(f"The weight is: {weight_of_each_interaction(file_path)}")
plt.show()
