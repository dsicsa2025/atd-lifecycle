import pandas as pd
import pingouin as pg

# Baca data dari file CSV
data = pd.read_csv("ANALYZE-RESULTS/atd_final.csv")

data = data.dropna(subset=['number_of_changes', 'payment-complexity', 'payment-sloc'])

# We want to control the variable 'SLOC' (Source Lines of Code)

# Calculate Partial Spearman Correlation
partial_corr = pg.partial_corr(data=data,
x='number_of_changes',                               
y='payment-complexity',
covar='payment-sloc',
method='spearman')
print(partial_corr)
