docker build . -t anlp
export ANLP_TMP_DIR=./tmp
export SUBMISSION_DIR=./submission/
export DATA_DIR=./data
export SCORES_DIR=./scores
python3 anlp_grading/main.py