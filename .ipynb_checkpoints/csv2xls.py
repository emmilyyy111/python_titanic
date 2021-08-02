import pandas as pd
import numpy as np

old = pd.read_csv('Ecommerce Customers')

new_file = pd.ExcelWriter('Ecommerce Customers.xlsx')

old.to_excel(new_file, index=False)

new_file.save()