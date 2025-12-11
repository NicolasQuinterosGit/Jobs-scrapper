import csv 
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def get_url(position):
    "Genera una url para la posicion buscada"
    template = 'https://ar.indeed.com/q-{}-empleos.html?'
    url _= template.format(position)
    return url

response = requests.get(url)
response
<Response [200]>
response.reason
'OK'
soup = BeautifulSoup(response.text, 'html.parser')