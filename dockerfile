FROM python:3.8-slim-buster
ADD anlp_grading /anlp_grading
WORKDIR /usr/src/app
COPY . .
# ARG USER_ID
# ARG GROUP_ID
# RUN addgroup --gid $GROUP_ID user
# RUN useradd -m $USER_ID
RUN pip install -e .
RUN pip install numpy
# RUN mkdir -p /mnt/code && chown -R 777 /mnt/code
# RUN mkdir -p /mnt/data && chown -R 777 /mnt/data
# RUN mkdir -p /mnt/scores && chown -R 777 /mnt/scores
# USER $USER_ID
CMD ["/anlp_grading/test.py"]
ENTRYPOINT ["python3"]
