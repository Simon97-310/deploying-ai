from langchain.tools import tool
import json
import requests


@tool
def get_ex_rate(
        base_currency:str, 
        price_currency:str, 
        date:str = 'latest'
    ):
    """Output information about currency exchange rate

    Args:
        base_currency (str): currency code of base currency
        price_currency (str): currency code of price currency
        date (str): as of date of the information. Accepted value should either be 'latest' or a date value in 'YYYY-MM-DD' format. 

    Returns:
        _type_: str
    """
    base_currency_ex = f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{date}/v1/currencies/{base_currency}.json'
    response = requests.get(base_currency_ex)
    resp_dict = json.loads(response.text)
    ex_rate = resp_dict[base_currency][price_currency]

    date_str = 'Today' if date == 'latest' else f'on {date}'

    response_str = '\n'.join([f'Base Currency: {base_currency}\n', 
                             f'Price Currency: {price_currency}\n', 
                             f'Exchange Rate {date_str}: {ex_rate}'])
    
    
    return {
        "base_currency": base_currency,
        "price_currency": price_currency,
        "date": date_str,
        "exchange_rate": ex_rate
    }
