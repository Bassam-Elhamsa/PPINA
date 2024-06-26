import csv

# reading the file and make a list of tuples
file_path = "/home/work/PathLinker_2018_human-ppi-weighted-cap0_75.txt"
output_file_path = "/home/work/output.txt"


def read_file(file_path, delimiter="\t"):
    try:
        list_of_tuples = []
        with open(file_path, "r") as file:
            data = csv.reader(file, delimiter = delimiter)
            headers = next(data)
            column_index = headers.index("edge_type")

            for row in data:
                filtered_row = tuple(value for index, value in enumerate(row) if index != column_index)
                list_of_tuples.append(filtered_row)
        return list_of_tuples
    except FileNotFoundError:
        print("Data file is missing!")

# save the output
def save_list(data, output_file_path, delimiter="\t"):
    with open(output_file_path, 'w') as output_file:
        write_output = csv.writer(output_file, delimiter = delimiter)
        write_output.writerow(["#tail", "head", "edge_weight"])
        write_output.writerows(data)


try:
    output = read_file(file_path)
    save_list(output, output_file_path)
except FileNotFoundError:
    print("Please provide a valid file path!")
except Exception as e:
    print(f"An error occurred: {e}")
