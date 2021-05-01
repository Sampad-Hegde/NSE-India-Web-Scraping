# National Stock Exchange (India) Web-Scraping For getting Required Data

## WebSite-Url : [https://www.nseindia.com/](https://www.nseindia.com/)

## gereral.py
That uses NSE private search api for getting id of a stock

example tata moors (Common name) :- TATAMOTORSEQN (ID assigned by NSE)
```python
from general import getId
id = getId('tata motors')
```


## today_all_stock.py
Gives all data of all companies including NIFTY, and you save it as CSV file.
getTodayData() returns tuple in the form of (nifty_data, Company_data)

```python
from today_all_stocks import getTodayData
nifty_data, companies_data = getTodayData() 
```

## intra_day.py
if you call the function intraDay(company_id) or nifty_intraDay(nifty_type) to get live data i.e., from 09:00:00 AM to till now

For Companies use like this,
```python
from intra_day import Intra_Day
ID = Intra_Day('TATA MOTORS')
timeStamp, dataPoints = ID.intraDay()
```

and for NIFTY use,

```python
from intra_day import Intra_Day
ID = Intra_Day('NIFTY 50')
timeStamp, dataPoints = ID.nifty_intraDay()
```

call nifty_intraday() or intraDay() as many times you need


## individual_company_stock.py
This will give you the historical data of that stock. max 3 years 

```python
from individual_company_stock import getHistoryData
getHistoryData('SHREECEM',from_date='30-04-2020',to_date='30-04-2021') 
# Default params : from_date = today's date in last year DD-MM-(YYYY-1), to_date=today's date DD-MM-YYYY
# for example today is 30-04-2021; from_date = 30-04-2020 to_date = 30-04-2021
```

```python
from individual_company_stock import niftyHistoryData
niftyHistoryData('NIFTY 50') 
# Default params : from_date = today's date in last year DD-MM-(YYYY-1), to_date=today's date DD-MM-YYYY
# for example today is 30-04-2021; from_date = 30-04-2020 to_date = 30-04-2021
```