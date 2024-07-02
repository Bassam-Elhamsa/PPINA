from PPINA import graph_construction,protein_degree,CTGN
import matplotlib.pyplot as plt

# Building graph
G = graph_construction.G_build("G2-M_DNA_damage_checkpoint_ppi.txt")
#Find the shortest path between two proteins
paths = gc.all_shortest_paths(draw_graph,"P62807" ,"Q12888")

#Caclculate the weight and the total path score for the shortest paths
weight = gc.weight_of_each_path(draw_graph,"P62807" ,"Q12888")

#Draw the subgraph
sub_graph = gc.subgraph_plot(draw_graph, path = paths[0]0
# Extract all proteins in the graph
all_proteins = list(G.nodes())
# plot histogram pathway's protein degrees and save it as png
protein_degree.proteins_degrees_hist(DiGraph=G,proteins=all_proteins,bin_width=10,save_file=[True,"Histogram of proteins degree.png"])

# Get sorted list pf proteins and its corresponding degrees and save it
deg=protein_degree.sort_proteins_degrees(DiGraph=G,proteins=all_proteins,save_file=[True,"M2-G protein degrees.txt"])

# plot bar plot of the highest 5 proteins degrees
max_5 = deg[0:5]  # Extract first 5 proteins
max_5_degrees = []
max_5_id = []
for d in max_5:
    Id=list(d.keys())[0]  # Getting protein uniprot ID
    degree = list(d.values())[0][0]  #Getting protein degree value
    max_5_id.append(Id)
    max_5_degrees.append(degree)
    



# Getting gene name of the protein
max_5_name = CTGN.convert_uniprotID_geneName(max_5_id)
# plotting the bar plot
plt.bar(max_5_name,max_5_degrees)
plt.xlabel("Gene Name")
plt.ylabel("Connection Degree")
plt.title("Bar_plot of the most 5 highest connection degrees")
plt.savefig("Bar_plot of the most 5 highest connection degrees.png",dpi=300)
plt.show()


# proteins connected (neigbors) to specific protein
protein_id = 'P35250'  # Replace with actual UniProt ID
degree, connections = list_direct_connections(G, protein_id)
from PPINA import CTGN as ct

import requests
uniprot_ids =['P62807', 'P31946', 'Q96RL1', 'Q9NXR7', 'P62807', 'P16104']

gene_names=ct.convert_uniprotID_geneName(uniprot_ids)

print(gene_names)

G= nx.DiGraph()
G.add_edge('A','B',weight=0.058035)
G.add_edge('B','C',weight=0.750000)
G.add_edge('C','A',weight=0.710749)
G.add_edge('D','F',weight=0.536469)
unweighted_G=ct.convert_to_unweighted_graph(G)
print(unweighted_G)

ad_matrix=ct.convert_to_adjacency_matrix(G)
ct.save_adjacency_matrix(ad_matrix,'ad9_matrix.csv')
print(ad_matrix)

