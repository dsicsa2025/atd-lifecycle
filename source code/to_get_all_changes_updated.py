import csv
from pydriller import Repository

# Function to find the last known path of a file, including if it was renamed, moved, or deleted
def find_last_known_path(repo_path, original_file_path):
    repo = Repository(repo_path)
    last_known_path = original_file_path  # Start with the original path
    file_status = 'Not Found'  # Default status if not found

    for commit in repo.traverse_commits():
        for modified_file in commit.modified_files:
            # Check if the file path matches the last known path or the original file path
            if last_known_path == modified_file.new_path or last_known_path == modified_file.old_path:
                # If the file is moved or renamed
                if modified_file.old_path and modified_file.new_path:
                    last_known_path = modified_file.new_path
                    file_status = 'Moved or Renamed'
                else: 
                    file_status = 'Exists'
                
            # Check if the file was deleted
            if modified_file.change_type.name == 'DELETE' and last_known_path == modified_file.old_path:
                file_status = 'Deleted'
                return last_known_path, file_status  # Return the last known path before deletion

    return last_known_path, file_status  # Return the last path and status (either 'Exists', 'Moved', 'Renamed', or 'Deleted')

# Read the list of files from a CSV
def read_file_list(input_csv):
    with open(input_csv, newline='') as csvfile:
        reader = csv.reader(csvfile)
        file_list = [row[0] for row in reader]  # Assuming file paths are in the first column
    return file_list

# Save the results into a CSV file
def save_results_to_csv(output_csv, results):
    with open(output_csv, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Original Path', 'Last Known Path', 'Status'])  # CSV headers
        writer.writerows(results)

# Main function to process the list of files
def process_files(repo_path, input_csv, output_csv):
    file_list = read_file_list(input_csv)
    results = []

    for file_path in file_list:
        last_known_path, status = find_last_known_path(repo_path, file_path)
        results.append([file_path, last_known_path, status])

    save_results_to_csv(output_csv, results)

# Example usage
repo_path = 'camel'  # Path to your git repository
input_csv = 'file_path.csv'    # CSV file containing list of file paths
output_csv = 'LAST_KNOWN_PATH/last_known_path-camel-789-payment.csv'  # CSV file to save the results

process_files(repo_path, input_csv, output_csv)