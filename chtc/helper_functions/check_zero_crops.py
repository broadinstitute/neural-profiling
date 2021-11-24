
"""
Check if crops have zero values.
"""
import pandas as pd
import os
import cv2
import numpy as np

sample = 'SQ00014818'

df = pd.read_csv(os.path.join(sample, 'sc-metadata.csv'))

def is_null(img_name):
    img = cv2.imread(os.path.join(sample, img_name), cv2.IMREAD_GRAYSCALE)
    pos = np.nonzero(img)
    if len(pos[0]) == 0:
        ls.append(img_name)

ls = []
res = df.apply(lambda row: is_null(row['Image_Name']), axis = 1)

if len(ls) < 100:
    for name in ls:
        df.drop(df[df['Image_Name'] == name].index, inplace=True)
        os.remove(os.path.join(sample, name))
else:
    print('too many zeros. Something is wrong')

df.to_csv(os.path.join(sample, 'sc-metadata.csv'))

ls = pd.DataFrame(ls, columns=['missing'])
ls.to_csv('zero_crops.csv', index=False)
