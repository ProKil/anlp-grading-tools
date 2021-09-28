import os
from anlp_grading.utils import get_all_zip_files, parse_canvas_format

tmp_dir = os.environ['ANLP_TMP_DIR']
if tmp_dir == "":
    print("set ANLP_TMP_DIR to a directory where you want to store the code.")
    exit(1)

submission_dir = os.environ['SUBMISSION_DIR']
if submission_dir == "":
    print("set SUBMISSION_DIR to folder contains submission zip files")
    exit(1)

data_dir = os.environ["DATA_DIR"]
if data_dir == "":
    print("set DATA_DIR to folder contains data zip files")
    exit(1)

scores_dir = os.environ["SCORES_DIR"]
if scores_dir == "":
    print("set SCORES_DIR to folder where to store results")
    exit(1)

files = get_all_zip_files(submission_dir)
parse_canvas_format(files)

for f in files:
    # unzip and expand zip file
    andrewid = f.name.split("/")[-1].split(".")[0]
    print(f"grading {andrewid}")
    os.system(f"unzip -o {f.absolute()} -d {tmp_dir}")
    new_folder = f"{tmp_dir}/{andrewid}"
    # run docker mounted code and data
    os.system(f"docker run -v {new_folder}:/mnt/code -v {data_dir}:/mnt/data -v {scores_dir}:/mnt/scores -e ANDREW_ID={andrewid} -it anlp")
    # remove the folder
    os.system(f"rm -rf {new_folder}")