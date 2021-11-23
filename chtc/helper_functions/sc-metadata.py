import pandas as pd

df = pd.read_csv('sc-metadata.csv', low_memory=False)

df['Split'] = "Unused"

print(df.columns)

compounds = df.Compound.unique()

for c in compounds:
    df.loc[df[df.Compound == c].sample(frac=0.05).index, 'Split'] = 'Training'
    df.loc[df[(df.Compound == c) & (df.Split == "Unused")].sample(frac=0.005).index, 'Split'] = 'Validation'

print(df[df['Split'] == 'Training'].Compound.value_counts())
print(df[df['Split'] == 'Validation'].Compound.value_counts())


df.loc[df[(df.Compound == "DMSO") & (df.Split == "Training")].sample(frac=0.9).index, 'Split'] = 'Unused'
df.loc[df[(df.Compound == "DMSO") & (df.Split == "Validation")].sample(frac=0.9).index, 'Split'] = 'Unused'

print(df[df['Split'] == 'Training'].Compound.value_counts())
print(df[df['Split'] == 'Validation'].Compound.value_counts())


df.to_csv("sc_1016.csv",index=False)
