import networkx as nx
import numpy as np
from Bio import Swissprot
def convert_uniprot_to_gene_name(uniprot_ids):
 uniprot_to_gene={
 'ID': 'Gene Name 1',
  'ID': 'Gene Name 2'
 }
 return {uniprot_id: uniprot_to_gene.get(uniprot_id) for uniprot_id in uniprot_ids}

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








