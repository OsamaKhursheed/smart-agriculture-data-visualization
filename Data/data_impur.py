import pandas as pd
import numpy as np
import random

# Load the original dataset
df = pd.read_csv('crop_dataset.csv')  # Replace 'original_dataset.csv' with your dataset file path

# Introduce missing values
missing_fraction = 0.05  # 5% of data will have missing values
missing_indices = random.sample(range(len(df)), int(len(df) * missing_fraction))
for index in missing_indices:
    column = random.choice(df.columns)
    df.at[index, column] = np.nan

# Introduce duplicate rows
duplicate_fraction = 0.03  # 3% of data will be duplicated
duplicate_indices = random.sample(range(len(df)), int(len(df) * duplicate_fraction))
df = pd.concat([df, df.iloc[duplicate_indices]], ignore_index=True)

# Introduce outliers
outlier_fraction = 0.02  # 2% of data will have outliers
outlier_indices = random.sample(range(len(df)), int(len(df) * outlier_fraction))
for index in outlier_indices:
    column = random.choice(df.select_dtypes(include=['float64', 'int64']).columns)
    df.at[index, column] *= 10  # Multiply by 10 to introduce outliers

# Introduce inconsistent or incorrect data
incorrect_fraction = 0.01  # 1% of data will have incorrect or inconsistent data
incorrect_indices = random.sample(range(len(df)), int(len(df) * incorrect_fraction))
for index in incorrect_indices:
    column = random.choice(df.columns)
    if column != 'label':
        df.at[index, column] = 'unknown' if isinstance(df.at[index, column], str) else -100  # Incorrect label and temperature

# Save the modified dataset
df.to_csv('crop_dataset2.csv', index=False)
