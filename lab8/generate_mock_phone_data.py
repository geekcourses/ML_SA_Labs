import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker to generate realistic data
fake = Faker()

# Generate mock data
data = {
    "PhoneNumber": [fake.phone_number() for _ in range(20)],
    "MinTalking": np.random.randint(1, 600, 20),  # Assuming minutes range from 1 to 600
    "Date": pd.date_range(start="2023-01-01", periods=20, freq='D').date
}

# Create DataFrame
df_phone = pd.DataFrame(data)

# Convert DataFrame to CSV
csv_phone_filename = ""
df_phone.to_csv('./datasets/phone.csv', index=False)

