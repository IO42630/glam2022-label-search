from escriptorium_connector import EscriptoriumConnector
import os
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    url = str(os.getenv('ESCRIPTORIUM_URL'))
    username = str(os.getenv('ESCRIPTORIUM_USERNAME'))
    password = str(os.getenv('ESCRIPTORIUM_PASSWORD'))
    escr = EscriptoriumConnector(url, username, password)
    print(escr.get_documents())
    escr.g
    br = 0
