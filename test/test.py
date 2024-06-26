from PPINA import graph_construction,protein_degree,CTGN
import matplotlib.pyplot as plt

# Building graph
G = graph_construction.G_build("G2-M_DNA_damage_checkpoint_ppi.txt")
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
