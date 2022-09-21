docker build . -t anlp
export ANLP_TMP_DIR=/home/ubuntu/anlp-grading-tools/tmp  #replace /home/ubuntu with path to directory for each case
export SUBMISSION_DIR=/home/ubuntu/anlp-grading-tools/submission/
export DATA_DIR=/home/ubuntu/anlp-grading-tools/data
export SCORES_DIR=/home/ubuntu/anlp-grading-tools/scores
python3 anlp_grading/main.py