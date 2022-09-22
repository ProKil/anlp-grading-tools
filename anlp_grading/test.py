from pathlib import Path
from utils import execute_cli_timeout, compare_outputs
import os
import time
import torch
data_folder = Path('/mnt/data')
student_folder = Path('/mnt/code')
scores_folder = Path('/mnt/scores')


execute_cli_timeout(
    'cd /mnt/code && '
    'python3 /mnt/code/classifier.py '
    '--option=pretrain '
    '--epochs=10 '
    '--lr=1e-3 '
    '--use_gpu '
    '--batch_size=64 '
    '--train=/mnt/data/sst-train.txt '
    '--dev=/mnt/data/sst-dev.txt '
    '--test=/mnt/data/sst-test.txt '
    '--dev_out=/mnt/scores/sst-dev-output.txt '
    '--test_out=/mnt/scores/sst-test-output.txt ',
    timeout=4200
)

sst_pretrain_dev_acc = compare_outputs(std="/mnt/data/sst-dev.txt", result="/mnt/scores/sst-dev-output.txt")
sst_pretrain_test_acc = compare_outputs(std="/mnt/data/sst-test.txt", result="/mnt/scores/sst-test-output.txt")

print('sst pretrain dev accuracy ',sst_pretrain_dev_acc)
print('sst pretrain test accuracy ', sst_pretrain_test_acc)

execute_cli_timeout(
    'cd /mnt/code && '
    'python3 /mnt/code/classifier.py '
    '--option=finetune '
    '--epochs=10 '
    '--lr=1e-5 '
    '--use_gpu '
    '--batch_size=64 '
    '--train=/mnt/data/sst-train.txt '
    '--dev=/mnt/data/sst-dev.txt '
    '--test=/mnt/data/sst-test.txt '
    '--dev_out=/mnt/scores/sst-dev-output.txt '
    '--test_out=/mnt/scores/sst-test-output.txt ',
    timeout=4200
)

sst_finetune_dev_acc = compare_outputs(std="/mnt/data/sst-dev.txt", result="/mnt/scores/sst-dev-output.txt")
sst_finetune_test_acc = compare_outputs(std="/mnt/data/sst-test.txt", result="/mnt/scores/sst-test-output.txt")

print('sst finetune dev accuracy ',sst_finetune_dev_acc)
print('sst finetune test accuracy ', sst_finetune_test_acc)


#sst_acc_orig = compare_outputs(std="/mnt/data/sst-test.txt", result="/usr/src/app/sst-test-output-orig.txt")
execute_cli_timeout(
    'cd /mnt/code && '
    'python3 /mnt/code/classifier.py '
    '--option=finetune '
    '--epochs=10 '
    '--lr=1e-5 '
    '--use_gpu '
    '--batch_size=8 '
    '--train=/mnt/data/cfimdb-train.txt '
    '--dev=/mnt/data/cfimdb-dev.txt '
    '--test=/mnt/data/cfimdb-test.txt '
    '--dev=/mnt/data/cfimdb-dev.txt  '
    '--dev_out=/mnt/scores/cfimdb-dev-output.txt ',
    timeout=4200
)

cfimdb_finetune_dev_acc = compare_outputs(std="/mnt/data/cfimdb-dev.txt", result="/mnt/scores/cfimdb-dev-output.txt")

print('cfimdb finetune dev accuracy ',cfimdb_finetune_dev_acc)


with open(scores_folder / os.environ["ANDREW_ID"], "w") as f:
    f.write(f"{sst_pretrain_dev_acc}\t{sst_pretrain_test_acc}\t{sst_finetune_dev_acc}\t{sst_finetune_test_acc}\t{cfimdb_finetune_dev_acc}")

execute_cli_timeout(
    'rm -rf /mnt/code/*',
    timeout=60
)