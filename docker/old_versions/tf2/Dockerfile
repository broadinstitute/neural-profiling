FROM tensorflow/tensorflow:2.5.0-gpu

RUN /usr/bin/python3 -m pip install --upgrade pip
RUN apt-get update
RUN apt update
RUN apt install wget
RUN apt-get -y install nano
RUN apt install -y tmux
RUN apt install -y htop
RUN apt install -y git

# install open cv
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt install libgl1-mesa-glx -y
RUN pip install opencv-python

# install DeepProfiler
# RUN rm -rf local_group_storage/broad_data/michael/DeepProfiler
RUN curl -L https://github.com/cytomining/deepprofiler/zipball/tf2/ > download.zip
RUN unzip download.zip
RUN mv cytomining-DeepProfiler-678cfb1 DeepProfiler
# curl -L https://github.com/cytomining/pycytominer/zipball/update_agg_TF2 > download.zip
# cytomining-pycytominer-72aa116
# RUN mkdir -p local_group_storage/broad_data/michael
# RUN mv DeepProfiler_2/ local_group_storage/broad_data/michael/DeepProfiler_2/
# WORKDIR local_group_storage/broad_data/michael/DeepProfiler_2
WORKDIR DeepProfiler
RUN pip install -e .
RUN pip install tqdm

# download models
RUN wget https://storage.googleapis.com/keras-applications/efficientnetb0_notop.h5
RUN mkdir -p ~/.keras/models
RUN cp efficientnetb0_notop.h5 ~/.keras/models
RUN mkdir -p /.keras/models
RUN cp efficientnetb0_notop.h5 /.keras/models

# install Pycytominer
RUN pip install git+git://github.com/cytomining/pycytominer

