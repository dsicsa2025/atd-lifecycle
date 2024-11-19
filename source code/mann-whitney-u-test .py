import pandas as pd
from scipy.stats import mannwhitneyu


file_path = 'ANALYZE-RESULTS/atd_final.csv'


data = pd.read_csv(file_path)


data['intro-FAN-IN'] = pd.to_numeric(data['intro-FAN-IN'], errors='coerce')
data['payment-FAN-IN'] = pd.to_numeric(data['payment-FAN-IN'], errors='coerce')



#FAN-IN
before = data['intro-FAN-IN'].dropna(axis=0, how='any')
after = data['payment-FAN-IN'].dropna(axis=0, how='any')


#FAN-IN
# before = intro_data['INTRO-Calls-Dependencies']
# after = payment_data['PAYMENTNACallsNADependencies']




# Mann-Whitney U Test untuk dua grup tidak berpasangan
u_stat, p_value = mannwhitneyu(before, after)
print(f'FAN-IN NON-ATD - Mann-Whitney U Statistic: {u_stat}, p-value: {p_value}')