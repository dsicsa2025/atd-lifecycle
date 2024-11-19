import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
data_atd = pd.read_csv('ANALYZE-RESULTS/atd_final.csv')
data_non = pd.read_csv('ANALYZE-RESULTS/non_atd_final.csv')

# data_atd = pd.read_csv(df_atd)
# data_non = pd.read_csv(df_non)


# Define columns to plot from each CSV file
columns_to_plot_atd = ['number_of_changes']
columns_to_plot_non = ['number_of_changes']

# Create a figure and a set of subplots for 2 boxplots
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(6, 2), sharex=False)

alias_atd = {
    'number_of_changes': 'ATD',
}

alias_non = {
    'number_of_changes': 'Non-ATD',
}

# Plot the boxplots from the first CSV file
for i, column in enumerate(columns_to_plot_atd):
    axes[i].boxplot(data_atd[column].dropna(), widths = 0.9, vert=False)
    axes[i].set_yticklabels([alias_atd[column]])
    #axes[i].set_ylabel(column)
    #axes[0].set_title('No. of Changes ATD')  # Display the sample size

    # Set labels
    #axes[i].set_ylabel(column)
    
    # Calculate the max value in the data to position the "N" label to the right
    max_value = data_atd[column].dropna().max()
    
    # Add "N = ..." label to the right side of the boxplot
    axes[i].text(max_value * 1.05, 1, f'N = {len(data_atd[column].dropna())}', 
                 va='center', ha='left', color='black')

print('\n\n')
print('\n\n')
fig.subplots_adjust(wspace=1, hspace=10)

# Plot the boxplots from the second CSV file
for j, column in enumerate(columns_to_plot_non, start=1):  # Start from index 2 to continue on the next subplots
    axes[j].boxplot(data_non[column].dropna(axis=0, how='any'), widths = 0.9, vert=False)
    axes[j].set_yticklabels([alias_non[column]])
    #axes[j].set_ylabel(column)
    axes[1].set_title('\n')
    axes[1].set_title('')
    #axes[j].set_title(f'N = {len(data_non[column].dropna())}')  # Display the sample size
    #axes[1].set_title('No. of Changes Non-ATD')

  # Set labels
    #axes[j].set_ylabel(column)
    
    # Calculate the max value in the data to position the "N" label to the right
    max_value = data_non[column].dropna().max()
    
    # Add "N = ..." label to the right side of the boxplot
    axes[j].text(max_value * 1.05, 1, f'N = {len(data_non[column].dropna())}', 
                 va='center', ha='left', color='black')

# Set a common x-axis label
axes[-1].set_xlabel('Values')

# Adjust the layout
plt.tight_layout()
#plt.savefig("boxplot_number_of_changes.pdf", format="pdf", bbox_inches="tight")

plt.show()