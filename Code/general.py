import requests

session = requests.session()

head = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/87.0.4280.88 Safari/537.36 "
}


def getId(name):
    search_url = 'https://www.nseindia.com/api/search/autocomplete?q={}'
    get_details = 'https://www.nseindia.com/api/quote-equity?symbol={}'
    session.get('https://www.nseindia.com/', headers=head)
    search_results = session.get(url=search_url.format(name), headers=head)
    search_result = search_results.json()['symbols'][0]['symbol']

    company_details = session.get(url=get_details.format(search_result), headers=head)
    return company_details.json()['info']['identifier']

# getId('tata motors') => TATAMOTORSEQN