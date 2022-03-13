#!/bin/bash
set -x

OUTPUT_DIR=OUTPUT_DIR
MODEL_PATH=results/epoch=2-val_loss=0.14.ckpt
RES_DIR=${OUTPUT_DIR}/models/sentence_select/

# every sentence
python -m models.sentence_select.main \
        --device 1 \
        --feature_used notes \
        --segment window_1 \
        --model Transformer \
        --score_function order \
        --return_candidates 10000 \
        --trained_model_path ${MODEL_PATH} \
        --result_dir ${RES_DIR} \
        --data_dir ${OUTPUT_DIR} \
        --data yelp \
        --target_type reg 

# # with all input
# python -m models.sentence_select.main \
#         --device 1 \
#         --feature_used notes \
#         --segment all \
#         --model Transformer \
#         --trained_model_path ${MODEL_PATH} \
#         --result_dir ${RES_DIR} \
#         --data_dir ${OUTPUT_DIR} \
#         --data yelp \
#         --target_type reg 
