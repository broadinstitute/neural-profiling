# import tensorflow GPU docker image
FROM tensorflow/tensorflow:2.5.1-gpu

# update installing scripts
RUN /usr/bin/python3 -m pip install --upgrade pip
RUN apt-get update
RUN apt update

# install usefull tools
RUN apt-get -y install nano
RUN apt install -y tmux
RUN apt install -y htop
RUN apt install -y git

# install open cv
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt install libgl1-mesa-glx -y
RUN pip install opencv-python

# install DeepProfiler
RUN git clone https://github.com/cytomining/DeepProfiler.git
WORKDIR DeepProfiler
RUN pip install -e .

# install Pycytominer and eval
RUN pip install git+git://github.com/cytomining/pycytominer
# pip install git+https://github.com/cytomining/pycytominer.git@update_agg_TF2
RUN pip install cytominer-eval



