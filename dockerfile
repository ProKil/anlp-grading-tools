FROM pytorch/pytorch:1.7.0-cuda11.0-cudnn8-devel
#nvcr.io/nvidia/pytorch:19.08-py3
#nvidia/cuda:10.1-cudnn7-runtime
#nvcr.io/nvidia/pytorch:19.08-py3
ADD anlp_grading /anlp_grading
WORKDIR /usr/src/app
COPY . .
# ARG USER_ID
# ARG GROUP_ID
# RUN addgroup --gid $GROUP_ID user
# RUN useradd -m $USER_ID
#install pip
RUN pip install --upgrade pip


#RUN pip install -e .
# RUN pip install pytorch==1.8.0 
# RUN pip install torchvision
# RUN pip install torchaudio 
#RUN pip install cudatoolkit=10.1
RUN pip install numpy
RUN pip install tqdm==4.58.0
RUN pip install requests==2.25.1
RUN pip install importlib-metadata==3.7.0
RUN pip install filelock==3.0.12
RUN pip install sklearn==0.0
RUN pip install tokenizers==0.10.1


# RUN mkdir -p /mnt/code && chown -R 777 /mnt/code
# RUN mkdir -p /mnt/data && chown -R 777 /mnt/data
# RUN mkdir -p /mnt/scores && chown -R 777 /mnt/scores
# USER $USER_ID


#Create conda environment
# ENV CONDA_DIR /opt/conda
# RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && /bin/bash ~/miniconda.sh -b -p /opt/conda
# #Put conda in path so we can use conda activate
# ENV PATH=$CONDA_DIR/bin:$PATH


CMD ["/anlp_grading/test.py"]
ENTRYPOINT ["python3"]
