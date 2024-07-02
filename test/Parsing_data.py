proteins = []
with open("Participating Molecules [R-HSA-69620].tsv",'r') as handle:
    handle.readline()
    for line in handle.readlines():
        line = line.split()
        proteins.append(line[0])


Path_linker_proteins=[]
with open('PathLinker_2018_human-ppi-weighted-cap0_75.txt',"r") as handle:
    handle.readline()
    for line in handle.readlines():
        line = line.split("\t")
        if line[0] in proteins and line[1] in proteins:
            Path_linker_proteins.append(line)

with open("G2-M_DNA_damage_checkpoint_ppi.txt", "w") as h:
    h.write("#tail\thead\tedge_weight\tedge_type\n")
    for protein in Path_linker_proteins:
        h.write("%s\t%s\t%f\t%s" % (protein[0], protein[1], float(protein[2]), protein[3]))