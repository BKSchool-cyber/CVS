import csv

def read_csv_no_duplicates(file_path):
    seen_rows = set()
    unique_rows = []

    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            row_tuple = tuple(row)
            if row_tuple not in seen_rows:
                seen_rows.add(row_tuple)
                unique_rows.append(row)
    return unique_rows

# Example usage:
file_path = 'PCAP Data.csv'
data = read_csv_no_duplicates(file_path)
for row in data:
    print(row)
