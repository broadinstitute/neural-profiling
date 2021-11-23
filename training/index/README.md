# Indexes
Indexes determine the training and testing split in your DP experiments. 
In the versions before DP 0.3.0, the index file living in `/inputs/metadata` would determine this split.
Now, the single cell metadata file (sc-metadata) tells the models which cell belongs to train, test and unused.

Old Indexes were created in  `old_index_maker.ipynb` and the new ones in  `sc-metadata/train_test_split.ipynb`. 
The new indexes are named `sc_XXXX.csc` 

# Logging experiments

`Train_index_file.md` is the most impportant file in this folder. 
It contains the details of each training run and all index files. 
