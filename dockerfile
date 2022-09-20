FROM nvcr.io/nvidia/pytorch:19.08-py3
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

RUN pip install -e .
RUN pip install numpy
# RUN mkdir -p /mnt/code && chown -R 777 /mnt/code
# RUN mkdir -p /mnt/data && chown -R 777 /mnt/data
# RUN mkdir -p /mnt/scores && chown -R 777 /mnt/scores
# USER $USER_ID
CMD ["/anlp_grading/test.py"]
ENTRYPOINT ["python3"]
