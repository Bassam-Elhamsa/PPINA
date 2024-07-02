# PPINA
Protein Protein Interaction Network Analyzer

## Overview
**PPINA** is a Python package designed for analyzing protein-protein interactions (PPIs) within biological pathways. Utilizing NetworkX, it provides tools to retrieve, visualize, and analyze PPI data, helping researchers understand the connectivity and interaction patterns in their pathways of interest.

## Modules

### `graph_construction`

- **Description**: Builds a graph from a PPI TSV file. The TSV file must include at least the first three columns: tail node, head node, and interaction weight.
- **Features**:
  - Constructs a PPI network graph from input data.
  - Extracts all possible shortest paths between two proteins in the graph.
  - Returns the total path score and weight of each interaction within these pathways.
  - Visualizes the identified pathways.

### `protein_degree`

- **Description**: Extracts and visualizes the degrees of proteins within a constructed graph.
- **Features**:
  - Plots histograms representing the degree distribution of proteins.
  - Extracts the degree of each protein and saves this information in a TSV file.

### `CTGN` (Convert To Gene Name)

- **Description**: Facilitates the conversion of UniProt IDs to gene names and transforms the constructed graph into an adjacency matrix.
- **Features**:
  - Converts UniProt IDs to corresponding gene names.
  - Converts the PPI network graph into an adjacency matrix representation.
## Installation 
to install *PPINA*, you need to have Python 3.6 or later. You can install the package from PyPI:

```bash
pip install PPINA
```

Ensure you have the following dependencies:

```bash
pip install networkx matplotlib colorama requests
```

