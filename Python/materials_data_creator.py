import pandas as pd
import random
import json
from config import BASE_PATH

input_file = 'manufacturers.json'

try:
    with open(input_file, 'r', encoding='utf-8') as file:
        manufacturers = json.load(file)

except FileNotFoundError:
    print(f"File {input_file} not found. Please run the extraction script first.")


manufacturer_material_pairs = []

for manufacturer in manufacturers:
    name = manufacturer['Name']
    materials = manufacturer['Materials']
    
    for material in materials:
        purchase_price = round(random.uniform(120, 430), 2)
        selling_price = round(purchase_price * random.uniform(1.5, 2.2), 2)
        manufacturer_material_pairs.append({'Material': material, 'Manufacturer': name, 'Purchase Price': purchase_price, 'Sell Price': selling_price})


materials_df = pd.DataFrame(manufacturer_material_pairs)
materials_df.insert(0, 'ID', range(1001, 1001 + len(materials_df)))

manufacturers_df = pd.read_csv(f"{BASE_PATH}\manufacturers.csv")

merged_df = pd.merge(materials_df, manufacturers_df, how='inner', left_on='Manufacturer', right_on='Name')
merged_df = merged_df.drop(columns=['Name', 'Website', 'Country', 'Manufacturer'])
merged_df = merged_df.rename(columns={'ID_x':'ID', 'ID_y':'Manufacturer_ID'})

result_df = merged_df[['ID', 'Material', 'Manufacturer_ID', 'Purchase Price',  'Sell Price']]

result_df.to_csv(f"{BASE_PATH}\materials.csv", index=False, encoding='utf-8')