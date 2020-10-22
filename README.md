# HK-Public-Holiday
This is a python tools for getting the public holiday of each year.


```py

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
```

This program will get the data from HK gov website to obtain the public holiday.

https://www.gov.hk/en/about/abouthk/holiday/2017.htm
