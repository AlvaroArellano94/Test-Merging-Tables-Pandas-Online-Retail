import pandas as pd
from extract_files import get_response_api_bank_holidays, get_bank_holidays_df_from_response
from extract_excel_file import get_online_retail_df, get_mapping_ISO_2_table, get_unique_countries

#Extraction of data sources:
#   -Extraction of "Online_Retail.xlsx file."
df_online_retail = get_online_retail_df()

#   -Extraction of mapping table "ISO_Codes_2.csv" 
df_iso_2_mapping_table = get_mapping_ISO_2_table()

#Add ISO_2 codes into the Online Reatil transactions dataframe    
df_online_reatil_with_iso_2 = pd.merge(df_online_retail, df_iso_2_mapping_table, how='left' ,left_on='Country', right_on='Name')

df_online_reatil_with_iso_2.rename(columns = {'Code':'Iso2Code'}, inplace=True)
df_online_reatil_with_iso_2.drop('Name', axis=1, inplace=True)
df_online_reatil_with_iso_2['InvoiceDateShort'] = df_online_reatil_with_iso_2['InvoiceDate'].dt.date

#   -Extraction of bank holidays using "Festivo" API
#   --First, it is needed to take a set of the countries we want to extract from the API
Iso_2_country_set = get_unique_countries(df_online_reatil_with_iso_2)

df_Bank_Holidays_API = pd.DataFrame(columns = ['Iso2Code', 'BankHolidayDate', 'IsBankHoliday'])
#Query the API for each Iso2Country
for Iso_2_country in Iso_2_country_set:
    json_bank_holiday_country = get_response_api_bank_holidays(Iso_2_country, 2021)

    one_Country_Bank_Holidays = get_bank_holidays_df_from_response(json_bank_holiday_country)

    increment_df = [df_Bank_Holidays_API, one_Country_Bank_Holidays]
    df_Bank_Holidays_API = pd.concat(increment_df)

df_Bank_Holidays_API_sel = df_Bank_Holidays_API[['Iso2Code','BankHolidayDate','IsBankHoliday']]

#Check Data
df_online_reatil_with_iso_2.to_csv('./data/data_to_left_join_1.csv')
df_Bank_Holidays_API_sel.to_csv('./data/data_to_left_join_2.csv')
load_1 = pd.read_csv('./data/data_to_left_join_1.csv')
load_2 = pd.read_csv('./data/data_to_left_join_2.csv')

#Include Bank Holidays into main table
df_online_retail_complete = pd.merge(load_1, load_2, how='left' ,left_on=['Iso2Code','InvoiceDateShort'], right_on=['Iso2Code','BankHolidayDate'])
del df_online_retail_complete['Unnamed: 0_x']
del df_online_retail_complete['Unnamed: 0_y']
del df_online_retail_complete['BankHolidayDate']

#dump into a csv file the result
df_online_retail_complete.to_csv('./data/df_online_retail_complete.csv')