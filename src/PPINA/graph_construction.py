import os
import networkx as nx
import matplotlib.pyplot as plt

# reading the file and make a list of tuples
file_path = "/home/work/PathLinker_2018_human-ppi-weighted-cap0_75.txt"

if not os.path.isfile(file_path):
    raise FileNotFoundError("Please provide a valid input file path, or make sure the file exists.")

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
print(read_file(file_path)[0:20])      
        
#Draw a constructed graph
def draw_graph(file_path, delimiter="\t"):
    G = nx.DiGraph()
    G.add_weighted_edges_from(read_file(file_path)[0:20], delimiter = delimiter)
    positions = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, positions, node_size=1500)
    nx.draw_networkx_edges(G, positions, edgelist=G.edges, edge_color='k', width=1)
    nx.draw_networkx_labels(G, positions, font_size=10, font_family='sans-serif')
    plt.show()
    return draw_graph


try:
    draw_graph(file_path)
except Exception as e:
    print(f"An error occurred: {e}")
    