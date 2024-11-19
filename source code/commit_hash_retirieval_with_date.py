import csv
import subprocess
import os

# Path to the input CSV file containing file paths
csv_file_path = "file_path.csv"

# Path to the output CSV file where the results will be saved
output_csv_file = "RESULTS/camel-789-payment.csv"

# Ensure we're in the Git repository's root directory
repo_dir = "camel"  # Update this to your Git repository's root directory
os.chdir(repo_dir)  # Change the working directory to the repository root

# Date range for filtering commits
since_date = "2007-03-19 00:01"  # Start date (inclusive)
until_date = "2008-08-07 23:59"  # End date (inclusive)

# Function to get commit hashes for a file within a specified date range
def get_commit_hashes(file_path, since, until):
    try:
        # Run git log command to get the commit hashes for the specific file in the given time range
        result = subprocess.run(
            ["git", "log", f"--since={since}", f"--until={until}", "--pretty=format:%H", "--", file_path],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.splitlines()  # Return the hashes as a list
    except subprocess.CalledProcessError as e:
        print(f"Error processing file {file_path}: {e}")
        return []

# Open the output CSV file in write mode
with open(output_csv_file, mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    
    # Write the header to the output CSV file
    writer.writerow(["file_path", "commit_hash"])
    
    # Open and read the input CSV file
    with open(csv_file_path, mode='r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            file_path = row['file_path']
            print(f"Processing commit hashes for {file_path}:")
            
            # Get commit hashes for the file within the date range
            commit_hashes = get_commit_hashes(file_path, since_date, until_date)
            
            if commit_hashes:
                for commit in commit_hashes:
                    # Write each commit hash and file path to the output CSV
                    writer.writerow([file_path, commit])
            else:
                print(f"No commits found for {file_path}")
                writer.writerow([file_path, "-"])
            print("\n")

print(f"Commit hashes have been saved to {output_csv_file}")
