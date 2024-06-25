import csv

#read the file and make a list of tuples

file_path = "/home/work/PathLinker_2018_human-ppi-weighted-cap0_75.txt"
output_file_path = "/home/work/output.txt"
def read_file(file_path, delimiter="\t"):
    tuples_list = []
    
    with open(file_path, 'r') as file:
        data = csv.reader(file, delimiter=delimiter)
        
        # Read the header row and skip the # character
        headers = next(data)

        # Find the index of the "edge_type" column
        column_index = headers.index("edge_type")
        
        for row in data:
            # Exclude the "edge_type" column and create a tuple
            filtered_row = tuple(value for index, value in enumerate(row) if index != column_index)
            tuples_list.append(filtered_row)

    return tuples_list

#save the list of tuples to a file with the header row
def save_file(data, output_file_path, delimiter="\t"):
    with open(output_file_path, 'w') as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerow(["#tail", "head", "edge_weight"])
        writer.writerows(data)

try:
    result = read_file(file_path)
    save_file(result, output_file_path)
    print(f"File saved successfully at: {output_file_path}")
except FileNotFoundError:
    print(f"The file {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

