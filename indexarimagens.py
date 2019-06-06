import os
from os import listdir
from os.path import isfile, join
import sys
from elasticsearch import Elasticsearch
from image_match.elasticsearch_driver import SignatureES

es = Elasticsearch()
ses = SignatureES(es, index='amcomamil')

files = [file for file in listdir('ImagensOriginais') if isfile(join('ImagensOriginais', file))]

for f in files:
    file_path = os.path.abspath('ImagensOriginais/'+f)
    print('Indexando imagem ' + file_path)
    ses.add_image(file_path)