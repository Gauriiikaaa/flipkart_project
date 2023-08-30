# preprocessing.py

import re
import string

from transformers import BertTokenizer

def clean_text(text):
  # Remove punctuation
  text = text.translate(str.maketrans('', '', string.punctuation))
  
  # Lowercase
  text = text.lower()
  
  # Remove extra whitespace
  text = re.sub(r'\s+', ' ', text)
  
  return text

def tokenize(text):
  tokenizer = BertTokenizer.from_pretrained('bert-base-cased')
  tokens = tokenizer.tokenize(text)
  
  return tokens

def create_sequences(tokens, max_len=50):
  # Truncate longer sequences
  if len(tokens) > max_len:
    tokens = tokens[:max_len]
  
  # Pad shorter sequences  
  if len(tokens) < max_len:
    padding = [0] * (max_len - len(tokens)) 
    tokens += padding  
    
  return tokens

def preprocess(text):
  cleaned = clean_text(text)
  tokens = tokenize(text)
  sequences = create_sequences(tokens)
  
  return sequences