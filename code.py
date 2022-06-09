import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_hk_public_holiday(in_year):

    url = 'https://www.gov.hk/en/about/abouthk/holiday/'+str(in_year)+'.htm'
    page = requests.get(url)
    # print(response.text)

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page.text, 'html.parser')
    # print(soup.prettify())

    table = soup.find_all('table')
    df = pd.read_html(str(table))[0]

    df[1] = df[1] + " " +str(in_year)

    return pd.to_datetime(df[1], dayfirst=True)[1:]
