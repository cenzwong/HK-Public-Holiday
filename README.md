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


```py
get_hk_public_holiday(2018)

# =========
1    2018-01-01
2    2018-02-16
3    2018-02-17
4    2018-02-19
5    2018-03-30
6    2018-03-31
7    2018-04-02
8    2018-04-05
9    2018-05-01
10   2018-05-22
11   2018-06-18
12   2018-07-02
13   2018-09-25
14   2018-10-01
15   2018-10-17
16   2018-12-25
17   2018-12-26
Name: 1, dtype: datetime64[ns]
```
