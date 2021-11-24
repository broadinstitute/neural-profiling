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


## Important random things
- Some information in this repository may be old since the DeepProfiler versions changed midway through the project
- The single cell crops of all 18 million cells within the LINCS subsection can be found on S3: `s3://jump-cellpainting/projects/2015_10_05_DrugRepurposing_AravindSubramanian_GolubLab_Broad/workspace/deep_learning/outputs/1017_sc/`
- If you can't reach Michael Bornholdt, try to reach Shantanu Singh. 


## Experimental data on S3

- Compressed LINCS images:  
`s3://jump-cellpainting/projects/2015_10_05_DrugRepurposing_AravindSubramanian_GolubLab_Broad/2016_04_01_a549_48hr_batch1_compressed/images/` 
- Backup large csv files: `s3://jump-cellpainting/projects/2015_10_05_DrugRepurposing_AravindSubramanian_GolubLab_Broad/workspace/location_backups/`
- Location files: `s3://jump-cellpainting/projects/2015_10_05_DrugRepurposing_AravindSubramanian_GolubLab_Broad/workspace/deep_learning/inputs/locations/`
- LINCS sub index: `s3://jump-cellpainting/projects/2015_10_05_DrugRepurposing_AravindSubramanian_GolubLab_Broad/workspace/deep_learning/inputs/metadata/sub_index.csv`
- full enriched index: `s3://jump-cellpainting/projects/2015_10_05_DrugRepurposing_AravindSubramanian_GolubLab_Broad/workspace/deep_learning/inputs/metadata/enriched_index.csv`
- logs of experiments: `s3://jump-cellpainting/projects/2015_10_05_DrugRepurposing_AravindSubramanian_GolubLab_Broad/workspace/deep_learning/logs/`
- models: `s3://jump-cellpainting/projects/2015_10_05_DrugRepurposing_AravindSubramanian_GolubLab_Broad/workspace/deep_learning/models/`
- LINCS subsets crop (18 million): `s3://jump-cellpainting/projects/2015_10_05_DrugRepurposing_AravindSubramanian_GolubLab_Broad/workspace/deep_learning/crops/`

