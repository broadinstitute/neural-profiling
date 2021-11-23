import pandas as pd
import os

# insert the sample to check
sample = '817_sample'

df = pd.read_csv(os.path.join(sample, 'sc-metadata.csv'))

def crop_exists(img_name, ls):
    if not os.path.isfile(os.path.join(sample, img_name)):
        ls.append(img_name)

# create a list of missing crops and save that list
ls = []
res = df.apply(lambda row: crop_exists(row['Image_Name'], ls), axis = 1)

ls = pd.DataFrame(ls, columns=['missing_crops'])
ls.to_csv('missing_crops.csv', index=False)
