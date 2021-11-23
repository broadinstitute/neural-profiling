export AWS_ACCESS_KEY_ID=XXXX

export AWS_SECRET_ACCESS_KEY=xxxx

export AWS_DEFAULT_REGION=us-east-1

cd /local_group_storage/broad_data/michael/training/

aws s3 sync folder/ s3://jump-cellpainting/projects/2015_10_05_DrugRepurposing_AravindSubramanian_GolubLab_Broad/workspace/deep_learning/folder/
