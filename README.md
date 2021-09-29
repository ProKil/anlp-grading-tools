# Grading tools for Advanced NLP (11-711)

## Installation

You'll need `docker` to use this repo. Visit the [official guide](https://docs.docker.com/get-started/) to get started. 

After you have install `docker`, install the python package by 

```
git clone https://github.com/ProKil/anlp-grading-tools
cd anlp-grading-tools
pip install -e .
```


## Usage

To evaluate your code, you'll need to change the environment variables in test.sh.

`ANLP_TMP_DIR`: `mkdir` a new folder, e.g. `mkdir tmp`, and point this variable to the absolute path of the tmp folder. 
`SUBMISSION_DIR`: this should point to the folder containing your submission zip file. Note that the toolkit will automatically evaluate all zip files in the folder. 
`SCORE_DIR`: this should point to an empty folder. Your score will be logged in a text file there. 

## Troubleshooting

You may find writing files inside `ANLP_TMP_DIR` and `SCORE_DIR` requires permission. You can either use `sudo` or log into docker through `docker run -v FOLDER_TO_WRITE:/mnt -it --entrypoint /bin/bash anlp` and `cd /mnt` to write those files. 