import requests
import re
import json
from bs4 import BeautifulSoup as BS
from translate import Translator

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

url = 'https://prof-decor.com.ua/brands'
html_content = requests.get(url, headers=headers)
translator = Translator(from_lang="ukrainian", to_lang="english")
output_file = 'manufacturers.json'

if html_content.status_code == 200:

    soup = BS(html_content.content, 'html.parser')
    
    # Find start and end headers

    start_header = soup.find(lambda tag: tag.name in ["h1", "h2", "h3"] and "Виробники декоративної штукатурки і фарби" in tag.get_text(strip=True))
    end_header = soup.find(lambda tag: tag.name in ["h1", "h2", "h3"] and "Види плінтуса" in tag.get_text(strip=True))

    # Collect data between start and end headers

    manufacturers = []
    if start_header and end_header:
        content_between = []
        for sibling in start_header.find_next_siblings():
            if sibling == end_header:
                break
            content_between.append(sibling)

        # Get data about manufacturers

        with open('manufacturers_sites.txt', 'r', encoding='utf-8') as f:
            websites = [line.strip(',\n') for line in f.readlines() if line.strip()]

        for block, website in zip(content_between, websites):
            if block.name == 'div' and 'item-block' in block.get('class', []):
                manufacturer = {}
                
                # Manufacturer name
                name_tag = block.find('h3')
                if name_tag:
                    manufacturer['Name'] = re.sub(r'\s*\(.*?\)', '', name_tag.get_text(strip=True))
                
                # Country
                country_tag = block.find('div', style=lambda value: value and 'min-height: 40px;' in value)
                if country_tag:
                    manufacturer['Country'] = translator.translate(country_tag.get_text(strip=True).replace("Виробництво: ", ""))
                
                # Materials
                materials = []
                for material_link in block.find_all('a', class_='link'):
                    materials.append(re.sub(r'\s*\(.*?\)', '', material_link.get_text(strip=True)))
                manufacturer['Materials'] = materials

                # Website
                manufacturer['Website'] = website


                manufacturers.append(manufacturer)

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(manufacturers, file, ensure_ascii=False, indent=4)

else:
    print(f"Error: {html_content.status_code}")
