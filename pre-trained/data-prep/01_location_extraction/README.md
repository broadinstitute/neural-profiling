# Location extraction

1. Input for DeepProfiler includes the locations of all cell centers. These are extracted from SQlite files which are the output of CellProfiler. 
2. Using extract.py, I downloaded the SQlite files from S3 and extracted the list of cell locations into a large csv (`SQ00014812_locations.csv`). 
3. Next, all large csv files need to be split into smaller csv files, one for each image (ie for each field of view). This was accomplished with split.py. 
4. Finally, one has to take care that the names of all files are correct (in the future change the way split.py works) and one also needs to devide all values by 2 to fit the pixel size of the images (see example image).
5. `A01-1-Nuclei.csv` is an example output of this process. 
6. The resulting location files were uploaded to S3 (exact location in config file).