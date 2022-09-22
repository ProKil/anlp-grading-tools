import pathlib
from typing import List


def get_all_zip_files(submission_dir) -> List[pathlib.Path]:
    """
    Get all zip files in submission_dir
    :param submission_dir:
    :return: list of zip files
    """
    flist = []
    for p in pathlib.Path(f"{submission_dir}/.").iterdir():
        if p.is_file():
            extension = p.name.split(".")[-1]
            if extension == "zip":
                flist.append(p)

    return flist


def parse_canvas_format(flist: List[pathlib.Path]):
    """
    mv canvas format zip file names to andrewid.zip
    :param flist:
    """
    for f in flist:
        folder = f.parents[0]
        fname = f.name.split("/")[-1]
        andrewid = fname.split(".")[0].split("_")[-1].split("-")[0]
        new_name = f"{andrewid}.zip"
        f.rename(folder / new_name)


def execute_cli_timeout(cmd, timeout):
    """
    Execute a command line command with a timeout
    :param cmd:
    :param timeout:
    :return:
    """
    import os
    import signal
    from subprocess import Popen, PIPE, TimeoutExpired
    from time import monotonic as timer

    start = timer()
    with Popen(cmd, shell=True, stdout=PIPE, preexec_fn=os.setsid) as process:
        try:
            _ = process.communicate(timeout=timeout)[0]
        except TimeoutExpired:
            os.killpg(process.pid, signal.SIGINT)  # send signal to the process group
            _ = process.communicate()[0]
    print('Elapsed seconds: {:.2f}'.format(timer() - start))


def compare_outputs(std, result):
    try:
        same = []
        result_lines = open(result).readlines()
        for idx, line1 in enumerate(open(std)):
            expected = line1.split('|||')[0].strip()
            predicted = result_lines[idx].split('|||')[2].strip()
            same.append(1 if predicted == expected else 0)
        return sum(same) / len(same)
    except Exception as e:
        print(e)
        return 0