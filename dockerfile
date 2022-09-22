FROM pytorch/pytorch:latest

ADD anlp_grading /anlp_grading
WORKDIR /usr/src/app
COPY . .
# ARG USER_ID
# ARG GROUP_ID
# RUN addgroup --gid $GROUP_ID user
# RUN useradd -m $USER_ID
#install pip
RUN pip install --upgrade pip


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


CMD ["/anlp_grading/test.py"]
ENTRYPOINT ["python3"]