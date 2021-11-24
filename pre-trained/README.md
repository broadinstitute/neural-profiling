# Achieving a Deep Learning Baseline with pretrained networks using DeepProfiler
Part 2 of the overall project, refer to the `/baseline` to read part 1  
Read the documentation of DeepProfiler (DP) to understand the following. 

## Folder structure
```commandline
.
├── README.md
├── ResNet50v2
│   ├── aggregated
│   │   ├── aggregate.ipynb
│   │   ├── aggregated_resnet_median.csv
│   │   ├── full_well_index.csv
│   │   ├── level3_resnet.csv
│   │   ├── raw.csv
│   │   └── testing_resnet_output.ipynb
│   └── post_processing
│       ├── Compare_eff_res_cp.ipynb
│       └── normalization.ipynb
├── data-prep
│   ├── 01_location_extraction
│   │   ├── README.md
│   │   ├── extract.py
│   │   ├── location_test.ipynb
│   │   └── split.py
│   └── 02_index_preperation
│       ├── 00_create_index.ipynb
│       ├── 01_enrich_index.ipynb
│       ├── 02_clean_index.ipynb
│       ├── README.md
│       ├── barcode_platemap.csv
│       ├── enriched_index.csv
│       ├── full_index.csv
│       ├── full_well_index.csv
│       ├── original_index.csv
│       ├── repurposing_info_external_moa_map_resolved.tsv
│       └── sub_index.csv
├── efficient_net
│   ├── aggregated
│   │   ├── README.md
│   │   ├── aggregated_efficientnet_median.csv
│   │   ├── run_aggregation.py
│   │   └── testing_efficientnet.ipynb
│   └── post_processing
│       ├── PCA_plots.ipynb
│       ├── consensus_spherized_dmso_eff_mean.csv
│       ├── efficientnet_full_analysis.ipynb
│       └── normalization.ipynb
└── thesis
    ├── 0_PCA_visualizatino.ipynb
    ├── 0_compare_arch.ipynb
    ├── 0_normalization.ipynb
    ├── batch_effect.ipynb
    ├── random_subsets.ipynb
    └── subselection_performance.ipynb
```
ResNet50v2 and efficient_net are the folders dealing with the profiles of both per-trained nets.
Thesis holds some high level analyses. 


## Getting the data
We decided to go with the locations calculated from CellProfiler first for closer comparison, but may later take the locations coming from a Unet masking or build our own CNN which takes in images instead of images and locations. 

The Unet locations can be found on DGX under `/dgx1nas1/cellpainting-datasets/2015_10_05_DrugRepurposing_AravindSubramanian_GolubLab_Broad/DP-project`

#### CellProfiler Metadata
The metadata from CellProfiler lives on S3 @ `s3://imaging-platform/projects/2015_10_05_DrugRepurposing_AravindSubramanian_GolubLab_Broad/workspace/backend/2016_04_01_a549_48hr_batch1/` 
The SQLite files hold a list of all cell locations + other metadata. 

I extracted the locations from these S3 files and moved them into the smaller csv files as is needed by DP. I set up a instance on EC2 with a large RAM memory (32 GB) and ran two scripts, one to extract the locations from the S3 files into a large csv file containing all locations for a plate, and the other to make smaller csv files (each referring to one site).
`extract.py` and `split.py` both make use of os.system() commands to pull and move files from S3.

WARNING. The location files don't have the same name as the images but rather they have a Well-Site-Nuclei nomenclatur.
I messed this up the first time and so `rename-s3.py` allows to rename all files on the s3 locations folder.

#### Locations data on S3
The locations files which will be used for DP are @ `s3://imaging-platform/projects/2015_10_05_DrugRepurposing_AravindSubramanian_GolubLab_Broad/workspace/deep_learning/locations/`. The `/full_csv/` folder contains the large csv files and is only there for backup. Only the plate files should be used for DP. 

#### Images
The images are taking from `s3://imaging-platform/projects/2015_10_05_DrugRepurposing_AravindSubramanian_GolubLab_Broad/2016_04_01_a549_48hr_batch1_compressed/images/`. These png are already compressed and (I think) this is means that the `prepare` function from DP is not very effective. 

### Config
The config file, listed as `config_pre_net.json` is a dummy file for a pretrained efficientnet network. TBD

