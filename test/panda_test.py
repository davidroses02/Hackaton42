import pandas as pd
from openpyxl.workbook import Workbook
# module openpyxl is required to create a Excel file


# Create a Pandas dataframe from some data.
df = pd.DataFrame({'name': ['John', 'Mary'],
                     'location': ['New York', 'Paris']})
# create a Excel with to_excel() method
df.to_excel('pandas_simple.xlsx', sheet_name='test', index=False, engine='openpyxl')