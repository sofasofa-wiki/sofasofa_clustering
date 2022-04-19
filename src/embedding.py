import os

from transformers import AutoTokenizer, AutoModelForMaskedLM, AutoModelForPreTraining, AutoModel
import numpy as np
import torch

model_path = '../pre_model/chinese-roberta-wwm-ext-large'
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModel.from_pretrained(model_path, output_hidden_states=True)

