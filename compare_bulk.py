import csv

def read_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return [row[0] for row in reader]

def check_ids_exist(file_a, file_list):
    ids_a = read_csv(file_a)

    non_matching_files = {}
    for file_b in file_list:
        ids_b = read_csv(file_b)
        non_matching_rows = []
        for id_b in ids_b:
            if id_b not in ids_a:
                non_matching_rows.append([id_b])

        count_non_matching = len(non_matching_rows)
        non_matching_files[file_b] = (non_matching_rows, count_non_matching)

    return non_matching_files

if __name__ == "__main__":
    # Provide the list of file names you want to match with File A
    file_list = [f"{i}.csv" for i in range(31, 40 + 1)]

    file_a = "followers.csv"

    non_matching_files = check_ids_exist(file_a, file_list)

    for file_b in non_matching_files:
        non_matching_rows, count_non_matching = non_matching_files[file_b]
        if non_matching_rows:
            print(f"*Non-matching entries in {file_b}:")
            for row in non_matching_rows:
                print(row[0])
            print(f"Number of non-matching entries in {file_b}: {count_non_matching}")
            print(" ")
        else:
            print(f"All IDs in {file_b} exist in FileA.")
