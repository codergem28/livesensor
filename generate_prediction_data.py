import yaml
import pandas as pd
import numpy as np

# Read schema
with open("config/schema.yaml", "r") as file:
    schema = yaml.safe_load(file)

# Get feature names
columns = schema["numerical_columns"]

# Number of rows you want
num_rows = 20

# Generate random values
data = {}

for col in columns:
   data[col] = np.random.randint(0, 1000, size=num_rows).astype(float)

# Create DataFrame
df = pd.DataFrame(data)

# Save CSV
df.to_csv("prediction_input.csv", index=False)

print("CSV generated successfully!")
print(df.head())