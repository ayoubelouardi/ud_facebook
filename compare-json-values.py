import json
import sys

def find_matching_values(file1_path, file2_path):
    """
    Loads two JSON files, finds matching values, and prints the matching key-value pairs.
    Handles both dictionaries and lists of dictionaries.
    """

    try:
        with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
            data1 = json.load(f1)
            data2 = json.load(f2)

        def extract_values(data):
            """Helper function to extract values from dictionaries or lists of dictionaries."""
            values = []
            if isinstance(data, dict):
                for value in data.values():
                    values.append(value)
            elif isinstance(data, list):
                for item in data:
                    if isinstance(item, dict):
                        for value in item.values():
                            values.append(value)
            return values

        def extract_items(data):
            """Helper function to extract key-value pairs from dictionaries or lists of dictionaries."""
            items = []
            if isinstance(data, dict):
                for key, value in data.items():
                    items.append((key, value))
            elif isinstance(data, list):
                for item in data:
                    if isinstance(item, dict):
                        for key, value in item.items():
                            items.append((key, value))
            return items

        values1 = extract_values(data1)
        values2 = extract_values(data2)

        items1 = extract_items(data1)
        items2 = extract_items(data2)

        for key1, value1 in items1:
            if value1 in values2:
                for key2, value2 in items2:
                    if value1 == value2:
                        print(f"this key-value '{key1}':'{value1}' is the same as '{key2}':'{value2}'")

    except FileNotFoundError:
        print("Error: One or both files not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in one or both files.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py file1.json file2.json")
    else:
        file1_path = sys.argv[1]
        file2_path = sys.argv[2]
        find_matching_values(file1_path, file2_path)    