# coding: utf-8
from escriptorium_connector import EscriptoriumConnector
import os
from dotenv import load_dotenv
from pprint import pprint

# Hardcoding these for now
PROJECT_NAME = '1538_jpges_WALO_Tryagain'
DOC_NAME = 'PackageAfterPackage'
DOC_PK = 7


if __name__ == '__main__':
    load_dotenv()
    url = str(os.getenv('ESCRIPTORIUM_URL'))
    username = str(os.getenv('ESCRIPTORIUM_USERNAME'))
    password = str(os.getenv('ESCRIPTORIUM_PASSWORD'))
    escr = EscriptoriumConnector(url, username, password)

    # pprint(escr.get_projects())

    project_pk = escr.get_project_pk_by_name(PROJECT_NAME)
    project = escr.get_project(project_pk)

    transcriptions = escr.get_document_transcriptions(DOC_PK)
    for t in transcriptions:
        print(t)
