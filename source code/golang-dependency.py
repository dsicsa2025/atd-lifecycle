import os
import re
import csv
from collections import defaultdict

def get_files_from_csv(csv_file):
    """Retrieve file paths from a CSV file."""
    files = []
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            files.append(row[0])  # Assumes file paths are in the first column
    return files

def parse_imports(filepath):
    """Extract imported packages from a Go file."""
    imports = set()
    with open(filepath, 'r') as f:
        in_import_block = False
        for line in f:
            # Handle import blocks and single imports
            if re.match(r"^import\s+\(", line):  # Start of import block
                in_import_block = True
            elif in_import_block and line.strip() == ")":  # End of import block
                in_import_block = False
            elif in_import_block or re.match(r"^import\s+", line):
                match = re.findall(r"\"([^\"]+)\"", line)
                imports.update(match)
    return imports

def parse_function_calls(filepath):
    """Find function calls in a Go file."""
    dependencies = set()
    with open(filepath, 'r') as f:
        for line in f:
            # Look for pattern package.Function or package.Function(...)
            match = re.findall(r"(\w+)\.\w+\(", line)
            dependencies.update(match)
    return dependencies

def calculate_fan_in_out(files):
    """Calculate FAN-IN and FAN-OUT for specified Go files."""
    module_dependencies = {}
    module_usage = defaultdict(set)
    
    # Parse each file to get dependencies and imports
    for file in files:
        if not os.path.exists(file):
            print(f"File not found: {file}")
            continue
        
        # Parse imports and function calls to detect dependencies
        imports = parse_imports(file)
        function_calls = parse_function_calls(file)
        dependencies = imports.union(function_calls)
        
        module_name = os.path.basename(file)
        module_dependencies[module_name] = dependencies
        for dep in dependencies:
            module_usage[dep].add(module_name)

    # Calculate FAN-IN and FAN-OUT
    fan_in_out_data = {}
    for module in module_dependencies:
        fan_out = len(module_dependencies[module])
        fan_in = len(module_usage[module])
        fan_in_out_data[module] = {"FAN-IN": fan_in, "FAN-OUT": fan_out}

    return fan_in_out_data

def display_fan_in_out(data):
    """Display the FAN-IN and FAN-OUT values in a table."""
    print(f"{'Module':<20} {'FAN-IN':<10} {'FAN-OUT':<10}")
    print("-" * 40)
    for module, values in data.items():
        print(f"{module:<20} {values['FAN-IN']:<10} {values['FAN-OUT']:<10}")

if __name__ == "__main__":
    # Path to the CSV file containing the Go file paths
    csv_file = "file_path.csv"
    
    # Retrieve files from CSV and calculate FAN-IN and FAN-OUT values
    files = get_files_from_csv(csv_file)
    fan_in_out_data = calculate_fan_in_out(files)
    
    # Display results
    display_fan_in_out(fan_in_out_data)