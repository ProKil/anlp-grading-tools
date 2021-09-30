docker build . -t anlp
export ANLP_TMP_DIR=/path/to/anlp-grading-tools/tmp
export SUBMISSION_DIR=/path/to/anlp-grading-tools/submission/
export DATA_DIR=/path/to/anlp-grading-tools/data
export SCORES_DIR=/path/to/anlp-grading-tools/scores
python anlp_grading/main.py
