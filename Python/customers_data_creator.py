import pandas as pd
import random
import config as cfg
from transliterate import translit
from config import BASE_PATH


# Amount of customers
NUM = random.randint(500, 800)  

customers_df = pd.DataFrame()
customers_df.insert(0, 'ID', range(10001, 10001 + NUM))

full_names = [cfg.generate_ukrainian_full_name() for _ in range(NUM)]
customers_df['Full Name'] = [
    translit(name, 'uk', reversed=True) for name in full_names
]

customers_df['Phone Number'] = [cfg.phone_number_generator() for _ in range(NUM)]

customers_df.to_csv(f"{BASE_PATH}/customers.csv", index=False, encoding='utf-8')