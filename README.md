# Grading tools for Advanced NLP (11-711)

## Installation

You'll need `docker` and `unzip` to use this repo. For `docker`, visit the [official guide](https://docs.docker.com/get-started/) to get started. For `unzip`, you can install it on ubuntu via `sudo apt-get install unzip`.

Install the python package by 
```
git clone https://github.com/ProKil/anlp-grading-tools
cd anlp-grading-tools
pip install -e .
```


## Usage

To evaluate your code, you'll need to change the environment variables in test.sh.

`ANLP_TMP_DIR`: `mkdir` a new folder, e.g. `mkdir tmp`, and point this variable to the absolute path of the tmp folder. 

`SUBMISSION_DIR`: this should point to the folder containing your submission zip file. Note that the toolkit will automatically evaluate all zip files in the folder. 

`SCORES_DIR`: this should point to an empty folder. Your score will be logged in a text file there. 

`DATA_DIR`: this should point to the data folder of `minnn-assignment`. Please copy the original `minnn-assignment/classifier.py` to `minnn-assignment/data/classifier_orig.py` to test if your code can be executed with the original classifier. 

Example code to prepare the folders:
```
mkdir tmp
mkdir scores
cp -r path/to/minnn-assignment/data ./
cp path/to/minnn-assignment/classifier.py data/classifier_orig.py
mkdir submission
cp your/submission.zip submission
```

Now you can evaluate your code through `bash test.sh`, after which your scores are at `SCORES_DIR/andrewid`. It is normal to get 0s for the last two (correct labels for the imdb test set are not available), but you should get reasonable accuracies for the first two (~40).

## Troubleshooting

1. You may find writing files inside `ANLP_TMP_DIR` and `SCORE_DIR` requiring permission. You can either use `sudo` or log into docker through `docker run -v FOLDER_TO_WRITE:/mnt -it --entrypoint /bin/bash anlp` and `cd /mnt` to write those files. 
2. You may experience other permission issues with docker. Please refer to [this page](https://docs.docker.com/engine/install/linux-postinstall/) to use docker without sudo.

