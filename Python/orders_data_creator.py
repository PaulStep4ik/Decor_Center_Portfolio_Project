import pandas as pd
import random
from datetime import datetime, timedelta
from config import BASE_PATH


NUM = random.randint(900, 1100)  # Amount of orders

# Read data from already generated files
customers_df = pd.read_csv(f"{BASE_PATH}\customers.csv")
mediators_df = pd.read_csv(f"{BASE_PATH}\mediators.csv")

# Cities and their streets in translit as a dictionary
city_street_map = {
    "Kyiv": [
        "Khreshchatyk St.", "Volodymyrska St.", "Bohdana Khmelnytskoho St.",
        "Lesi Ukrainky Blvd.", "Pobedy Ave.", "Andriivskyi Uzviz",
        "Instytutska St.", "Saksahanskoho St.", "Velyka Vasylkivska St.",
        "Shevchenka Ave."
    ],
    "Kharkiv": [
        "Sumska St.", "Haharina Ave.", "Poltavskyi Shlyakh St.",
        "Pushkinska St.", "Universytetska St.", "Moskovskyi Ave.",
        "Holodnohirska St.", "Heroiv Kharkova Ave.", "Svobody Sq.", 
        "Nauky Ave."
    ],
    "Lviv": [
        "Svobody Ave.", "Halytska St.", "Rynok Sq.",
        "Virmenska St.", "Franko St.", "Shevchenka St.",
        "Chornovola Ave.", "Leva St.", "Kopernyka St.",
        "Bandery St."
    ],
    "Odesa": [
        "Derybasivska St.", "Prymorskyi Blvd.", "Pushkinska St.",
        "Hretska St.", "Kanatna St.", "Frantsuzkyi Blvd.",
        "Polska St.", "Novoselskoho St.", "Tolstoho St.",
        "Mykhailivska St."
    ],
    "Dnipro": [
        "Dmytra Yavornytskoho Ave.", "Kalynova St.", "Myrna St.",
        "Peremohy Sq.", "Heroiv Ave.", "Zakhidna St.",
        "Glinka St.", "Verkhniy Val St.", "Stepova St."
    ],
    "Zaporizhzhia": [
        "Sobornyi Ave.", "Tsentralna St.", "Peremohy St.",
        "Pratsi Sq.", "Pobedy Blvd.", "Pivnichna St.",
        "Khortytska St.", "Molodizhna St.", "Dniprovska St."
    ],
    "Vinnytsia": [
        "Soborna St.", "Kyivs'ka St.", "Pirogova St.",
        "Hrushevskogo St.", "Zamkova St.", "Korolenko St.",
        "Vasylenka St.", "Budivelnykiv St.", "Sportyvna St."
    ],
    "Poltava": [
        "Sobornosti St.", "Pushkina St.", "Zhovtneva St.",
        "Mazepy St.", "Chornovola St.", "Oktober St.",
        "Kirova St.", "Kalynova St.", "Sadova St."
    ],
    "Chernihiv": [
        "Shevchenka St.", "Piatnytska St.", "Rokossovskoho St.",
        "Nezalezhnosti St.", "Haharina St.", "Kotsyubynskoho St.",
        "Lazariana St.", "Dniprovska St.", "Myru St."
    ],
    "Mykolaiv": [
        "Admiralska St.", "Sadova St.", "Shevchenka St.",
        "Lenina St.", "Chkalova St.", "Khortytska St.",
        "Frunze St.", "Nezalezhnosti St.", "Dunaeva St."
    ],
    "Ivano-Frankivsk": [
        "Nezalezhnosti St.", "Hrushevskoho St.", "Shevchenka St.",
        "Konovaltsya St.", "Sichovykh Striltsiv St.", "Melnyka St.",
        "Levytskoho St.", "Holovna St.", "Sportyvna St."
    ],
    "Sumy": [
        "Kharkivska St.", "Pokrovska St.", "Soborna St.",
        "Heroyiv St.", "Vyshneva St.", "Zhovtneva St.",
        "Myru Ave.", "Lermontova St.", "Sadova St."
    ]
}

cities = list(city_street_map.keys())
priority_cities = ["Kyiv", "Kharkiv", "Lviv", "Odesa"]

def generate_address(city):
    street = random.choice(city_street_map[city])
    building_number = random.randint(1,255)
    return f"{street}, {building_number}"

# Generate orders
orders_df = pd.DataFrame()
orders_df['Order ID'] = range(10001, 10001 + NUM)
orders_df['Customer ID'] = [random.choice(customers_df['ID']) for _ in range(NUM)]
orders_df['Mediator ID'] = [random.choice(mediators_df['ID']) for _ in range(NUM)]
orders_df['City'] = [
    random.choices(priority_cities + cities, weights=[5] * len(priority_cities) + [1] * len(cities), k=1)[0]
    for _ in range(NUM)
]
orders_df['Address'] = [generate_address(city) for city in orders_df['City']]

# Generate random order dates within the last 2 years
start_date = datetime.now() - timedelta(days=730)
orders_df['Order Date'] = [
    (start_date + timedelta(days=random.randint(0, 730))).strftime('%Y-%m-%d') for _ in range(NUM)
]

# Save to CSV
orders_df.to_csv(f"{BASE_PATH}\orders.csv", index=False, encoding='utf-8')