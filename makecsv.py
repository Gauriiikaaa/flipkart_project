import pandas as pd

# Sample data
data = [
    {"log_id": 1, "date": "2022-01-01", "user": "john@company.com", "activity": "Copied customer data to laptop", "status": "Unauthorized"},
    {"log_id": 2, "date": "2022-01-05", "user": "alice@company.com", "activity": "Accessed production server", "status": "Unauthorized"},
    {"log_id": 3, "date": "2022-01-07", "user": "bob@company.com", "activity": "Uploaded code changes to production", "status": "Policy Violation"},
    {"log_id": 4, "date": "2022-01-12", "user": "john@company.com", "activity": "Shared password with coworker", "status": "Security Breach"},
    {"log_id": 5, "date": "2022-01-15", "user": "david@company.com", "activity": "Restarted production server", "status": "Admin Activity Logged"}
]

# Map status labels to integers
label_mapping = {
    "Unauthorized": 0,
    "Policy Violation": 1,
    "Security Breach": 2,
    "Admin Activity Logged": 3,
    # ... add more labels and mappings
}

# Create a DataFrame
df = pd.DataFrame(data)

# Add a label column based on the status mapping
df["label"] = df["status"].map(label_mapping)

# Save to CSV
df.to_csv("log.csv", index=False)

print("CSV file 'logs_with_labels.csv' created.")
