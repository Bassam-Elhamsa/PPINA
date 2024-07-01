import networkx as nx
import matplotlib.pyplot as plt
from colorama import Fore


def proteins_degrees_hist(DiGraph, proteins, bin_width=10, log=False, show=True,
                          save_file=[False, "Histogram of proteins degree"]):
    """
       proteins_degrees_hist is a function that draw a histogram for a set of proteins connection degree
       that is extracted from PPI network graph\n\n
       :param DiGraph : non-empty networkx.DiGraph class of PPI network
       :param proteins : non-empty list of non-empty string elements of proteins names
       :param bin_width : default 500 : integer that decide width of bins of the histogram (optional)
       :param log : default False : bool that decide whether to use log transformation to better visualize condensed data (optional)
       :param save_file : default [False, "Histogram of proteins degree.png"] : non-empty list of 2 elements first of which is
       bool and second is non-empty string of the saved file name this parameter decide if the histogram will be saved
       or not and specify the saved file name (if the file name not specified default name will be given 'Histogram of proteins degree') (optional)
       :param show : default True : bool that decide whether histogram will be shown or not (optional)
       :return: proteins_degrees_hist returns figure of histogram for set of proteins connection degrees
    """

    # Testing the parameters that user define

    ## testing if the DiGraph is non-empty networkx.DiGraph class and raise TypeError if not
    if not isinstance(DiGraph, nx.DiGraph) or len(DiGraph) == 0:
        raise TypeError("DiGraph should be non empty networkx.DiGraph class")

    ## testing if the proteins is non-empty list of strings elements and raise TypeError if not
    if not isinstance(proteins, list) or len(proteins) == 0 or any(not isinstance(protein, str) for protein in proteins) \
            or any(len(protein) == 0 for protein in proteins):
        raise TypeError("proteins should be non empty list of non-empty strings elements of proteins names")

    ## testing if the log is of type bool and use the default value (False) with a warning massage if not
    if not isinstance(log, bool):
        log = False
        print(Fore.RED + "Warning:log should be either True or False\nlog now is at default value: False")

    ## testing if the bin_width is of type int and use the default value (500) with a warning massage if not
    if not isinstance(bin_width, int):
        bin_width = 500
        print(Fore.RED + "Warning:bin_width should be integer\nbin_width now is at default value: 500")

    ## testing if save_file is of type list and its first element of type bool and use the default value (False, "Histogram of proteins degree") with a warning massage if not
    if not isinstance(save_file, list) or len(save_file) == 0 or not isinstance(save_file[0], bool):
        save_file = (False, "Histogram of proteins degree.png")
        print(
            Fore.RED + "Warning:save_file should be a list of 2 elements bool and non-empty str respectively\nThe figure will not be saved")

    ## testing if the show is of type bool and use the default value (True) with a warning massage if not
    if not isinstance(show, bool):
        show = True
        print(Fore.RED + "Warning:show should be bool\nshow now is at default value: True")

    ## Extracting proteins degrees of the DiGraph through a for loop and append it to a list
    dist = []
    for protein in proteins:
        dist.append(DiGraph.degree[protein])

    ## Plotting proteins degrees histogram

    # plot the histogram
    plt.hist(dist, log=log, bins=range(0, max(dist) + bin_width, bin_width), edgecolor='b')
    # Giving title for the histogram
    plt.title("Histogram of proteins degree", size=20)
    # Giving title for x-axis the histogram
    plt.xlabel("Proteins connection degree", size=12)
    # test if the log parameter is True or False to title the y-axis
    # if True y-axis title will be "Log Frequency"
    # if False y-axis title will be "Frequency"
    if log:
        plt.ylabel("Log Frequency", size=12)
    else:
        plt.ylabel("Frequency", size=12)

    # test if the save_file parameter is True or False to save the histogram with the user defined name
    if save_file[0]:
        # test if the user mis-define saved file name and to save the histogram with default name and printing warning massage of doing so
        if len(save_file) < 2 or len(save_file[1]) == 0 or not isinstance(save_file[1], str):
            plt.savefig("Histogram of proteins degree.png", dpi=300)
            print(
                Fore.RED + "Warning:File name not specified\nDefault name will be used:'Histogram of proteins degree'")
        else:
            plt.savefig(save_file[1], dpi=300)

    # test if the show parameter is True or False to show the histogram
    if show:
        plt.show()


def sort_proteins_degrees(DiGraph, proteins, order="descending",
                          save_file=[False, str], in_out_degrees=False):
    """
        sort_proteins_degrees is a function that sort set of proteins based on proteins degrees\n\n
        :param DiGraph: non-empty networkx.DiGraph class of PPI network
        :param proteins: non-empty list of non-empty string elements of proteins names
        :param order: default "descending" : non-empty str that decide the order of proteins degrees ranking\
                can be "descending" or "ascending" only

        :param save_file: default [False, str] : non-empty list of 2 elements first\
                of which is bool and second is non-empty string of the saved file name\
                this parameter decide if the proteins degrees ranking will be saved in a tsv file or not\
                and specify the saved file name (if the file name not specified default name will be given\
                '"sorted_proteins_degree_%s_order.txt" % order')
        :param in_out_degrees: default False : bool that decide to return number of proteins that point to and out of the given protein
        :return: list of dicts, each dict is keyed by the protein name and the value is a list of [proteins degrees] or [ proteins degrees,proteins in_degrees ,proteins out_degrees] if the in_out_degrees is True
        """
    ## Testing the parameters that user define

    ## testing if the DiGraph is non-empty networkx.DiGraph class and raise TypeError if not
    if not isinstance(DiGraph, nx.DiGraph) or len(DiGraph) == 0:
        raise TypeError("DiGraph should be non empty networkx.DiGraph class")

    ## testing if the proteins is non-empty list of strings elements and raise TypeError if not
    if not isinstance(proteins, list) or len(proteins) == 0 or any(
            not isinstance(protein, str) for protein in proteins) \
            or any(len(protein) == 0 for protein in proteins):
        raise TypeError("proteins should be non empty list of non-empty strings elements of proteins names")
    ## testing if order is non-empty str of values "descending" or "ascending" and use default value "descending" with a warning massage if not
    if order not in ["descending", "ascending"] or not isinstance(order, str):
        order = "descending"
        print(Fore.RED + "Warning:order value should be either 'descending' or 'ascending'\
            \nDefault value will be used: 'descending'")
    ## testing if save_file is of type list and its first element of type bool and use the default value [False, str] with a warning massage if not
    if not isinstance(save_file, list) or len(save_file) == 0 or not isinstance(save_file[0], bool):
        save_file = [False, str]
        print(Fore.RED + "Warning:save_file should be a list of 2 elements bool and non-empty str respectively\
                \nNo ranking file will be saved")
    ## testing if the in_out_degrees is of type bool and use the default value (False) with a warning massage if not
    if not isinstance(in_out_degrees, bool):
        in_out_degrees = False
        print(Fore.RED + "Warning:in_out_degrees should be either True or False\
                \nin_out_degrees now is at default value: False")

    ## Extracting proteins degrees through a for loop and append it to a list of dicts\
    ## in which each dict is keyed by protein name and the value is list of protein degrees
    proteins_degrees = []
    for protein in proteins:
        proteins_degrees.append({protein: [DiGraph.degree[protein]]})

    ## test if in_out_degrees is True or False
    if in_out_degrees:
        ## If True 2 elements will be appended to dict value list which are "protein_in_degree" and "protein_out_degree"
        # for loop to go through all dicts of our list of dicts
        for i in range(len(proteins_degrees)):
            protein_dict_value = proteins_degrees[i][proteins[i]]  # each dict value
            protein_in_degree = DiGraph.in_degree[proteins[i]]  # number of proteins pointing to our protein
            protein_out_degree = DiGraph.out_degree[proteins[i]]  # number of proteins pointing out of our protein

            protein_dict_value.append(protein_in_degree)  # appending protein_in_degree to the value of the dicts
            protein_dict_value.append(protein_out_degree)  # appending protein_out_degree to the value of the dicts

    ## test if order is "descending"
    if order == "descending":
        proteins_degrees.sort(key=lambda d: list(d.values())[0],
                              reverse=True)  # sorting by dicts value first element (proteins degrees)
    ## test if order is "ascending"
    elif order == "ascending":
        proteins_degrees.sort(key=lambda d: list(d.values())[0],
                              reverse=False)  # sorting by dicts value first element (proteins degrees)

    # test if the save_file parameter is True or False to save the sorted proteins by proteins degrees in a tsv file with the user defined name
    if save_file[0]:
        # test if the user mis-define saved file name and to save the tsv file with default name and printing warning massage of doing so
        if len(save_file) < 2 or len(save_file[1]) == 0 or not isinstance(save_file[1], str):
            save_file = [save_file[0], "sorted_proteins_degree_%s_order.txt" % order]
            print(Fore.RED + "Warning:File name not specified\
                            \nDefault name will be used:'%s'" % save_file[1])
        # open tsv file for writing
        with open(save_file[1], 'w') as sort_w:
            # test for in_out_degrees
            # if True the file will have 4 columns of Protein, Protein_degrees, Protein_in_degrees and Protein_out_degrees
            # if False the file will have 2 columns of Protein and Protein_degrees
            if in_out_degrees:
                header = "Protein\tProtein_degree\tProtein_in_degree\tProtein_out_degree\n"  # Define header row
                sort_w.write(header)  # write header row to the pre-defined tsv file
                # for loop to extract data
                for node in proteins_degrees:
                    Protein = list(node.keys())[0]  # Protein name
                    Protein_degree = node[Protein][0]  # Protein_degrees
                    Protein_in_degree = node[Protein][1]  # Protein_in_degrees
                    Protein_out_degree = node[Protein][2]  # Protein_out_degrees
                    line = "%s\t%d\t%d\t%d\n" % (
                        Protein, Protein_degree, Protein_in_degree, Protein_out_degree)  # each Line of the tsv file
                    sort_w.write(line)  # Writing line to the tsv file
            else:
                header = "Protein\tProtein_degree\n"  # Define header row
                sort_w.write(header)  # # write header row to the pre-defined tsv file
                # for loop to extract data
                for node in proteins_degrees:
                    Protein = list(node.keys())[0]  # Protein name
                    Protein_degree = node[Protein][0]  # Protein_degrees
                    line = "%s\t%d\n" % (Protein, Protein_degree)  # each Line of the tsv file
                    sort_w.write(line)  # Writing line to the tsv file

    return proteins_degrees
                            
def list_direct_connections(G, protein,saved_file_name="direct_connections.txt"):
    neighbors = list(G.neighbors(protein))
    degree = len(neighbors)  # calculating the degree of proteins
    connections = []  # list of proteins (neighbours) and weights
    for neighbor in neighbors:
        weight = G[protein][neighbor]['weight'] 
        connections.append((neighbor, weight))
    with open(saved_file_name, 'w') as f:  
        f.write(f"Degree: {degree}\n")
        for neighbor, weight in connections:
            f.write(f"{neighbor}: {weight}\n")
    return degree, connections
 
