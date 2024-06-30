import networkx as nx
import matplotlib.pyplot as plt

def G_build(file_path):
    try:
        list_of_tuples = []
        with open(file_path, "r") as file:
            for line in file.readlines():
                if line[0] == '#':
                    continue
                line = line.split("\t")
                list_of_tuples.append((line[0], line[1], float(line[2])))
        G = nx.DiGraph()
        G.add_weighted_edges_from(list_of_tuples)
        return G
    except FileNotFoundError:
        print("Input file is missing.")




def all_shortest_paths(graph,source,target):
# Find the shortest path between two proteins
    paths = nx.all_shortest_paths(graph, source, target)
    paths_list = list(paths)  # Convert to a list to reuse
    return paths_list


# Calculate the weight of the shortest paths
def weight_of_each_path(graph, source, target,file_name="shortest_paths_with_weights"):
    path_details = []
    paths = all_shortest_paths(graph, source=source, target=target)
    for path in paths:
        path_score = 0
        edge_weights = []
        for i in range(len(path) - 1):
            weight = graph[path[i]][path[i + 1]]['weight']
            path_score += weight
            edge_weights.append(weight)
        path_details.append((path, path_score, edge_weights))
    with open(file_name,'w') as out:
        out.write("#Path\tPath_Score\tInteraction_Weights\n")
        for path in path_details:
            Path = "--".join(path[0])
            Path_score = float(path[1])
            Interaction_weights = str(path[2])
            out.write("%s\t%f\t%s\n" %(Path,Path_score,Interaction_weights))
    return path_details



# Extract the edges and nodes for the subgraph
def subgraph_plot(G,path):
    edges = []
    for i in range(len(path)-1):
        edges.append((path[i],path[i+1]))
    subgraph = G.edge_subgraph(edges)
    # Draw the subgraph
    position = nx.spring_layout(subgraph)  # Layout for better visualization
    nx.draw(subgraph, position, with_labels=True, node_size=1500, node_color="skyblue",
            font_size=12, font_weight="bold", edge_color="cyan", width=2.0)
    labels = nx.get_edge_attributes(subgraph, 'weight')
    nx.draw_networkx_edge_labels(subgraph, position, edge_labels=labels)
    plt.show()


