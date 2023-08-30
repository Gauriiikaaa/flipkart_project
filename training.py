
import tensorflow as tf
from transformers import TFBertForSequenceClassification

def train_model(train_data):
  
  model = TFBertForSequenceClassification.from_pretrained("bert-base-cased")

  # Unpack the tuple
  input_ids, labels = train_data

  model.compile(optimizer=tf.keras.optimizers.Adam(),
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=tf.metrics.SparseCategoricalAccuracy())
  
 
  model.fit(input_ids, labels, epochs=5)
  
  return model
