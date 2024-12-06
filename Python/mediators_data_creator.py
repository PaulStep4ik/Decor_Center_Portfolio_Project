import pandas as pd
import config as cfg
import random
from transliterate import translit
from config import BASE_PATH


NUM = random.randint(27, 55) # Amount of mediators 
companies = [
    "Kovalska Group",
    "Zhitlobud-1",
    "Kyivmiskbud",
    "TMM Holding",
    "Intergal-Bud",
    "Beton Kompleks",
    "UDP (Ukrainska Developerska Kompaniya)",
    "Altis-Holding",
    "Spetsbudmontazh",
    "Stolytsia Group"
]

mediators_df = pd.DataFrame()
mediators_df.insert(0, 'ID', range(1, 1 + NUM))

full_names = [cfg.generate_ukrainian_full_name() for _ in range(NUM)]

mediators_df['Full Name'] = [translit(name, 'uk', reversed=True) for name in full_names]
mediators_df['Phone Number'] = [cfg.phone_number_generator() for _ in range(NUM)]
mediators_df['Company'] = [random.choice(companies) for _ in range(NUM)]

mediators_df.to_csv(f'{BASE_PATH}\mediators.csv', index=False, encoding='utf-8')

