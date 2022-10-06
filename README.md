# International Online Retailer's Transactions - Technical Test

### SETUP:

You need to have Python installed.

-(OPTIONAL)Virtualenv: 
    python3 -m venv venv
    (OPTIONAL) After, you will need to execute the next command:
    .\venv\Scripts\activate

After that, You will need to execute the next command:
```bash
pip3 install -r requirements.txt
```

-Permissions needed:
You need to have a file called ".env" that contains the variable "API_KEY" in order to be able to fetch the data. It is being this way in order to hide confidential information.
You can find an example of that ".env" file in the root directory of the project with the name ".env.example".

### SOURCE DATA:

All data used in the project can be found in "data" folder (except the information from the API).
"Online_Retail.xlsx": this is the dataset that has the transactions and the main information*. The dataset has been downloaded from: "https://archive.ics.uci.edu/ml/machine-learning-databases/00352/".
"ISO_Codes_2.csv": this is the file that containts information about countries and "ISO_2" codes. It is used as a mapping table. The mapping table has been downloaded from: "https://pkgstore.datahub.io/core/country-list/data_csv/data/d7c9d7cfb42cb69f4422dec222dbbaa8/data_csv.csv".

"API Festivos": from this API the project gets the information of bank holidays from each different country. The link is: "https://getfestivo.com/".**

*Some country names of the mapping table has been manually modified in order to match correctly.
**From "API Festivos" only can be retrieved data from the previous year. Also, It is mandatory to include both "year" and "Iso2country" filter. 

### SOLUTION:

The final solution it has been collected in the file: "df_online_retail_complete.csv" that can be found in the "data" folder. 