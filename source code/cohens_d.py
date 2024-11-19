import numpy as np
import pandas as pd

# Function to calculate Cohen's d
def cohens_d(x, y):
    diff = np.mean(x) - np.mean(y)
    pooled_std = np.sqrt((np.std(x, ddof=1) ** 2 + np.std(y, ddof=1) ** 2) / 2)
    return diff / pooled_std

# Load the dataset
file_path = 'ANALYZE-RESULTS/atd_final.csv'
data = pd.read_csv(file_path)


# data['INTRO-Called-By-Dependencies'].fillna(0, inplace=True)
# data['PAYMENTNACalledNAByNADependencies'].fillna(0, inplace=True)

data['payment-FAN-IN'] = data['payment-FAN-IN'].dropna(axis=0, how='any')
data['intro-FAN-IN'] = data['intro-FAN-IN'].dropna(axis=0, how='any')

data['payment-FAN-OUT'] = data['payment-FAN-OUT'].dropna(axis=0, how='any')
data['intro-FAN-OUT'] = data['intro-FAN-OUT'].dropna(axis=0, how='any')

# Calculate Cohen's d for intro-called-by and payment-called-by

# d_value = cohens_d([1, 1, 1], [1, 1, 1])
# print(f"Sample Cohen's d: {d_value}")

# FAN-IN
fan_in_cohens_d_value = cohens_d(data['payment-FAN-IN'], data['intro-FAN-IN'])
# Display the result
print(f"FAN-IN Cohen's d: {fan_in_cohens_d_value}")


# #FAN-OUT
fan_out_cohens_d_value = cohens_d(data['payment-FAN-OUT'], data['intro-FAN-OUT'])
# Display the result
print(f"FAN-OUT Cohen's d: {fan_out_cohens_d_value}")
