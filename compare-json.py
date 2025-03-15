import json
import sys

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def compare_json(obj1, obj2, path='', differences=None, similarities=None):
    if differences is None:
        differences = []
    if similarities is None:
        similarities = []
    
    diff_count_before = len(differences)

    # Type mismatch check
    if type(obj1) != type(obj2):
        differences.append(f"Type mismatch at {path}: {type(obj1).__name__} vs {type(obj2).__name__}")
        return differences, similarities

    # Compare dictionaries
    if isinstance(obj1, dict):
        keys1 = set(obj1.keys())
        keys2 = set(obj2.keys())
        
        # Check missing keys
        for key in keys1 - keys2:
            differences.append(f"Key missing in second file: {append_path(path, key)}")
        for key in keys2 - keys1:
            differences.append(f"Key missing in first file: {append_path(path, key)}")
        
        # Compare common keys
        for key in keys1 & keys2:
            new_path = append_path(path, key)
            compare_json(obj1[key], obj2[key], new_path, differences, similarities)

    # Compare lists
    elif isinstance(obj1, list):
        if len(obj1) != len(obj2):
            differences.append(f"Array length differs at {path}: {len(obj1)} vs {len(obj2)}")
        else:
            for i, (item1, item2) in enumerate(zip(obj1, obj2)):
                new_path = f"{path}[{i}]" if path else f"[{i}]"
                compare_json(item1, item2, new_path, differences, similarities)

    # Compare primitive values
    else:
        if obj1 != obj2:
            differences.append(f"Value differs at {path}: {repr(obj1)} vs {repr(obj2)}")
        else:
            similarities.append((path, obj1))

    # Add parent path if no differences were found in this subtree
    if len(differences) == diff_count_before:
        similarities.append((path, obj1))

    return differences, similarities

def append_path(current_path, new_element):
    if not current_path:
        return str(new_element)
    return f"{current_path}/{new_element}" if isinstance(new_element, str) else f"{current_path}[{new_element}]"

def print_differences(differences):
    if not differences:
        print("No differences found")
        return
    
    print(f"\nFound {len(differences)} differences:")
    for i, diff in enumerate(differences, 1):
        print(f"{i}. {diff}")

def print_similarities(similarities):
    if not similarities:
        print("No similar fields found")
        return
    
    # Remove duplicates while preserving order
    seen = set()
    unique_similarities = []
    for path, value in similarities:
        if path not in seen:
            seen.add(path)
            unique_similarities.append((path, value))

    print(f"\nFound {len(unique_similarities)} similar fields:")
    for i, (path, value) in enumerate(unique_similarities, 1):
        # Format path display
        display_path = "/ (root)" if path == "" else path
        # Convert value to JSON string for better formatting
        formatted_value = json.dumps(value, indent=2, ensure_ascii=False) if isinstance(value, (dict, list)) else repr(value)
        print(f"{i}. Path: {display_path}")
        print(f"   Value: {formatted_value}\n")

def main():
    if len(sys.argv) != 3:
        print("Usage: python compare_json.py <file1.json> <file2.json>")
        sys.exit(1)
    
    file1, file2 = sys.argv[1], sys.argv[2]
    
    try:
        data1 = load_json(file1)
        data2 = load_json(file2)
    except Exception as e:
        print(f"Error loading JSON files: {str(e)}")
        sys.exit(1)
    
    differences, similarities = compare_json(data1, data2)
    
    if data1 == data2:
        print("JSON files are identical")
    
    print_differences(differences)
    print_similarities(similarities)

if __name__ == "__main__":
    main()
