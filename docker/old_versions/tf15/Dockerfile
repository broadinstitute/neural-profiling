# FROM tensorflow/tensorflow:1.15.5-gpu
FROM tensorflow/tensorflow:2.5.0-gpu

RUN /usr/bin/python3 -m pip install --upgrade pip
RUN apt-get update
RUN apt install wget
RUN apt install curl
RUN apt-get -y install nano
RUN apt install -y tmux
RUN apt install -y htop


# install DeepProfiler
# RUN wget https://github.com/cytomining/DeepProfiler/archive/refs/heads/master.zip
# RUN wget https://github.com/cytomining/DeepProfiler/archive/refs/heads/tf2.zip
RUN curl -L https://github.com/cytomining/deepprofiler/zipball/tf2/ > test.tar
# RUN unzip master.zip
RUN unzip tf2.zip
RUN mkdir -p local_group_storage/broad_data/michael
# RUN mv DeepProfiler-master/ local_group_storage/broad_data/michael/DeepProfiler
RUN mv DeepProfiler-tf2/ local_group_storage/broad_data/michael/DeepProfiler
WORKDIR local_group_storage/broad_data/michael/DeepProfiler-tf2
RUN pip install -e .
RUN pip install tqdm

# Now aws
WORKDIR /
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install -i /usr/local/aws-cli -b /usr/local/bin
