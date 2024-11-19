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

def parse_module_name(filepath):
    """Extract the module name from an Erlang file."""
    with open(filepath, 'r') as f:
        for line in f:
            match = re.match(r"-module\((\w+)\).", line)
            if match:
                return match.group(1)
    return None

def find_dependencies(filepath, module_name):
    """Find dependencies (calls to other modules) in an Erlang file."""
    dependencies = set()
    with open(filepath, 'r') as f:
        for line in f:
            # Look for module:function pattern
            match = re.findall(r"(\w+):\w+\(", line)
            for dep_module in match:
                if dep_module != module_name:  # Exclude self-references
                    dependencies.add(dep_module)
    return dependencies

def calculate_fan_in_out(files):
    """Calculate FAN-IN and FAN-OUT for specified Erlang modules."""
    module_dependencies = {}
    module_usage = defaultdict(set)

    # Parse each file to get module name and dependencies
    for file in files:
        if not os.path.exists(file):
            print(f"File not found: {file}")
            continue

        module_name = parse_module_name(file)
        if module_name:
            dependencies = find_dependencies(file, module_name)
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
    # Path to the CSV file containing the Erlang file paths
    csv_file = "file_path.csv"
    
    # Retrieve files from CSV and calculate FAN-IN and FAN-OUT values
    files = get_files_from_csv(csv_file)
    fan_in_out_data = calculate_fan_in_out(files)
    
    # Display results
    display_fan_in_out(fan_in_out_data)