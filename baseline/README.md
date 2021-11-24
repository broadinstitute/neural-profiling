# Baseline 
This folder is about the first part of the project. 
The aim is to figure out the replicate reproducibility of the old pipeline, i.e. Classical feature extraction from CellProfiler and then the postprocessing by pycytominer.

The analysis folder has notebooks including the important steps of choosing data and running the evaluations.

## Data

Most data used in this folder comes form the LINCS repository, eg:
https://github.com/broadinstitute/lincs-cell-painting/tree/master/consensus/2016_04_01_a549_48hr_batch1

## Analysis
This folder contains all notebooks. Most importantly the data is cleaned and selected here and the anaylsis is demonstrated.

## Thesis
This is a collection of further analysis notebooks and plots. 

## Folder structure
```commandline
.
├── 01_data
│   ├── full_level3.csv
│   ├── level3.ipynb
│   ├── level3_featselected_500_nadropped.csv
│   ├── level_3_data
│   │   └── sub_level3.csv
│   └── level_5_data
│       └── 2016_04_01_a549_48hr_batch1_dmso_spherized_profiles_with_input_normalized_by_dmso_consensus_median.csv.gz
├── 02_analysis
│   ├── 01_data_insights.ipynb
│   ├── 02_clean_data.ipynb
│   ├── 03_enrichment_demo.ipynb
│   ├── 03_precision_demo.ipynb
│   ├── compare_consensus.ipynb
│   ├── examples_images.ipynb
│   └── level3_data_insights.ipynb
├── README.md
└── thesis
    ├── 00_baseline_calc.ipynb
    ├── 00_baselines_plots.ipynb
    ├── 0_PCA_visualizatino.ipynb
    ├── 0_example_hitk.ipynb
    ├── 0_precision_doof.ipynb
    ├── compare_metrics.ipynb
    ├── meta.csv
    └── subselection_performance.ipynb
```