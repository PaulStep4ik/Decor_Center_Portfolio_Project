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

        coverage_area = random.choices(
            range(1, 151),
            weights=[1 if x > 100 else 5 if 50 < x <= 100 else 20 for x in range(1, 151)],
            k=1
        )[0]

        min_quantity = max(1, coverage_area // 10)
        max_quantity = max(min_quantity, coverage_area // 2)

        quantity = random.randint(min_quantity, max_quantity)


        price_per_sqm = random.randint(150, 600)

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
