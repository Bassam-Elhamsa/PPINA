# PPINA
Protein Protein Interaction Network Analyzer

## Overview
*PPINA* is a Python package designed for analyzing protein-protein interactions (PPIs) within biological pathways. Utilizing NetworkX, it provides tools to retrieve, visualize, and analyze PPI data, helping researchers understand the connectivity and interaction patterns in their pathways of interest.

## Modules
- *graph_construction*: This module is for building a graph from *PPI* tsv file that has at least the first three columns that are tail node, head node and weight of the interaction , also *graph_construction* can be used to extract all possible shortest pathes between two proteins from a graph and returning the total path score and weight of each interaction of the pathway and vizualizng the path
- *protein_degree*: This module is for extracting and vizualizng proteins degrees of set of proteins in a constructed graph
- *CTGN*: This module is for converting *UniprotID* to gene name and to convert the constructed graph to adjacency matrix

## Installation 
to install *PPINA*, you need to have Python 3.6 or later. You can install the package from PyPI:

\```Bash
pip install PPINA
\```

Ensure you have the following dependencies:

\```Bash
pip install networkx matplotlib colorama requests
\```

