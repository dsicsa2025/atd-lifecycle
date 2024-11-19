import csv
import lizard
import os

# Function to calculate McCabe Cyclomatic Complexity using lizard
def calculate_mccabe_complexity(file_path):
    try:
        # Analyze the file using lizard
        analysis = lizard.analyze_file(file_path)

        # Sum all the cyclomatic complexity values
        total_complexity = sum(func.cyclomatic_complexity for func in analysis.function_list)
        
        # Return the total complexity and the number of functions analyzed
        return total_complexity, len(analysis.function_list)

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None, None

# Read list of files from CSV and process them
def process_files_from_csv(repo_path, input_csv, output_csv):
    file_results = []

    with open(input_csv, newline='') as csvfile:
        reader = csv.reader(csvfile)

        # Skip header if present in the input CSV
        next(reader, None)

        # Iterate over the rows, assuming the first column contains the file paths
        for row in reader:
            filename = row[0]  # Assuming the filename is in the first column
            file_path = os.path.join(repo_path, filename)

            if os.path.exists(file_path):
                # Calculate McCabe Cyclomatic Complexity
                total_complexity, num_functions = calculate_mccabe_complexity(file_path)
                
                if total_complexity is not None and num_functions is not None:
                    avg_complexity = total_complexity / num_functions if num_functions > 0 else 0
                else:
                    avg_complexity = '-'
                    total_complexity = '-'
                
                # Store the result (filename, total complexity, average complexity)
                file_results.append([filename, total_complexity, avg_complexity])
            else:
                print(f"File '{filename}' not found in the repository.")
                file_results.append([filename, '-', '-'])

    # Write the results to a new CSV file
    with open(output_csv, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Filename', 'Total McCabe Cyclomatic Complexity', 'Average McCabe Cyclomatic Complexity'])  # CSV Header
        writer.writerows(file_results)

    print(f"Results written to {output_csv}")

# Specify the repository path, input CSV, and output CSV
repo_path = "camel"  # Path to the local Git repository
input_csv = "file_path.csv"  # The input CSV file containing the list of file paths
output_csv = "CYCLOMATIC_COMPLEXITY/lizard-camel-789-payment.csv"  # The output CSV file to write the results

# Process the files and calculate McCabe Cyclomatic Complexity
process_files_from_csv(repo_path, input_csv, output_csv)