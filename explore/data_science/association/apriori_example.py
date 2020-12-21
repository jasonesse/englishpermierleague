import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
df = pd.read_csv('apriori_data.csv')
apri_df = apriori(df, min_support=0.5, use_colnames=False, max_len=None, verbose=0,low_memory=False)
rules = association_rules(apri_df, metric= 'confidence', min_threshold=0.3)
print(rules)