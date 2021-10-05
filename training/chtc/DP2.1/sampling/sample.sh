echo "Hello CHTC from Job $1"

# this index is transfered from your submission server to the run server and is then moved to the relevant spot in your project folder.
mv 924_index.csv /local_group_storage/broad_data/michael/training/inputs/metadata/
mv config_sample.json /local_group_storage/broad_data/michael/training/inputs/config/

# Create a folder to put the crops in
mkdir /local_group_storage/broad_data/michael/training/outputs/1004_sample/

# cd to the position of DeepProfiler in the docker
cd /DeepProfiler
# run the sampling command
python3 deepprofiler --root=/local_group_storage/broad_data/michael/training/ --config=config_sample.json --metadata=924_index.csv --sample=1004_sample sample-sc

# output the number of files in the sample folder to make sure it was successful
cd /local_group_storage/broad_data/michael/training/outputs/1004_sample/
find . -type f | wc -l

echo "done"