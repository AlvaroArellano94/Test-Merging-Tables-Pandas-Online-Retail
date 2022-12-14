import pandas as pd
def get_online_retail_df() -> object:
    """
    This function is used to extract the data of the file "Online_Retail.xlsx". It returns a dataframe with this data.
    """
    ONLINE_RETAIL_FILE_NAME = "./data/Online_Retail.xlsx"
    df_online_retail = pd.read_excel(ONLINE_RETAIL_FILE_NAME)

    return df_online_retail

def get_unique_countries(df_online_retail: object) -> set:
    """
    This function needs as argument a dataframe of the "Online_Retail.xlsx".
    It returns a dataframe with a set of the "Iso2Code" of the countries that appears in the file.
    """
    set_countries_with_nan = set(df_online_retail['Iso2Code'])
    set_countries_without_nan = [x for x in set_countries_with_nan if str(x) != 'nan']
    return set_countries_without_nan

def get_mapping_ISO_2_table() -> object:
    """
    This function is used to extract the data of the file "ISO_Codes_2.csv". It returns a dataframe with this data.
    """
    ISO_2_MAPPING_TABLE = "./data/ISO_Codes_2.csv"
    df_iso_2_mapping_table = pd.read_csv(ISO_2_MAPPING_TABLE, sep=';')

    return df_iso_2_mapping_table