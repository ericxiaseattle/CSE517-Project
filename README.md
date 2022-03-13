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
We download the [yelp dataset](https://www.yelp.com/dataset/download) and only select reviews from restaurants to build our dataset. The preprocessing script
effectively reads in the 52268 restaurants and associated reviews from the dataset and computes the average of the first 50 reviews. At the base directory, run 
```
python -m preprocess.yelp_preprocess --yelp_data_dir YELP_DATA_DIR --output_dir OUTPUT_DIR
```

## Training Longformer Model
Run the command
```
sudo bash scripts/train_transformer.sh
```
The trained model will be saved to a path like `${OUTPUT_DIR}/version_27-12-2021--16-59-15/checkpoints/epoch=1-val_loss=0.12.ckpt`. 

## Running DecSum
We run
```
sudo bash scripts/sentence_selection.sh
```
The DecSum summaries will be saved at `${RES_DIR}/models/sentence_select/selected_sentence/yelp/50reviews/test/Transformer/window_1_DecSum_WD_sentbert_50trunc_1_1_1/best/1/text_.csv`.

*_MSE with True Label_* metric will be store at `${RES_DIR}/models/sentence_select/results/yelp/50reviews/test/Transformer/window_1_DecSum_WD_sentbert_50trunc_1_1_1/best/1/text_.csv`.

## Computing Decision Scores for Individual Sentences
```
sudo bash scripts/single_sentence_score.sh
```
Results will be saved at `${RES_DIR}/models/sentence_select/selected_sentence/yelp/50reviews/test/Transformer/window_1/order/10000/text_.csv`.
Sentences are in the original order for each restaurants (business).

## Additional Experiments 
We carried out experiments beyond the scope of the paper to test the effect of certain hyperparameters on the result. These were done by modifying the parameters in `sentence_select.sh` (e.g. `num_sentences`, `num_review`) and `train_transformer.sh` (e.g. `max_seq_length`). 

## Computing Wasserstein Distances
Rename the result of `single_sentence_score.sh` to `all.csv`. Store the DecSum summaries and `all.csv` into an input directory. Then run 
```
python wasserstein.py PATH/TO/INPUT/DIRECTORY
```

## Generating PDF Plot
```
python pdf.py
```

## Citation of Authors' Paper
```
@inproceedings{hsu-tan-2021-decision,
    title = "Decision-Focused Summarization",
    author = "Hsu, Chao-Chun  and
      Tan, Chenhao",
    booktitle = "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2021",
    address = "Online and Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.emnlp-main.10",
    doi = "10.18653/v1/2021.emnlp-main.10",
    pages = "117--132",
}
```
