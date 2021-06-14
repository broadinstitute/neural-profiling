# baseline 
This folder is about the first part of the project. 
The aim is to figure out the replicate reproducibility of the old pipeline, i.e. Classical feature extraction from CellProfiler and then the postprocessing by pycytominer.

The analysis folder has notebooks including the important steps of choosing data and running the evaluations.

## data

`2016_04_01_a549_48hr_batch1_consensus_modz_feature_select_dmso.csv.gz`  
This file is from the consensus lincs directory:  
https://github.com/broadinstitute/lincs-cell-painting/tree/master/consensus/2016_04_01_a549_48hr_batch1

`selected_data_df.csv`  
This is a subset of the above data. It is selected in the `02_clean_data.ipynb`

## analysis
This folder contains all notebooks. Most importantly the data is cleaned and selected here and the anaylsis is demonstrated.

## results
This is a collection of images and numerical results.