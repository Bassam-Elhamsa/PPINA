import networkx as nx
import numpy as np
from Bio import Swissprot
def getting_gene_name(Uniprot_ID):

def convert_to_unweighted_graph(G):
 unweighted_G = nx.DiGraph()
 for edge in G.edges():
  unweighted_G.add_edge(edge[0], edge[1])
  return unweighted_G

def convert_to_adjacency_matrix(G):
 ad_matrix = nx.to_numpy_array(G)
 return ad_matrix


def save_adjacency_matrix(ad_matrix, filename):
 np.savetxt(filename, ad_matrix, delimiter=';', fmt='%d')








