# CSE517 Project

We attempt to reproduce the experiments described in [this EMNLP 2021 paper](https://aclanthology.org/2021.emnlp-main.10.pdf), Decision-Focused Summarization, by Chao-Chun Hsu and Chenhao Tan, for our CSE517: Natural Language Processing class at the University of Washington. A writeup of our reproduction may be found [here](https://github.com/ericxiaseattle/CSE517-Project/raw/main/out/projectv2.pdf), and the directories assets, out, and src correspond to the different versions of our writeup.

In our reproduction, we discovered that the authors' repo contains some code errors (e.g. syntax) and have fixed them in this repo. 
All other directories are associated with DecSum, and as we were having problems pushing the directories OUTPUT_DIR, YELP_DATA_DIR, and results to Github due to their large file size, we have instead uploaded them to [MEGA](https://insertmegalinkhere.com). Some of the documentation in this README.md, when applicable, is copied from the authors' README.md on their repo.

## Environment
First download the MEGA tar.gz archive to the working directory and uncompress it. Then run the following commands.
```
conda create -n yelp python=3.7.6
cat requirements.txt | sed -e '/^\s*#.*$/d' -e '/^\s*$/d' | xargs -n 1 python -m pip install
# download spacy package
python -m spacy download en_core_web_sm

# If you are using RTX3090, try the following step to install pytorch
pip install torch==1.7.0+cu110 -f https://download.pytorch.org/whl/torch_stable.html
```
## Preprocessing
We download the [yelp dataset](https://www.yelp.com/dataset/download) and only select reviews from restaurants to build our dataset. At the base directory, run 
```
python -m preprocess.yelp_preprocess --yelp_data_dir YELP_DATA_DIR --output_dir OUTPUT_DIR
```

## 
