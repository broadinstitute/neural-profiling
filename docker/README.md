# DeepProfiler Dockers

This [Docker repository](https://hub.docker.com/repository/docker/michaelbornholdt/deep_profiler) includes all docker images you need to run DP on your server.
The most recent tag stable tag is tf2_2.0. 
It runs on the Docker file found in the 0.3.0 folder (the nomenclature refers to the 0.3.0 version of DeepProfiler).

```commandline
# RUN pip install git+git://github.com/cytomining/pycytominer
# RUN pip install git+https://github.com/cytomining/pycytominer.git@update_agg_TF2
```
These two lines depend on whether pycytominer.DeepProfiler_Aggregate has been adapted to the new structure.

In the future, the docker files could additionally contain example files and folder structures.


### Legacy 

Until October 2021 DP was run on Tensorflow 1.5. 
Some older Docker images thus on TF 1.5. 