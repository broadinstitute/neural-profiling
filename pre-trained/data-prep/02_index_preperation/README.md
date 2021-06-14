# Index Preparation

The index files is the central files for DP. Enriching it with the right Metadata is crucial for the analysis later on. 

1. I took the index.csv which already existed on the DGX.
2. enrich_index.ipynb then uses other metadata to enrich and prepare for DP.
3. In `clean_index.ipynb` I select a subsection of the data. Very similar to `baseline/02_clean_data`
4. `sub_index.csv` can then be applied to DP.

original_index: `/dgx1nas1/cellpainting-datasets/2015_10_05_DrugRepurposing_AravindSubramanian_GolubLab_Broad/DP-project/inputs/metadata/index.csv`