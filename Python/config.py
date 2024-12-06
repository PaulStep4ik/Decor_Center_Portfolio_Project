import random
from faker import Faker

# Path for storing generated files with datasets
BASE_PATH = r"C:\Portfolio Project - Decor Center\Generated Data"

fake = Faker('uk_UA')

# Function for phone number generation
def phone_number_generator():
    country_code = '+380'
    operator_codes = ['67', '68', '96', '97', '98', '50', '66', '95', '99', '63', '73', '93']
    operator_code = random.choice(operator_codes)
    number = f"{random.randint(0, 9999999):07d}"
    return f"{country_code}{operator_code}{number}"

# Function for full name generation
def generate_ukrainian_full_name():
    return f"{fake.last_name()} {fake.first_name()} {fake.middle_name()}"