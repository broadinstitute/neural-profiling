# Neural-profiling
Author: Michael Bornholdt / November 2021

This repository relates to my work done at the Carpenter-Singh lab at the Broad institute of MIT and Harvard.
Within the summer of 2021, I develop a protocol for robustly and scalably quantifying (profiling) cellular states from images using deep neural networks.
The results and conclusions can be in the resulting Master thesis document `/Final_Masterthesis_Bornholdt.pdf`.

## Experiment IDs
Each experiment has a unique ID which refers to the day on which it was run, eg, 1028.
The `Training_index.md` file holds all information on which experiment was run on which parameters and which what data
In `/training/index` you can find all the index files for the different subsets of data. 
The `/training/runs` folder holds all profiles and training output from each experiment. 

## Folder structure
```commandline
.
├── LINCS_example_data
│   ├── inputs
│   │   ├── config
│   │   ├── images
│   │   ├── locations
│   │   └── metadata
│   └── outputs
├── baseline
│   ├── 01_data
│   │   ├── level_3_data
│   │   └── level_5_data
│   ├── 02_analysis
│   └── thesis
├── chtc
│   ├── DP_0.3.0
│   │   ├── aggregate
│   │   ├── checking
│   │   ├── profile
│   │   ├── sampling
│   │   └── train
│   ├── helper_functions
│   └── old_DP
│       ├── aggregate
│       ├── checking
│       ├── exporting
│       ├── profile
│       └── train
├── docker
│   ├── 0.3.0
│   └── old_versions
├── hit_k
├── pre-trained
│   ├── ResNet50v2
│   │   ├── aggregated
│   │   └── post_processing
│   ├── data-prep
│   │   ├── 01_location_extraction
│   │   └── 02_index_preperation
│   ├── efficient_net
│   │   ├── aggregated
│   │   └── post_processing
│   └── thesis
├── training
│   ├── aggregation
│   ├── index
│   │   └── sc-metadata
│   ├── prediction_analysis
│   │   └── 819
│   ├── results
│   │   └── accuracy
│   └── runs
│       ├── 1003
        ... 
│       └── 931
└── utils
```

## Description of the repository content
### `basline/`
The first part of the project gathers CellProfiler profiles from the LINCS repository and compares them. 
A general overview of the data and of the subselection is found here! 
If you want to compare metrics with my data, you need to follow the steps in `baseline/02_analysis/02_clean_data.ipynb`.

### `pre-trained/`
The two pre-trained nets are compared here and create the baseline for the trained neural networks. 
The best pipeline for deep learning features is determined.

### `training/`
All experiments live here. 
The experiments are different models trained with different hyperparameters and data. 
A full analysis of the resulting profiles can be found in the `training/results/` folder. 

### `chtc/` and `docker/`
These folders hold important scripts for setting up and running DeepProfiler on a server.

### `hit_k`
This folder contains the development code of the hit@k metric. Now on Cyto-eval/ 

### `LINCS_example_data/`
A small subsection of the LINCS data allows to test and learn DP. 
Alternatively used example data from DP Github.


## Experimental data on S3

- Compressed LINCS images:  
`s3://cellpainting-gallery/cpg0004-lincs/broad/2016_04_01_a549_48hr_batch1_compressed/images/` 
- Backup large csv files: `s3://cellpainting-gallery/cpg0004-lincs/broad/workspace/location_backups/`
- Location files: `s3://cellpainting-gallery/cpg0004-lincs/broad/workspace/deep_learning/inputs/locations/`
- LINCS sub index: `s3://cellpainting-gallery/cpg0004-lincs/broad/workspace/deep_learning/inputs/metadata/sub_index.csv`
- full enriched index: `s3://cellpainting-gallery/cpg0004-lincs/broad/workspace/deep_learning/inputs/metadata/enriched_index.csv`
- logs of experiments: `s3://cellpainting-gallery/cpg0004-lincs/broad/workspace/deep_learning/logs/`
- models: `s3://cellpainting-gallery/cpg0004-lincs/broad/workspace/deep_learning/models/`
- LINCS subsets crop (18 million): `s3://cellpainting-gallery/cpg0004-lincs/broad/workspace/deep_learning/crops/`



## Important random things
- Some information in this repository may be old since the DeepProfiler versions changed midway through the project
- The single cell crops of all 18 million cells within the LINCS subsection can be found on S3: `s3://cellpainting-gallery/cpg0004-lincs/broad/workspace/deep_learning/outputs/1017_sc/`
- If you can't reach Michael Bornholdt, try to reach Shantanu Singh. 

