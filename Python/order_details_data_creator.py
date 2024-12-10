import pandas as pd
import random
from config import BASE_PATH


orders_df = pd.read_csv(f"{BASE_PATH}\\orders.csv")
materials_df = pd.read_csv(f"{BASE_PATH}\\materials.csv")

orders_ids = orders_df['Order ID'].tolist()
materials_ids = materials_df['ID'].tolist()

order_details = []
detail_id_start = 100001

for order_id in orders_ids:
    num_materials = random.choices(
        [1, 2, 3, 4, 5],
        weights=[60, 25, 8, 5, 2],
        k=1
    )[0]

    for _ in range(num_materials):
        material_id = random.choice(materials_ids)

        coverage_area = round(
            random.choices(
                [x / 100 for x in range(100, 15001)],
                weights=[1 if x > 10000 else 5 if 5000 < x <= 10000 else 20 for x in range(100, 15001)],
                k=1
            )[0], 
            2
        )

        min_quantity = round(max(1.00, coverage_area / 10), 2)
        max_quantity = round(max(min_quantity, coverage_area / 2), 2)

        quantity = round(random.uniform(min_quantity, max_quantity), 2)

        price_per_sqm = round(random.uniform(150.00, 600.00), 2)

        order_details.append({
            'ID': detail_id_start,
            'Order ID': order_id,
            'Material ID': material_id,
            'Quantity': quantity,
            'Coverage Area': coverage_area,
            'Price Per SQM': price_per_sqm,
            'Description': ''
        })

        detail_id_start += 1


order_details_df = pd.DataFrame(order_details)
order_details_df.to_csv(f"{BASE_PATH}\\order_details.csv", index=False, encoding='utf-8')

print(order_details_df.head())
