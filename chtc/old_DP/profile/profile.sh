echo "Hello CHTC from Job $1"

mv config_profile.json /local_group_storage/broad_data/michael/training/inputs/config/

cat /local_group_storage/broad_data/michael/training/inputs/config/config_profile.json

cd /local_group_storage/broad_data/michael/training/outputs/

# experiment number
NR=928

mkdir -p ${NR}_profile/checkpoint/
# the model needs to be manually adapted
cp 928_train/checkpoint/checkpoint_0020.hdf5 ${NR}_profile/checkpoint/

cd /DeepProfiler
python3 deepprofiler --gpu=0 --root=/local_group_storage/broad_data/michael/training --config=config_profile.json --metadata=sub_index.csv --exp=${NR}_profile profile


cd /local_group_storage/broad_data/michael/training/outputs/${NR}_profile/features
find . -type f | wc


echo "We are done! $1"
