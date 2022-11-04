import os
import shutil

import pandas as pd
import openpyxl
import requests as requests

print(os.getcwd())
os.chdir('./data')

fileName = 'occurrence.csv'
data = pd.read_csv(fileName, sep='\t')
for x in data.values:
    print(x, x[12])
    url = x[12]
    res = requests.get(url, stream=True)
    if res.status_code == 200:
        with open(x[0] + '.jpg', 'wb') as f:
            shutil.copyfileobj(res.raw, f)
