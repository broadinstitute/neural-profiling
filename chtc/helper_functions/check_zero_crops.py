"""
Check if crops have zero values.
"""
import pandas as pd
import os
import cv2
import numpy as np

sample = '924_sample'
dump = '/local_group_storage/broad_data/michael/training/dump/'
os.makedirs(dump, exist_ok = True)

df = pd.read_csv(os.path.join(sample, 'sc-metadata.csv'))

def is_null(img_name, ls):
    img = cv2.imread(os.path.join(sample, img_name), cv2.IMREAD_GRAYSCALE)
    pos = np.nonzero(img)
    if len(pos[0]) == 0:
        print(img_name)
        ls.append(img_name)

ls = []
res = df.apply(lambda row: is_null(row['Image_Name'], ls), axis = 1)

if len(ls) < 50:
    for name in ls:
        df.drop(df[df['Image_Name'] == name].index, inplace=True)
        os.rename(os.path.join(sample, name), os.path.join(dump, name))
else:
    print('too many zeros. Something is wrong')


df.to_csv(os.path.join(sample, 'sc-metadata.csv'))

ls = pd.DataFrame(ls, columns=['missing'])
ls.to_csv('zero_crops.csv', index=False)