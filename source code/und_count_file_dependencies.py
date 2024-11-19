import understand
import csv

# Open the Understand database
db = understand.open("camel-789-payment.und")

# Function to count dependencies for a given file
def count_dependencies(file):
    # FAN-OUT: Number of components this file depends on (calls)
    calls = file.depends()  # Dependencies that this file "calls"
    
    # FAN-IN: Number of components that depend on this file (called by)
    called_by = file.dependsby()  # Dependencies that "call" this file
    
    # Count the dependencies
    fan_out = len(calls)
    fan_in = len(called_by)
    
    return fan_in, fan_out

# Read list of filenames from CSV
def process_files_from_csv(input_csv, output_csv):
    with open(input_csv, newline='') as csvfile:
        reader = csv.reader(csvfile)
        file_results = []

        # Skip header if present in the input CSV
        next(reader, None)

        # Iterate over the rows, assuming the first column contains the filenames
        for row in reader:
            filename = row[0]  # Assuming the filename is in the first column

            # Lookup the file entity in the Understand database
            file_entity = db.lookup(filename, "file")
            if file_entity:
                file = file_entity[0]  # Get the first matching file entity

                # Count the dependencies
                fan_in, fan_out = count_dependencies(file)
                
                # Store the result (filename, FAN-IN, FAN-OUT)
                file_results.append([filename, fan_in, fan_out])
            else:
                print(f"File '{filename}' not found in the database.")
                file_results.append([filename, '-', '-'])

    # Write the results to a new CSV file
    with open(output_csv, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Filename', 'FAN-IN', 'FAN-OUT'])  # CSV Header
        writer.writerows(file_results)

    print(f"Results written to {output_csv}")

# Specify the input CSV and output CSV
input_csv = "file_path.csv"  # The input CSV file containing the list of filenames
output_csv = "COUNT_DEPENDENCY/camel-789-payment.csv"  # The output CSV file to write the results

# Process the files and generate the dependency graph count
process_files_from_csv(input_csv, output_csv)