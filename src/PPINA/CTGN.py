import networkx as nx
import numpy as np
from Bio import Entrez, SeqIO

Entrez.email = "maiteleb830@gmail.com"

def getting_gene_name(Uniprot_IDs):
    Gene_names = []
    for ID in Uniprot_IDs:
        Prot = Entrez.efetch(db="protein", id=ID, rettype="gb", retmode="text")
        result = SeqIO.read(Prot, "gb")
        Gene_names.append(result.description.split()[1])
    return gene_names

# testing function 1
Uniprot_IDs = ["Q8TBF4", "Q6I9Y2", "P51648","Q5MIZ7"]
print(getting_gene_name(Uniprot_IDs))


def convert_to_unweighted_graph(G):
    unweighted_G = nx.DiGraph()
    unweighted_G.add_edges_from(G.edges())
    return unweighted_G

#test function2
    G = nx.DiGraph()
    G.add_edge('A', 'B', weight=3.1)
    G.add_edge('B', 'C', weight=7.1)
    G.add_edge('C', 'A', weight=3.11)
    unweighted_G = convert_to_unweighted_graph(G)
    print(unweighted_G)

def convert_to_adjacency_matrix(G):
 ad_matrix = nx.to_numpy_array(G)
 return ad_matrix
#test function3
 ad_matrix = convert_to_adjacency_matrix(unweighted_G)

def save_adjacency_matrix(ad_matrix, filename):
 np.savetxt(filename, ad_matrix, delimiter=';', fmt='%d')

#test function4
save_adjacency_matrix(ad_matrix, 'ad45_matrixx.csv')

print(ad_matrix)







