from pathlib import Path
from utils import execute_cli_timeout, compare_outputs
import os
import time
import torch
data_folder = Path('/mnt/data')
student_folder = Path('/mnt/code')
scores_folder = Path('/mnt/scores')


print(torch.cuda.is_available())

print('Running setup.sh')

execute_cli_timeout('bash ls', timeout=1800)
#execute_cli_timeout('cp /mnt/data/classifier_orig.py /mnt/code/classifier_orig.py', timeout=600)

print('Running pretrain')

start = time.time()

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
    '--test=/mnt/data/sst-test.txt ',

    timeout=1800
)

end = time.time()
print("Time elapased" ,end - start)

sst_pretrain_dev_acc = compare_outputs(std="/mnt/data/sst-dev.txt", result="/mnt/./sst-dev-output.txt")
sst_pretrain_test_acc = compare_outputs(std="/mnt/data/sst-test.txt", result="/mnt/./sst-test-output.txt")


print('Running finetune')

start = time.time()

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
    '--test=/mnt/data/sst-test.txt ',
    timeout=1800
)

end = time.time()
print("Time elapased" ,end - start)

sst_finetune_dev_acc = compare_outputs(std="/mnt/data/sst-dev.txt", result="/mnt/./sst-dev-output.txt")
sst_finetune_test_acc = compare_outputs(std="/mnt/data/sst-test.txt", result="/mnt/./sst-test-output.txt")

print('Running cfimdb finetune')
start = time.time()

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
    '--test=/mnt/data/cfimdb-test.txt ',
    timeout=1800
)

end = time.time()
print("Time elapased" ,end - start)

cfimdb_finetune_dev_acc = compare_outputs(std="/mnt/data/cfimdb-dev.txt", result="/mnt/./cfimdb-dev-output.txt")
# cfimdb_pretain_test_acc = compare_outputs(std="/mnt/data/sst-test.txt", result="/usr/src/app/sst-test-output.txt")

# execute_cli_timeout(
#     'cd /mnt/code && '
#     'python3 /mnt/code/classifier.py '
#     '--option=finetune'
#     '--epochs=10'
#     '--lr=1e-5'
#     '--train=/mnt/data/cfimdb-train.txt '
#     '--dev=/mnt/data/cfimdb-dev.txt '
#     '--test=/mnt/data/cfimdb-test.txt '
#     '--dev_out=/usr/src/app/cfimdb-dev-output.txt '
#     '--test_out=/usr/src/app/cfimdb-test-output-orig.txt ',
#     timeout=1800
# )
# cfimdb_pretrain_dev_acc = compare_outputs(std="/mnt/data/sst-dev.txt", result="/usr/src/app/sst-dev-output.txt")
#cfimdb_pretain_test_acc = compare_outputs(std="/mnt/data/sst-test.txt", result="/usr/src/app/sst-test-output.txt")

print(sst_pretrain_dev_acc, sst_pretrain_test_acc, sst_finetune_dev_acc, sst_finetune_test_acc,cfimdb_finetune_dev_acc)

with open(scores_folder / os.environ["ANDREW_ID"], "w") as f:
    f.write(f"{sst_pretrain_dev_acc}\t{sst_pretrain_test_acc}\t{sst_finetune_dev_acc}\t{sst_finetune_test_acc}\t{cfimdb_finetune_dev_acc}")

execute_cli_timeout(
    'rm -rf /mnt/code/*',
    timeout=60
)