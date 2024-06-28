import networkx as nx
import numpy as np
from Bio import Entrez, SeqIO

Entrez.email = "maiteleb830@gmail.com"

def getting_gene_name(Uniprot_ID):

    Prot = Entrez.efetch(db="protein", id=Uniprot_ID, rettype="gb", retmode="text")
    result = SeqIO.read(Prot, "gb")
    return result.description.split()[1]

# testing function 1
Uniprot_IDs=['Q8TBF4','Q15717','Q5MIZ7','Q8N490']
for Uniprot_ID in Uniprot_IDs:
    Gene_Name = getting_gene_name(Uniprot_ID)
    if Gene_Name is not None:
        print(f"UniProt ID: {Uniprot_ID}, Gene Name: {Gene_Name}")
    else:
        print(f"Error: Invalid UniProt ID: {Uniprot_ID}")



def convert_to_unweighted_graph(G):
    unweighted_G = nx.DiGraph()
    unweighted_G.add_edges_from(G.edges())
    return unweighted_G

#test function
    G = nx.DiGraph()
    G.add_edge('A', 'B', weight=3.1)
    G.add_edge('B', 'C', weight=7.1)
    G.add_edge('C', 'A', weight=3.11)
    unweighted_G = convert_to_unweighted_graph(G)
    print(unweighted_G)

def convert_to_adjacency_matrix(G):
 ad_matrix = nx.to_numpy_array(G)
 return ad_matrix
#test function
 ad_matrix = convert_to_adjacency_matrix(unweighted_G)

def save_adjacency_matrix(ad_matrix, filename):
 np.savetxt(filename, ad_matrix, delimiter=';', fmt='%d')

#test function
save_adjacency_matrix(ad_matrix, 'ad45_matrixx.csv')

print(ad_matrix)







