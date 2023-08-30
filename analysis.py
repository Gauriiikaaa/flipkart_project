def check_violations(logs, rules):
  violations = []
  
  for log in logs:
    if violates(log, rules):
      violations.append(log)
      
  return violations