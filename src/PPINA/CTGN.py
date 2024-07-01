import networkx as nx
import numpy as np
from Bio import Entrez, SeqIO



def getting_gene_name(Uniprot_IDs,Entrez_email):
    Entrez.email = Entrez_email
    Gene_names = []
    for ID in Uniprot_IDs:
        Prot = Entrez.efetch(db="protein", id=ID, rettype="gb", retmode="text")
        result = SeqIO.read(Prot, "gb")
        Gene_names.append(result.description.split()[1])
    return Gene_names



def convert_to_unweighted_graph(G):
    unweighted_G = nx.DiGraph()
    unweighted_G.add_edges_from(G.edges())
    return unweighted_G



def convert_to_adjacency_matrix(G):
 ad_matrix = nx.to_numpy_array(G)
 return ad_matrix


def save_adjacency_matrix(ad_matrix, filename):
 np.savetxt(filename, ad_matrix, delimiter=';', fmt='%d')








