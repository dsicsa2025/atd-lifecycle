import pandas as pd

# Function to calculate statistics for the 'number_of_changes' column
def calculate_change_statistics(file_path):
    # Load the CSV file
    data = pd.read_csv(file_path)

    # Clean the data: drop rows with missing values in the 'number_of_changes' column
    column_data = 'number_of_changes'
    cleaned_data = data.dropna(subset=[column_data])

  # Calculate the statistics
    mean_changes = cleaned_data[column_data].mean()
    median_changes = cleaned_data[column_data].median()
    min_changes = cleaned_data[column_data].min()
    max_changes = cleaned_data[column_data].max()
    std_changes = cleaned_data[column_data].std()

    # Print the results
    print(f"Mean: {mean_changes}")
    print(f"Median: {median_changes}")
    print(f"Minimum: {min_changes}")
    print(f"Maximum: {max_changes}")
    print(f"Standard Deviation: {std_changes}")

# Specify the path to your CSV file
file_path = 'ANALYZE-RESULTS/atd_final.csv'

# Call the function
calculate_change_statistics(file_path)
