# Working on the CHTC Server 

This README gives a practical guide to working on the Wiscon Center for High Throughput Computing (CHTC). 
Depending on which version of Deepprofiler you are using, the commands may differ marginaly. 

I am currently writing this guide for the `0.3.0` version of DP on the 20th of November 2021. 
All files used in the CHTC can be found in the DP_0.3.0 folder. 
The old_DP folder contains old versions of these files. 

While surely not perfect, my setup on CHTC submission server served me well and I will thus present the contents of each folder in the relevant subsection. 
For further reference, here is the relevant structure of the [Docker](https://hub.docker.com/r/michaelbornholdt/deep_profiler/tags?page=1&ordering=last_updated) on the CHTC run server.  
```
.
+-- DeepProfiler
|   +-- deepprofiler
|   +-- plugins
etc.
+-- local_group_storage/broad_data/michael/
|   +-- training
|   |   +-- inputs
|   |   +-- outputs
|   |   |   +-- sample_xx
|   |   |   +-- train_xx
|   |   |   +-- profile_xx
|   +-- log_xx.txt
```

Here are some basic resources from CHTC and Condor: 
- [CHTC Website](https://chtc.cs.wisc.edu/)
- [CHTC Email](chtc@cs.wisc.edu)
- [Connecting to CHTC](https://chtc.cs.wisc.edu/uw-research-computing/connecting)
- [Introduction and Hello World](https://chtc.cs.wisc.edu/uw-research-computing/helloworld)
- [HPC overview](https://chtc.cs.wisc.edu/uw-research-computing/hpc-overview)
- [How to run a docker](https://chtc.cs.wisc.edu/uw-research-computing/docker-jobs#1-choose-or-create-a-docker-container-image)
- [HTcondor manual front page](https://htcondor.readthedocs.io/)
- [How to use file transfer](https://htcondor.readthedocs.io/en/latest/users-manual/file-transfer.html?highlight=S3#specifying-what-files-to-transfer)

Here are your most important condor commands and files:
- file.sub: submission files holding information on server, files transfers and resources
- file.sh: executable file; runs commands. 
- [condor_q](https://htcondor.readthedocs.io/en/latest/man-pages/condor_q.html): list all running clusters
- [condor_submit](https://htcondor.readthedocs.io/en/latest/man-pages/condor_submit.html): submit a job
- [condor_ssh_to_job](https://htcondor.readthedocs.io/en/latest/man-pages/condor_ssh_to_job.html): access the running server and manipulate / read files
- [condor_tail](https://htcondor.readthedocs.io/en/latest/man-pages/condor_tail.html): Display the last contents of a running job’s standard output or file

# Pipeline

The normal pipeline for this project was the following
1. Export all single cells with the `export-sc` command. (This has been done already: `/outputs/1017_sc/`)
2. Decide on a subsection data to train on. That can be only part of all classes or all classes but sampled at a smaller fraction. Change the `split` columns of the metadata file to determine which cells go in training, testing and unused - according to your subselection. 
3. Make sure all crops are valid (check for zero images)
4. Train a model 
5. Profile / infer the profiles
6. Aggregate 
7. Move to cytominer-eval 


## 1. Exporting single cells

The sampling folder on the submit server will typically look like this
```
.
+-- exporting
|   +-- export.sh
|   +-- export.sub
|   +-- config_export.json
|   +-- 924_index.csv
|   +-- XXXXXXXX.log 
|   +-- XXXXXXXX.err
|   +-- XXXXXXXX.out
```

### export.sub

The first few lines of all submission files are the same.
```bash
universe = docker
docker_image = michaelbornholdt/deep_profiler:tf2_2.0
```
This defines which docker will be mounted. [Be careful!]() Never build a docker file with the same name as an old one. 
CHTC will not pull the new docker if it knows the name but use a cached version.  

```bash
accounting_group = COBA
requirements = (Machine == "coba2000.chtc.wisc.edu")
```
These lines simply define which server to run on. Never change these.
```commandline
executable = sample.sh
transfer_executable = true
arguments = $(Cluster)
```
Here you define your executable files and input arguments. 

```commandline
+LongJob = true
```
This is crucial so your exporting can run longer than 72 hours. 18 Million cells took around a week.

```commandline
output = $(Cluster).out
error = $(Cluster).err
log = $(Cluster).log
```
Finally your output files are named. These are just useful conventions that can be changed.

### export.sh

The main command from [sample.sh](DP2.1/sampling/sample.sh) is 
```
python3 deepprofiler --gpu=3 --root=/local_group_storage/broad_data/michael/training/ --config=config_sample.json --metadata=sub_index.csv --single-cells=1017_sc export-sc
```
Note that `/local_group_storage/broad_data/michael/training/` is my project folder in the CHTC structure and `--single-cells=1017_sc` determines the folder in which the crops will be placed.

Also note that the first lines of sample.sh move the input file `config_sample.json` into the correct position in the DeepProfiler structure.
This method will be used in all other bash files.

### config_export.json

In the [config_export.json](DP_0.3.0/exporting/config_export.json), only the following lines are relevant.
```json
 "sampling": {
            "factor": 1,
            "workers": 16,
            "cache_size": 40000
            }
```
The factor number defines the fraction of cells cropped in each site. 

## 2. Manipulate metadata file.

The creation of old training indexes can be traced in the `old_index_maker` notebook in the `train/index` folder. 
All sites will be allocated for either training, validation or unused in the 'Split' column of the index.csv.
Index file example: [826_index.csv](../index/826_index.csv)

The new way with 0.3.0 is to manipulate the sc-metadata.csv file that is created during exporting. Again, the `split` column will determine how these cells will be used during training. 
The `helper_functions/sc-metadata.py` gives an example on how to manipulate this file (also see `/training/index`). 

## 3. Validating crops

Unfortunately, the crops created in the prior step can have errors. 
This may be the case due to locations files or the sampling command having errors.
Nonetheless, some crops are totally black (all values are zero) and this creates an error during the training process. 
Furthermore, some files can go lost when transfering large numbers of files for example.
The two helper functions `check_crops.py` and `zero_crops.py` find missing files and black crops. 

Both python files live at the `/local_group_storage/broad_data/michael/training/outputs` location.
Additionally, both functions output a `missing_crops.csv` file which can be read on the submission server.

If you did not move the files after sampling, there is no need for running check_crops. 
However, there is always a need to run `zero_crops.py`. 
Running this function should take around 20 - 60 mins. 


## 4. Train

Your train folder may look like this
```
+-- sampling
|   +-- train.sub
|   +-- train.sh
|   +-- config_train.json
|   +-- log_XXXXXXXX
|   +-- err_XXXXXXXX
|   +-- out_XXXXXXXX
```
### train.sh

The [train.sh](DP_0.3.0/train/train.sh) file moves the config to the correct location and then outputs the config for documentation. 

You then define the name of the experiment (I used numbers that refered to dates) and then run the training with the following command:
```commandline
python3 deepprofiler --gpu=0 --metadata=826_index.csv --exp=${NR}_train --single-cells=1017_sc  --root=/local_group_storage/broad_data/michael/training --config=config_train.json train --epoch 1 2>&1 | tee /local_group_storage/broad_data/michael/log_${NR}_train.txt
```
Make sure that you are training on an unused gpu (you can check with nvidia-smi beforehand) and make sure that you are using the right sample folder. 
You can also change the epoch value if you want to train on top of a already trained model. 
The final part of the command send all std_out and std_err to the log file. 

### config_train.json

```json
 "model": {
            "name": "efficientnet",
            "augmentations": false,
            "crop_generator": "sampled_crop_generator",
            "metrics": ["accuracy", "top_k"],
            "epochs": 20,
            "initialization":"ImageNet",
            "params": {
                "learning_rate": 0.02,
                "batch_size": 256,
                "conv_blocks": 0,
                "label_smoothing": 0.0,
                "feature_dim": 256,
                "pooling": "avg"
            },
            "lr_schedule": "cosine"
```
Relevant parameters are augmentation, epochs, learning_rate, batch_size and label_smoothing.
Details on these can be found in the [DeepProfiler documentation](https://github.com/cytomining/DeepProfiler/wiki).

For Resnet use: 
```json
"name": "resnet",
"conv_blocks": 50,
```


## 5. Profile


### profile.sh
```
cp 928_train/checkpoint/checkpoint_0020.hdf5 ${NR}_profile/checkpoint/
```
Beware the model from which we are profiling needs to be manually set each time.
The experiment and the epoch number must be correct and in accordance with the config file.

```commandline
python3 deepprofiler --gpu=0 --root=/local_group_storage/broad_data/michael/training --config=config_profile.json --metadata=sub_index.csv --exp=${NR}_profile profile
```
Apart from checking that the GPU is unused, the profile command does not need to be changed. 

If you want to get the class predictions instead of the profiles, you need to simply change the output layer in the config: 

```json
  "profile": {
      "feature_layer": "Compound",
      "checkpoint": "checkpoint_0020.hdf5",
      "batch_size": 512
    }
}
```

If you want to use the pre-trained models to infer features, then use:
```json
  "profile": {
      "feature_layer": "pool5",
      "checkpoint": "None",
      "batch_size": 512
    }
}
```


## 6. Aggregate

Perform the `run_aggregation.py` after profiling and download the aggregated csv to the submission server. 

Note that the experiment numbers in `aggregate.sub` and in `run_aggregation.py` must be adapted before each submission: 
```bash
# in aggregate.sub
transfer_output_files = /local_group_storage/broad_data/michael/928_aggregated_median.csv
# in run aggregation
experiment = '928_profile'
# and
df_well.to_csv('/local_group_storage/broad_data/michael/928_aggregated_median.csv')
```


## 7. Move to cytoeminer-val

Simply use the following command and your CHTC password to move files from the submission server to your personal PC for downstream processing.

```commandline
scp username@submit-1.chtc.wisc.edu:/home/username/aggregate/XXX_aggregated_median.csv /target/location 
```