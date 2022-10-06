import requests  #pip install requests
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('API_KEY')

def get_response_api_bank_holidays(country_iso_2_name:str, year_num:int) -> dict:
    """
    This function needs two arguments: one as country and the other as the year. It returns a JSON with information of bank holidays from "Festivos" API.
    """
    url = f'https://api.getfestivo.com/v2/holidays?country={country_iso_2_name}&year={year_num}&api_key={API_KEY}'
    response = requests.get(url)
    json_response = response.json()

    return json_response

def get_bank_holidays_df_from_response(json_response:dict) -> object:
    """
    This function needs to pass as argument a dictionary and it returns a dataframe.
    """
    list_of_dates = []
    bank_holiday_list_info = json_response['holidays']
    for bank_date_info in bank_holiday_list_info:
            list_of_dates.append(bank_date_info['date'])

    data = {}
    data['BankHolidayDate'] = list_of_dates
    iso_2_code = json_response['query']['country']

    bank_holidays_country_df = pd.DataFrame(data)
    bank_holidays_country_df['Iso2Code']=iso_2_code
    bank_holidays_country_df['IsBankHoliday']=True
    return bank_holidays_country_df

def get_bank_holidays_from_response(json_response:dict) -> set: 
    """
    This function gets the response of "Festivos" API and returns a list of the bank holidays. Also, it removes duplicate dates. 
    """
    bank_holiday_list_info = json_response['holidays']
    bank_holiday_dates_temp = set()

    for bank_holiday in bank_holiday_list_info:
        bank_holiday_dates_temp.add(bank_holiday["date"])

    bank_holiday_dates = list(bank_holiday_dates_temp)
    return bank_holiday_dates