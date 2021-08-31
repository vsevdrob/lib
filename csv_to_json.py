import csv
import json

def make_json(csv_file_path, json_file_path, primary_column):
    """Convert CSV to JSON."""
    data = {}
	# Open a CSV reader.
    with open(csv_file_path, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        # Convert each row into a dictionary and add it to data.
        for rows in csvReader:
            key = rows[primary_column]
            data[key] = rows
    # Dumping data to JSON.
    with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

if __name__ == "__main__":
    # Requesting for user input and making JSON.
    csv_file_path = input(r"-> Path to CSV file:   ")
    json_file_path = input(r"-> Path to JSON file:  ")
    primary_column = input("-> Primary column key: ")
    make_json(csv_file_path, json_file_path, primary_column)
