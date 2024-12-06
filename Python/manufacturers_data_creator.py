import json
import pandas as pd
from config import BASE_PATH

input_file = 'manufacturers.json'

try:
    with open(input_file, 'r', encoding='utf-8') as file:
        manufacturers = json.load(file)

except FileNotFoundError:
    print(f"File {input_file} not found. Please run the extraction script first.")


manufacturers_df = pd.DataFrame([{'Name': manufacturer['Name'], 'Country': manufacturer['Country'], 'Website': manufacturer['Website']} for manufacturer in manufacturers])

manufacturers_df.insert(0, 'ID', range(101, 101 + len(manufacturers_df)))

manufacturers_df.to_csv(f"{BASE_PATH}\manufacturers.csv", index=False, encoding='utf-8')