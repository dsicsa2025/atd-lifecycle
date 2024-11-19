import pandas as pd
from scipy.stats import mannwhitneyu


file_path = 'ANALYZE-RESULTS/atd_final.csv'


data = pd.read_csv(file_path)


data['intro-FAN-IN'] = pd.to_numeric(data['intro-FAN-IN'], errors='coerce')
data['payment-FAN-IN'] = pd.to_numeric(data['payment-FAN-IN'], errors='coerce')

data['intro-FAN-OUT'] = pd.to_numeric(data['intro-FAN-OUT'], errors='coerce')
data['payment-FAN-OUT'] = pd.to_numeric(data['payment-FAN-OUT'], errors='coerce')

#FAN-IN
before_in = data['intro-FAN-IN'].dropna(axis=0, how='any')
after_in = data['payment-FAN-IN'].dropna(axis=0, how='any')

#FAN-OUT
before_out = data['intro-FAN-OUT'].dropna(axis=0, how='any')
after_out = data['payment-FAN-OUT'].dropna(axis=0, how='any')

# Mann-Whitney U Test 
u_stat, p_value = mannwhitneyu(before_in, after_in)
print(f'FAN-IN ATD - Mann-Whitney U Statistic: {u_stat}, p-value: {p_value}')

u_stat, p_value = mannwhitneyu(before_out, after_out)
print(f'FAN-OUT ATD - Mann-Whitney U Statistic: {u_stat}, p-value: {p_value}')
