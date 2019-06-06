from elasticsearch import Elasticsearch
from image_match.elasticsearch_driver import SignatureES
import sys

file_path = str(sys.argv[1])

es = Elasticsearch()
ses = SignatureES(es, index='amcomamil')

result = ses.search_image(file_path, all_orientations=True)

with open('resultado.txt', 'w') as f:
    f.write(str(result))
    f.flush()