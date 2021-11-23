echo "start training on $1"

mv config_train.json /local_group_storage/broad_data/michael/training/inputs/config/config_train.json
cd ~/DeepProfiler

echo "-------------"

cat /local_group_storage/broad_data/michael/training/inputs/config/config_train.json

echo "-------------"

# Name of the experiment
NR=1004

mkdir /local_group_storage/broad_data/michael/training/outputs/${NR}_train/
python3 deepprofiler --gpu=0 --metadata=sc_1027.csv --exp=${NR}_train --single-cells=1017_sc --root=/local_group_storage/broad_data/michael/training --config=config_train.json train --epoch 1 2>&1 | tee /local_group_storage/broad_data/michael/log_${NR}_train.txt


echo "-------------"

echo "finished training $1"
