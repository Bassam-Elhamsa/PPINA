import networkx as nx
import numpy as np
def convert_uniprot_to_gene_name(uniprot_ids):
 uniprot_to_gene={
 'ID': 'Gene Name 1',
  'ID': 'Gene Name 2'
 }
 return {uniprot_id: uniprot_to_gene.get(uniprot_id) for uniprot_id in uniprot_ids}

def convert_to_unweighted_graph(G):
 unweighted_G = nx.Graph()