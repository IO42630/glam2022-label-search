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

    # See all the projects in the instance
    pprint(escr.get_projects())

    # Show our project
    project_pk = escr.get_project_pk_by_name(PROJECT_NAME)
    project = escr.get_project(project_pk)

    # Show the transcriptions for the document in our project that we
    # transcribed. One document = a collection of images. We uploaded 256
    # images from the ones that were likely related to Walo Koch.
    # The transcription info looks like this:
    #
    # [GetAbbreviatedTranscription(pk=8,
    #                              name='kraken:TREE',
    #                              archived=False,
    #                              avg_confidence=0.896720964857014),
    #  GetAbbreviatedTranscription(pk=9,
    #                              name='kraken:HTR-United-Manu_McFrench',
    #                              archived=False,
    #                              avg_confidence=0.939923500128904),
    #  GetAbbreviatedTranscription(pk=7,
    #                              name='manual',
    #                              archived=False,
    #                              avg_confidence=None)]
    transcriptions = escr.get_document_transcriptions(DOC_PK)
    pprint(transcriptions)

    # Show the lines from one document part (= one image). This image was
    # transcribed manually - we can see this because the lines that have a
    # transcription look like this, with "transcription=7":
    #
    #         transcriptions=[GetTranscription(pk=292,
    #                                          line=4751,
    #                                          transcription=7,
    #                                          content='Crepis praemorsa (L.) '
    #                                                  'Walther',
    #                                          versions=[],
    #                                          version_author='admin',
    #                                          version_source='eScriptorium',
    #                                          version_updated_at=datetime.datetime(2022, 11, 5, 13, 7, 58, 352529, tzinfo=datetime.timezone.utc),
    #                                          graphs=None,
    #                                          avg_confidence=None)])
    lines = escr.get_document_part(DOC_PK, 219).lines

    # Show the transcription content for each line in the image that has it:
    #
    # 'Crepis praemorsa (L.) Walther'
    # 'conf. Carmen Hiltebrand 2/2015'
    # 'verwendet für die Masterarbeit, 2014 (Z)'
    # 'BOTANISCHE SAMMLUNGEN DER EIDG. TECHNISCHE HOCH'
    # 'FLORA HELVETICA'
    # 'Crepis praemorsa (L.)Tausch'
    # 'Gem.: Oberbüren, unter Ebersol, Thur-Absturz'
    # 'östl.Kloster Glattbrugg'
    # 'Ep.SSW Mergel Steilhang 510-530 m'
    # 'Pinus silv.-Mol.-litoralis -Ass.'
    # '23.5.1950'
    # 'leg. Walo Koch'
    # '50/42'
    # 'BOTANISCHE SAMMLUNGEN'
    # 'der Eisgenössischen Technischen Hochschule'
    # '2361'
    # '905'
    print(len(lines))
    for line in lines:
        line_data = escr.get_document_part_line(DOC_PK, 219, line.pk)
        if len(line_data.transcriptions) > 0:
            for trans in line_data.transcriptions:
                pprint(trans.content)
