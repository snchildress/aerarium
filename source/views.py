from django.http import HttpResponse
from datetime import date, timedelta
import requests

from source.models import Currency
from source import source_settings


### External functions

def home(request):
    update_currencies()
    return HttpResponse('Successfully updated yesterday\'s currencies!')

### Internal functions

def update_currencies():
    # Loops through all conversions in the database
    for currency in Currency.CURRENCY_TYPES:
        currency = currency[0] # Take first value in currency_type tuple
        convert_to_usd(currency)

def convert_to_usd(currency):
    # Writes conversion rate to USD for given currency to the database
    yesterday = date.today() - timedelta(1)
    currency_endpoint = source_settings.CURRENCY_ENDPOINTS['convert_to_usd'].format(yesterday, currency)
    response = requests.get(currency_endpoint).json()
    currency = response['base']
    conversion_rate = response['rates']['USD']
    conversion_rate_date = response['date']
    if conversion_rate_date == yesterday: # Prevents duplicate Friday data
        currency_record = Currency(
            currency=currency,
            conversion_rate=conversion_rate,
            conversion_rate_date=conversion_rate_date
        )
        currency_record.save()
