import csv 
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def get_url(position, location):
    "Genera una url para la posicion buscada"
    template = 'https://ar.indeed.com/q-{}-l-{}-empleos.html'
    url = template.format(position, location)
    return url
url = get_url('data-scientist', 'Buenos-Aires')

response = requests.get(url)
response

response.reason

soup = BeautifulSoup(response.text, 'html.parser')
cards = soup.find_all('div', 'slider_container css-weo834 eu4oa1w0')
len(cards)

card=''
if (cards and cards[0] is not None):
    card = cards[0]
atag = card.h2.a
job_title = atag.get('title')
job_url = 'https://ar.indeed.com' + atag.get('href')
company = card.find('span', 'company-name').text.strip()

job_location = card.find('div', class_='css-1f06pz4 eu4oa1w0').get_text(strip=True)
## Funcion para extraer los datos de cada trabajo
def get_record(card):
    "Extrae los datos de un trabajo"
    atag = card.h2.a
    job_title = atag.get('title')
    job_url = 'https://ar.indeed.com' + atag.get('href')
    company = card.find('span', 'company-name').text.strip()
    job_location = card.find('div', class_='css-1f06pz4 eu4oa1w0').get_text(strip=True)

    record = (job_title, company, job_location, job_url)
    return record

records = []
for card in cards:
    record = get_record(card)
    records.append(record)

records[:3]
