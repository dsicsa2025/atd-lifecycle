import subprocess
import pandas as pd
import os

# Define the path to the Apache Camel project directory
project_dir = "camel"

# Load your CSV file with the list of files
csv_file = "file_path.csv"
df = pd.read_csv(csv_file)

# Assuming the CSV has a column 'file_path' with file paths
file_paths = df['file_path'].tolist()

# Create a dictionary to store file paths and their respective SLOC
sloc_data = {}

# Loop over each file path and calculate SLOC using cloc
for file in file_paths:
    try:
        # Construct the full path to the file
        full_file_path = os.path.join(project_dir, file)

        # Run cloc command to get the SLOC for each file
        result = subprocess.run(['cloc', full_file_path, '--csv'], capture_output=True, text=True)
        # Extract the SLOC from cloc's CSV output (second line contains the data)
        lines = result.stdout.splitlines()
        if len(lines) > 1:
            sloc_line = lines[1]
            sloc_values = sloc_line.split(',')
            # Extract SLOC value (physical lines of code is usually in the 4th column of cloc output)
            sloc = int(sloc_values[4]) if sloc_values[4].isdigit() else 0
            sloc_data[file] = sloc
        else:
            sloc_data[file] = 0
    except Exception as e:
        print(f"Error processing {file}: {e}")
        sloc_data[file] = 0

# Convert the results into a DataFrame and display them
sloc_df = pd.DataFrame(list(sloc_data.items()), columns=['file_path', 'sloc'])

# Save the DataFrame to a CSV file
output_csv_file = "SLOC/camel-789-payment.csv"
sloc_df.to_csv(output_csv_file, index=False)

print(f"SLOC results have been saved to {output_csv_file}")


#korelasi sloc dengan complexity, intro and payment
