import pandas as pd
index = pd.read_csv('/local_group_storage/broad_data/michael/training/inputs/metadata/826_index.csv', low_memory=False)
index['Key'] = index['Metadata_Plate'] + "/" + index['Metadata_Well'] + "/" + index['Metadata_Site'].astype(str)
sub = index[["Key", "Split"]]

df = pd.read_csv('1017_sc/sc-metadata.csv', low_memory=False)
df = pd.merge(df, sub, how='left', on='Key', validate='many_to_one')


df.loc[df[(df['Split_x'] == "Training")].sample(frac=0.9).index, 'Split_x'] = 'Unused'
df.loc[df[(df.Split_y != 'Training') & (df.Split_x == "Training")].index, 'Split_x'] = 'Unused'

ls = df[df['Split_x'] == 'Training'].Compound.value_counts()
ls = ls[ls < 100].index.tolist()
for c in ls:
    df.loc[df[(df.Split_y == 'Training') & (df.Compound == c)].sample(frac=0.1).index, 'Split_x'] = 'Training'


df.loc[df[(df.Compound == "DMSO") & (df.Split_x == "Training")].sample(frac=0.95).index, 'Split_x'] = 'Unused'


df.to_csv("wip.csv", index=False)

