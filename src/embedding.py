import os

from transformers import AutoTokenizer, AutoModel
from sentence_transformers import SentenceTransformer
import numpy as np
import torch

model_path = '../pre_model/chinese-roberta-wwm-ext-large'
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModel.from_pretrained(model_path, output_hidden_states=True)

sentence_model_path = '../pre_model/paraphrase-multilingual-mpnet-base-v2'
sentence_model = SentenceTransformer(sentence_model_path)


def get_tag_embedding(tags):
    # AutoTokenizer, AutoModel调用预训练好的模型获取词向量
    inputs = tokenizer(tags, return_tensors='pt', padding=True)
    output = model(**inputs)


def get_title_embedding(texts):
    # SentenceTransformer调用预训练好的句向量模型获取句向量
    sentence_embeddings = sentence_model.encode(texts)
    return sentence_embeddings


def get_embeddings():
    pass
