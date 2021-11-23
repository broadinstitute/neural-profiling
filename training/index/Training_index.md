# Indexes / subsets of data

Sub_index is the full LINCS subset with 1 dose and MOA classes > 1. 
All other indexes are subselections. 
Within this document the old and new index can be found. Beware that we now control the training data via the single cell metadata file (sc-metadata.csv).  
Ask Michael Bornholdt for details on these subselections and training experiments.
For all details of these index files in the old_index_maker.ipynb

## Old indexes

**sub_index**: full index

**top_moa**: 
- select top 50 moas  
- make rep 1 and site 1 to test
- well overlapping between train and test

**811_index**:
- select top 50 moas  
- delete all Compounds that do not have 5 replicates,  
- replica 1 & 2 are for test,  
- very large number of DMSO in test,  
- 512 compounds  

**812_index**:
- same as 811, 
- replica 1, site 1&2 for test 
- 92 DMSOs for test

**817_index**:
- make sure that each compound has both batches for training and the larger batch 2 sites for testing
- 45 DMSO's in test

**823_index**:
- choose bottom moas instead of top 50
- now have 510 compounds

**826_index**:
- do not subselect moas 
- 1018 compounds

**924_index**:
- high phenotype data 

## New indexes

Random subsection of 450 compounds:
- length of sc 1007: 456533
- Length of sc 1025:  911,042
- Length of sc 1026:  2,267,640

---

**Full subsection**: 18,239,862 cells

- sc_1017: 534,166. All compounds
- sc_1027: 578,103 all compounds. Basically like 926 with only batches 3-5
- sc_1028: 1 mil all compounds. Basically like 1027 with more cells


# Runs
This is important! it tells you which 

- 727 / 805 were nan runs 
- 806_1: top_moa. 10 Epochs / 0.005 LR cosine / 64 batch
- 806_2: top_moa. 5 Epochs / 0.005 LR cosine / 64 batch
- 811: 812_index. 10 Epochs / 0.005 LR cosine / 64 batch
- 813: 812_index. 24 Epochs / 0.005 LR cosine / 64 batch
- 819: 817_index. 10 Epochs / 0.005 LR cosine / 64 batch
- 822: 817_index (resnet). 10 Epochs / 0.005 LR cosine / 64 batch
- 825: 823_index. 20 Epochs / 0.005 LR cosine / 256 batch
- 826_2: 817_index (with augmentation). 10 Epochs / 0.005 LR cosine / 256 batch
- 827: 817_index. 25 Epochs  / 0.005 LR cosine / 256 batch 
- 831: 826_index. 20 epochs / 0.005 LR cosine / 256 batch
- 901: 826_index. (with augmentation) 10 Epochs / 0.005 LR cosine / 256 batch
- 902: on top of 813. 26 Epochs  / 0.005 LR cosine / 256 batch
- 903: 812_index (with augmentation) 25 E / 0.005 LR cosine / 256 batch
- 910: 812_index 30 E / 0.005 LR cosine / 256 batch
- 913: 812_index flat LR. 30E / 256 batch
- 914: 812_index flat LR. with augmentation / 256 batch
- 915: LR flat Index 812. 20E / REsnet!  / 0.005 LR cosine / 256 batch
- 916: LR flat Index 812. 20E / efficiennet  / 0.02 LR cosine / 256 batch
- 917: Cosine.005 / index 817 / 20E / batch size 256
- 918: Cosine.005 / index 817 / 20E / batch size 64
- 919: Cosing 005 / index 817/ sample 915 / 20E / BS 256 
- 920 cosine 0.005 / index 826 / 10 out of 25E / batch size 64
- 921 cosine 0 .002 / index 826 / 25E / batch size 64
- 922 / cosine 005 / 25 E/ 826 index / BS 64
- 923 / cosine 005 / 25 E/ 826 index / BS 256??
- 925 / Cosine.005 / index 817 / 20E / batch size 32
- 926 / cosine 005 index and sample 924 / 20E / BS64
- 927 / Cosine .02 / index 817 / 20E / batch size 256
- 928 / Cosine.01 / index 817 / 20E / batch size 256
- 929 / Cosine.002 / index 817 / 20E / batch size 256
- 931 / on top of 930 / flat 0.002 / start with epoch 12
- 1003 / flat 0.01 index 817 . 20E . BS 256 - random initalization!

1007_sample: 
- 1007 / on 1007 sample / 20 E / 0.01 LR / Aug off / smooth off /
- 1008 / 1007 sample / 30 E / 0.02 LR cosine / Aug off / smooth off / 256 batch
- 1009 / 1007 sample / 30 E / 0.02 LR cosine / Aug off / smooth 0.2 / 256 batch
- 1010 / 1007 sample / 30 E / 0.02 LR cosine / Aug true / smooth 0.0 / 256 batch
- 1011 / 1007 sample / 30 E / 0.02 LR cosine / Aug true / smooth 0.2 / 256 batch
- 1012 / 1007 sample / 30 E / 0.02 LR cosine / Aug off / smooth 0.1 / 256 batch
- 1013 / 1007 sample / 25 E / 0.01 LR cosine / 64 batch / Aug off / smooth 0.05 /
- 1014 / Resnet like 1008 / 1007 sample / 30 E / 0.2 LR cosine / Aug off / smooth off / 256 batch
- 1015 / 1007 sample / 30 E / 0.2 LR cosine / Aug off / smooth 0.3 / 256 batch
- 1016 / 1007 sample / 30 E / 0.2 LR cosine / Aug off / smooth 0.05 / 256 batch
- 1018 / 1007 sample / 30 E / 0.2 LR cosine / Aug off / smooth 0.00 / 64 batch / Random init
- 1019 / 1007 sample - 1025 index / 30 E / .02 LR cosine / Aug off / smooth 0.00 / 256 batch
- 1020 / 1007 sample - 1026 index / 30 E / .02 LR cosine / Aug off / smooth 0.00 / 256 batch
- 1021 / 1007 index /  30 E / .02 LR cosine / Aug off / smooth 0.00 / 64 batch
- 1022 / 1007 sample / 30 E / 0.2 LR flat / Aug off / smooth off / 256 batch
- 1023 /  1007 index / 30 E / 0.02 cosine / Aug on / smooth 0.1 / 64 batch
- 1024 / 1017 sample 1017 index / 30 E / 0.2 LR cosine / Aug off / smooth off / 64 batch
- 1025 / 1017 sample 1017 index / 30 E / 0.2 LR cosine / Aug on / smooth 0.1 / 64 batch
- 1026 / 1017 sample 1027 index / 30 E / 0.2 LR cosine / Aug on / smooth 0.1 / 64 batch/ compare to 1025
- 1027 / 1017 sample 1028 index / 20 E / 0.4 LR cosine / Aug on / smooth 0.1 / 64 batch/
- 1028 / 1017 sample 1017 index / 30 E / 0.4 LR cosine / Aug on / smooth 0.1 / 64 batch 
- 1029 / 1007 sample / 30 E / 0.02 LR cosine / Aug off / smooth 0.08 / 256 batch
- 1101 / 1007 index /  30 E / .02 LR cosine / Aug off / smooth 0.00 / 32 batch - high? 
- 1102 / 1007 sample- 1026 index / 30 E / .02 LR cosine / Aug off / smooth 0.00 / 32 batch
- 1103 / 1017 sample 1017 index / 30 E / lr / Aug off / smooth 0.0 / 32 batch
  - LR 0.02: “epoch”:[10,20,25], “lr”:[0.01, 0.005, 0.002]}
- 1104 / 1017 sample 1017 index / 30 E / lr / Aug on / smooth 0.0 / 32 batch
- 1105 / 1017 sample 1017 index / 30 E / 0.4 LR cosine / Aug on / smooth 0.0 / 64 batch - compare wth 1028
- 1107 / index 1028 / 30 E / 0.02 LR cosine / Aug on / smooth 0.08 / 32 batch

# Experiments
First number is the CHTC run ID. If you log onto my server, you can find the logs for that experiment. 


14256290 profile again 811 cause I did too small in the beginning

14256304 use 811 to extract classes

14256319 use 811 to extract classes. v2
Then 14256323 (edited) 


14256343 aggregate 811_2


14256345.0 811 to extract classes. v4


14256497 aggregate the class 811


14256512 sample 817 (edited) 


14256782 817 sample first train


14256954.0 813 profile - to test how training long effects the scores. (edited) 


14256984.0 819 sampling


14257078.0 813 aggregate


14257081 resnet train


14257276 profile 822 (resnet)


14257365 sample 823 (edited) 


14257363 aggregate 822 (resbet)


14257376 819 class profile

## 8/25

14257480 Delete zeros for sample_23 

14257514  Train_825. Sample_23 - new index with lower moas

14257515.0 train_826 sample 17 index 17. New training with augmentation! stopped

14257516 train_827. Sample_17, index_17 - long run to compare with short runs. stopped

## 8/26 

14257750 train_826_2 sample 17 index 17. New training with augmentation!  

14257752 train_827. Sample_17, index_17 - long run to compare with short runs. 

14257756.0 sample all data at 0.3. 826_sample stopped 


14257820 sample_825_20 profile 825_train 
## 8/30 

14257865 aggregate 825_20_profile

14257875 profile 826_2 . aggregate with 14258043

14257870 profile 827_2 epoch 8. aggregate with 14260920

14257873 profile 827_2 epoch 16. aggregate with 14258045

14257874 profile 827_2 epoch 25 aggregate with 14258046

14258042 make sample_826 sample all data at 0.25

## 8/31

14260148 check zero 826 

14260952 train_31 on sample 826. 20 epochs

## 9/02 

14265280.0 10 epochs with 826 data and augmentation. train 901

14265279 DO 26 epochs on top of 813 since its the best so far. train 902

14265282.0 train_903. With augm. RUn on 811 

## 9/07

14279039.0 Profile 901 - 14279111 for aggregation

14279037.0 Profile 902 - 14279112.0 aggregate

14279040.0 Profile 903 - 14279114.0 aggregate

## 9/10

14280063.0 Profile 831. I had forgoten that somehow

14280067.0 train 910. Train on index 812 since that was the best. 

# 9/13 

14281400.0 Aggregate 831 

14281422.0  Profile E30 from 910 

14281423 Train 913. LR = 0.005 flat. Index 812

14281425 Train 914. LR = 0.005 flat. Index 812. With Augmentation

# 9 /14

14282122 Aggregate 910 

14282129 Train 915. LR = 0.005 flat. Index 812. REsnet!

14282130.0 Train 916. LR = 0.005 flat. Index 812. efficiennet

14282172 Profile 913 0005E . / 14282954 for aggregation

14282174.0 Profile 913 0015E / 14282956 for aggregation  

# 9/15

14282410.0 sample 915. ON index 817. sample_rate: 0.1

14282892 zero crops 915

14282895 Profile 913 - 0015E - didnt happen 

14282897 Train 917. Cosine.005 / index 817 / 20E / batch size 256

14282951 Train 918. Cosine.005 / index 817 / 20E / batch size 64

14282952 Train 919. Cosing 005 / index 817/ sample 915 / 20E / BS 256

14282962 Profile 913 0030 E . Aggregate with 14283306.0 

14282997 Profile 914 22. - Failed

14283002 Profile 915 25E. - Failed 

14283004 Profile 916 25E. Aggreagte with 14283308.0

# 9/20
14283439 Profile 917 20E. agg with 14283521.0

14283303 Profile 919 20E. agg with 

14283304 Profile 918 20E. agg with 14283522

14283305 Profile 914 22E. agg with 14283434

14283440 Profile 915 25E. - failed again

14283441 Train 920 cosine 0.005 / index 826 / 25E / batch size 64

14283442 Train 921 cosine 0.002 / index 826 / 25E / batch size 64

# 9 /21

14283628 Train 922 / cosine 005 / 25 E/ 826 index / BS 64

# 9 /22

14283843 sample index 826 with 0.1 onto 922_sample 

14283862.0 test run. Same as train22 i think with BS 256

14284039 profile 920 

14284040 profile 921

14284042 Train 924. Cosine.005 / index 817 / 20E / batch size 128

14284043 Train 925. Cosine.005 / index 817 / 20E / batch size 32

14284055 Sample 924 with factor 1. Top phenotype. 

# 9 / 27 

14285972 profile 920 . agg with 14286053

14285973 Aggregate 921  

14285975 profile 922 agg 14286055

14285976 profile 923 agg 14286056

14285977 profile 925

14286054.0 train_26 cosine 005 index and sample 924 / 20E / BS64

14286058 train 27 / Cosine.02 / index 817 / 20E / batch size 256

# 9 / 29 

14289118 train 28 / Cosine.01 / index 817 / 20E / batch size 256

14289119 train 29 / Cosine.002 / index 817 / 20E / batch size 256

14289120 profile 26 

14289284 train30 / flat 0.01 / index sample 826 / 20E BS 256 / hoping to train again. 

14289364 profile 27. 14289696 aggregate

# 10 / 4

14289705 profile 28

14289698.0 profile 29

14289731 train931 / on top of 930 / flat 0.002 / start with epoch 12

14289730 train 1003 / flat 0.01 index 817 . 20E . BS 256 - random initalization! 

# 10 /5 

14294916 Aggregate 928 
14294095 agg 929 

14294304 first try of v14/ train1004 / flat 0.01 / 826 / 256 / 20 E 

14294917 sample 924 onto 1004 with v15. 

# 10 / 6 

14304211 Profile 930. 11E, to compare to 931 profile

14304212 Profile 931

14307077.0 new sampline!!! 1007 sample 

# 10 / 17 

14357361 train 1007 / on 1007 sample / 20 E / 0.1 LR / Aug off / smooth off / 

14357427.0 sampling on sub_index

14357455 train 1008 / 1007 sample / 30 E / 0.2 LR cosine / Aug off / smooth off / 256 batch 

14357456 train 1009 / 1007 sample / 30 E / 0.2 LR cosine / Aug off / smooth 0.2 / 256 batch

14357458  1010 / 1007 sample / 30 E / 0.2 LR cosine / Aug true / smooth 0.0 / 256 batch

14357459 1011 / 1007 sample / 30 E / 0.2 LR cosine / Aug true / smooth 0.2 / 256 batch

14357558 1012 / 1007 sample / 30 E / 0.2 LR cosine / Aug off / smooth 0.1 / 256 batch

14357609 profile 1008 / agg with 14357756

14357738 profile 1009 / 14357833 agg

14357740 profile 1010 / 14357840 agg

14357743 profile 1011 / 14357840

14357753 1013 / 1007 sample / 25 E / 0.1 LR cosine / 64 batch / Aug off / smooth 0.05 /

14357754 profile 1012 / 14357848 agg

14357780 profile 1003 - nope

14357789 profile 1007 

14357793 train 1014 / Resnet like 1008 / 1007 sample / 30 E / 0.2 LR cosine / Aug off / smooth off / 256 batch

# 10 / 22 

14357835 profile 1013 / 14357857
14357836 profile 1014 / 14357865

14357842 train 1015 / 1007 sample / 30 E / 0.2 LR cosine / Aug off / smooth 0.3 / 256 batch

14357843 train 1016 / 1007 sample / 30 E / 0.2 LR cosine / Aug off / smooth 0.05 / 256 batch

failed. 14357866 train 1017 / 1007 sample / 30 E / 0.2 LR cosine / Aug off / smooth 0.00 / 256 batch / Random init

14357867 train 1018 / 1007 sample / 30 E / 0.2 LR cosine / Aug off / smooth 0.00 / 64 batch / Random init

# 10 / 23

14359685 profile 16 / agg 14361019
14359670 profile 18

# 10 / 25 

14361017 profile 15 

# 10 / 26 

14362026 train 1019 / 1007 sample - 1025 index / 30 E / .02 LR cosine / Aug off / smooth 0.00 / 256 batch

14362140 train 1020 / 1007 sample - 1026 index / 30 E / .02 LR cosine / Aug off / smooth 0.00 / 256 batch 

14362230 train 1021 /1007 sample - 1007 index /  30 E / .02 LR cosine / Aug off / smooth 0.00 / 64 batch

14362234 1022 /  / 1007 sample / 30 E / 0.02 LR flat / Aug off / smooth off / 256 batch

14362610 1023 /  1007 index / 30 E / 0.02 cosine / Aug on / smooth 0.1 / 64 batch

# 10 / 27

14362611.0 profile 1019 / agg 14363670

14362621 profile 1021 / agg 14363671

14363712 train 1024 / 1017 sample 1017 index / 30 E / 0.2 LR cosine / Aug off / smooth off / 64 batch

14363743 1025 / 1017 sample 1017 index / 30 E / 0.2 LR cosine / Aug on / smooth 0.1 / 64 batch

# 10 / 28 



14364024 profile 1020 / 14364999 agg 1020 

14364025 profile 1022 /14364828 agg 1022

14364514 profile 1023 / add 14366190

14364899 profile 1024 / 14367390 agg

14365980 profiles 1025 / 14367407 agg

14367389 1026 / 1017 sample 1027 index / 30 E / 0.2 LR cosine / Aug on / smooth 0.1 / 64 batch/ compare to 1025

14366298 1027 / 1017 sample 1028 index / 20 E / 0.4 LR cosine / Aug on / smooth 0.1 / 64 batch/ 

# 10 / 29

14367630 profile 1014 / aggg 14368048

14367639 1028 / 1017 sample 1017 index / 30 E / 0.4 LR cosine / Aug on / smooth 0.1 / 64 batch 


# 10 /21 

14368049 profile 1028 / agg 14373067

14373068 profile 1027 / 14373143

14373081 profile 1026 / agg 14373137

14368053 1029 / 1007 sample / 30 E / 0.02 LR cosine / Aug off / smooth 0.08 / 256 batch 

# 11 / 1

14373093 profile 1029 / agg 14374240

14373122 / 1101 / 1007 index /  30 E / .02 LR cosine / Aug off / smooth 0.00 / 32 batch - high? 

14373154 // 1102 / 1007 sample- 1026 index /  30 E / .02 LR cosine / Aug off / smooth 0.00 / 32 batch 

LR 0.02: “epoch”:[10,20,25], “lr”:[0.01, 0.005, 0.002]}
14374653 / 1103 / 1017 sample 1017 index / 30 E / lr / Aug off / smooth 0.0 / 32 batch

14374814 1104 / 1017 sample 1017 index / 30 E / lr / Aug on / smooth 0.0 / 32 batch

# 11 / 2 

14379459 profile 1101 / agg 14382886

14383158 profile 1103 / agg 14389252

14383844 1105 / 1017 sample 1017 index / 30 E / 0.4 LR cosine / Aug on / smooth 0.0 / 64 batch - compare wth 10828

14389258 profile 1004 / agg 14392019

14389271 1106  / 1017 sample 1017 index / 30 E / 0.4 LR cosine / Aug on / smooth 0.1 / 64 batch

# 11 / 4

14397811 profile 1105 / agg 14402044

14399244 profile 1106 / agg 14404312

14399275 profile 1102 E26 / agg 14404315

14404329 profile 1102 E20

Run on 1027 index. 

# 11 /8

- train 1107 / index 1028 / 30 E / 0.02 LR cosine / Aug on / smooth 0.08 / 32 batch

- 14437822 train 1108 . / 1007 index / 30 E / 0.2 LR cosine / Aug on / smooth 0. / 64 batch - compare to 1021

- 14438198 train 1109 . / 1007 index / 30 E / 0.2 LR cosine / Aug off / smooth 0.1 / 64 batch - compare to 1021
  
- 14441553 profile 1107 / agg 14446085

14446086 profile 1102 new  / agg 14446173

14446177 train 1110 / continueing 1027 / 1028 index / 40E start at 20/ 0.04 Lr/ Aug on / smooth 0.1

14447027 profile 1109
