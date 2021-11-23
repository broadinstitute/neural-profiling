echo "Hello CHTC from Job $1"

# move config
mv config_sample.json /local_group_storage/broad_data/michael/training/inputs/config/

# Create a folder to put the crops in
mkdir /local_group_storage/broad_data/michael/training/outputs/1017_sc/

# cd to the position of DeepProfiler in the docker
cd /DeepProfiler
# run the sampling command
python3 deepprofiler --gpu=3 --root=/local_group_storage/broad_data/michael/training/ --config=config_sample.json --metadata=sub_index.csv --single-cells=1017_sc export-sc


# output the number of files in the sample folder to make sure it was successful
cd /local_group_storage/broad_data/michael/training/outputs/1017_sc/
find . -type f | wc -l

echo "done"