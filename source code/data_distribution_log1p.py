import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the CSV file (replace with your file path if needed)
# Load the CSV file into a DataFrame

#df = pd.read_csv('ANALYZE-RESULTS/atd_final.csv')
df = pd.read_csv('ANALYZE-RESULTS/atd_final.csv')


#df = pd.read_csv('ANALYZE-RESULTS/normalized_atd_final.csv')
#df = pd.read_csv('ANALYZE-RESULTS/normalized_non_atd_final.csv')

# # Specify the columns you want to plot
intro_fan_in = 'intro-FAN-IN'  # replace with the actual column name
payment_fan_in = 'payment-FAN-IN'  # replace with the actual column name

# Specify the columns you want to plot
# intro_fan_in = 'normalized_intro-FAN-IN'  # replace with the actual column name
# payment_fan_in = 'normalized_payment-FAN-IN'  # replace with the actual column name


df[intro_fan_in] = pd.to_numeric(df[intro_fan_in], errors='coerce')

df[payment_fan_in] = pd.to_numeric(df[payment_fan_in], errors='coerce')

#------------------------------------------------
# Apply log transformation to intro-FAN-IN and intro-FAN-OUT using np.log1p
df[intro_fan_in] = np.log1p(df[intro_fan_in])
df[payment_fan_in] = np.log1p(df[payment_fan_in])

#.dropna(axis=0, how='any')


# Plot histograms instead of KDE
plt.figure(figsize=(12, 6))

# FAN-IN histogram
plt.subplot(2, 2, 1)
sns.histplot(df[intro_fan_in], kde=True, bins=20)

# Calculate and plot the median
intro_median_in = df[intro_fan_in].median()
plt.axvline(intro_median_in, color='red', linestyle='--', label=f'Median: {intro_median_in:.2f}')

#plt.title('Log-Transformed Distribution of intro-FAN-IN')
plt.xlabel('log(Initial Commit FAN-IN + 1)')
plt.ylabel('Distribution')
plt.legend()
#plt.show()
# plt.hist(data_intro['INTRO-Calls-Dependencies'],# bins=20, density=True, alpha=0.6, color='g')
# #plt.title('Histogram of intro-FAN-OUT')
# plt.xlabel('Intro FAN-OUT')
# plt.ylabel('Density')

# FAN-OUT histogram
plt.subplot(2, 2, 2)
sns.histplot(df[payment_fan_in], kde=True, bins=20)

payment_median_in = df[payment_fan_in].median()
plt.axvline(payment_median_in, color='red', linestyle='--', label=f'Median: {payment_median_in:.2f}')

#lt.title('Histogram and KDE of intro-FAN-OUT')
#plt.title('Log-Transformed Distribution of intro-FAN-OUT')
plt.xlabel('log(Recorded FAN-IN + 1)')
plt.ylabel('Distribution')
plt.legend()
# plt.hist(data_payment['PAYMENTNACallsNADependencies'], bins=20, density=True, alpha=0.6, color='g')
# #plt.title('Histogram of payment-FAN-OUT')
# plt.xlabel('Payment FAN-OUT')
# plt.ylabel('Density')


# print('\n\n')
# print('\n\n')
# plt.subplots_adjust(wspace=1, hspace=10)


# Specify the columns you want to plot
intro_fan_out = 'intro-FAN-OUT'  # replace with the actual column name
payment_fan_out = 'payment-FAN-OUT'  # replace with the actual column name

# intro_fan_out = 'normalized_intro-FAN-OUT'  # replace with the actual column name
# payment_fan_out = 'normalized_payment-FAN-OUT'  # replace with the actual column name


df[intro_fan_out] = pd.to_numeric(df[intro_fan_out], errors='coerce')

df[payment_fan_out] = pd.to_numeric(df[payment_fan_out], errors='coerce')

#------------------------------------------------
# Apply log transformation to intro-FAN-IN and intro-FAN-OUT using np.log1p
df[intro_fan_out] = np.log1p(df[intro_fan_out])
df[payment_fan_out] = np.log1p(df[payment_fan_out])

# Plot histograms instead of KDE
#plt.figure(figsize=(12, 6))

# FAN-IN histogram
plt.subplot(2, 2, 3)
sns.histplot(df[intro_fan_out], kde=True, bins=20, color='lightgrey')

# Calculate and plot the median
intro_median_out = df[intro_fan_out].median()
plt.axvline(intro_median_out, color='red', linestyle='--', label=f'Median: {intro_median_out:.2f}')

#plt.title('Log-Transformed Distribution of intro-FAN-IN')
plt.xlabel('log(Initial Commit FAN-OUT + 1)')
plt.ylabel('Distribution')
plt.legend()
#plt.show()
# plt.hist(data_intro['INTRO-Calls-Dependencies'], bins=20, density=True, alpha=0.6, color='g')
# #plt.title('Histogram of intro-FAN-OUT')
# plt.xlabel('Intro FAN-OUT')
# plt.ylabel('Density')

# FAN-OUT histogram
plt.subplot(2, 2, 4)
sns.histplot(df[payment_fan_out], kde=True, bins=20, color='lightgrey')

payment_median_out = df[payment_fan_out].median()
plt.axvline(payment_median_out, color='red', linestyle='--', label=f'Median: {payment_median_out:.2f}')

#lt.title('Histogram and KDE of intro-FAN-OUT')
#plt.title('Log-Transformed Distribution of intro-FAN-OUT')
plt.xlabel('log(Recorded FAN-OUT + 1)')
plt.ylabel('Distribution')
plt.legend()
# plt.hist(data_payment['PAYMENTNACallsNADependencies'], bins=20, density=True, alpha=0.6, color='g')
# #plt.title('Histogram of payment-FAN-OUT')
# plt.xlabel('Payment FAN-OUT')
# plt.ylabel('Density')

#plt.savefig("merged_non_atd_in_out.pdf", format="pdf", bbox_inches="tight")
plt.tight_layout()
plt.show()