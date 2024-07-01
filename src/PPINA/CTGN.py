import networkx as nx
import numpy as np
import requests



def convert_uniprotID_geneName(uniprot_ids=list):
    """
    Fetches Gene name for a given UniProt ID.

    :param uniprot_ids: The UniProt IDs to fetch gene name for.
    :return: list containing the converted gene names.
    """
    try:
        gene_names=[]
        for uniprot_id in uniprot_ids:
            url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}"
            params = {
                'format': 'json'
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            protein_info = response.json()
            gene_name = protein_info["genes"][0]["geneName"]["value"]
            gene_names.append(gene_name)
        return gene_names
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def convert_to_unweighted_graph(G):
    unweighted_G = nx.DiGraph()
    unweighted_G.add_edges_from(G.edges())
    return unweighted_G



def convert_to_adjacency_matrix(G):
 ad_matrix = nx.to_numpy_array(G)
 return ad_matrix


def save_adjacency_matrix(ad_matrix, filename):
 np.savetxt(filename, ad_matrix, delimiter=';', fmt='%d')








