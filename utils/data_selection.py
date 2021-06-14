import pandas as pd
from pycytominer.cyto_utils import infer_cp_features
import numpy as np


def drop_feats(df, threshold):
    features = infer_cp_features(df)
    drop_features = []
    for feat in features:
        if (np.abs(df[feat]) > threshold).any():
            drop_features.append(feat)
    df_out = df.drop(drop_features, axis="columns")
    print("dropped {} features".format(len(drop_features)))
    return df_out


def clean_moas(df: pd.DataFrame):
    # 1. Only keep the dose 6 and dose 0 (DMSO)
    df = df.query("Metadata_dose_recode == 0 | Metadata_dose_recode == 6 ")
    # 2. Get rid of all compounds that have unknown MOAs
    df = pd.concat(
        [df.query("Metadata_moa != 'unknown'"),
         df.query("Metadata_broad_sample == 'DMSO'")],
        ignore_index=True
    )
    # 3. Drop all single Moas
    ls = df.Metadata_moa.value_counts() != 1
    keys = ls[ls].keys()
    df = df[df["Metadata_moa"].isin(keys)]
    return df
