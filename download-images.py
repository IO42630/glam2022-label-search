import os
import shutil

import pandas as pd
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
#by the way for the linux user. Wget is already part of the system. You can use it to download files from the command line.
# For example:
# creat a csv only with the url
# got to the folder
# in the shell: wget -i filenname.csv

