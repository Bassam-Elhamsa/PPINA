import networkx as nx
import matplotlib.pyplot as plt
from colorama import Fore

def proteins_degrees_hist(DiGraph, proteins, bin_width=500, log=False, show=True,
                          save_file=[False, "Histogram of proteins degree"]):
    """
    proteins_degrees_hist is a function that draw a histogram for a set of proteins connection degree
    that is extracted from PPI network graph

    Required parameters:\n
    1- DiGraph : non-empty networkx.DiGraph class of PPI network
    2- proteins : non-empty list of non-empty string elements of proteins names

    optional parameters:\n
    1- bin_width : default 500 : integer that decide width of bins of the histogram\n
    2- log : default False : bool that decide whether to use log transformation to better visualize condensed data\n
    3- save_file : default [False, "Histogram of proteins degree.png"] : non-empty list of 2 elements first of which is
    bool and second is non-empty string of the saved file name this parameter decide if the histogram will be saved
    or not and specify the saved file name (if the file name not specified default name will be given 'Histogram of proteins degree')\n
    4- show : default True : bool that decide whether histogram will be shown or not

    proteins_degrees_hist return figure of histogram for set of proteins connection degrees
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

    # test if the show parameter is True or False to show the histogram
    if show:
        plt.show()

    # test if the save_file parameter is True or False to save the histogram with the user defined name
    if save_file[0]:
        # test if the user mis-define saved file name and to save the histogram with default name and printing warning massage of doing so
        if len(save_file) < 2 or len(save_file[1]) == 0 or not isinstance(save_file[1], str):
            plt.savefig("Histogram of proteins degree.png", dpi=300)
            print(
                Fore.RED + "Warning:File name not specified\nDefault name will be used:'Histogram of proteins degree'")
        else:
            plt.savefig(save_file[1], dpi=300)

