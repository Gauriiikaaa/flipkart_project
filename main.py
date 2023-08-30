def main(logs, policies):

  # Preprocess data
  train_data = preprocessing(policies)

  # Train model
  model = training.train_model(train_data)

  # Extract rules
  rules = extraction.extract_rules(model, policies)

  # Check violations
  violations = analysis.check_violations(logs, rules)

  return violations