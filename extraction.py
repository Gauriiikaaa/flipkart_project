def extract_rules(model, policies):
  inputs = preprocess_data(policies)
  predictions = model.predict(inputs)
  rules = parse_predictions(predictions)
  return rules