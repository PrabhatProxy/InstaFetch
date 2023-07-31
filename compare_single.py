import sys
import csv

def read_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return [row[0] for row in reader]

def check_ids_exist(file_a, file_b):
    ids_a = read_csv(file_a)
    ids_b = read_csv(file_b)

    non_matching_rows = []
    for id_b in ids_b:
        if id_b not in ids_a:
            non_matching_rows.append([id_b])

    count_non_matching = len(non_matching_rows)

    return non_matching_rows, count_non_matching

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python compare_single.py A.csv B.csv")
        sys.exit(1)

    file_a = sys.argv[1]
    file_b = sys.argv[2]

    non_matching_rows, count_non_matching = check_ids_exist(file_a, file_b)

    if non_matching_rows:
        print("Non-matching entries in FileB:")
        for row in non_matching_rows:
            print(row[0])
        print(f"Number of non-matching entries: {count_non_matching}")
    else:
        print("All IDs in FileB exist in FileA.")
