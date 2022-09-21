#!/usr/bin/env bash
# conda init bash
# conda create -n bert_hw -y python=3.7
conda activate pytorch
conda install -y pytorch==1.8.0 torchvision torchaudio cudatoolkit=10.1 -c pytorch
pip install tqdm==4.58.0
pip install requests==2.25.1
pip install importlib-metadata==3.7.0
pip install filelock==3.0.12
pip install sklearn==0.0
pip install tokenizers==0.10.1