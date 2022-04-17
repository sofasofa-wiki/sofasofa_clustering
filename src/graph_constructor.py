import json
import os

import networkx as nx


path = './data/sofasofa-data'


edges = []
for _, _, c in os.walk(path):
    for name in c:
        file_path = os.path.join(path, name)
        with open(file_path, 'r', encoding='utf-8') as fr:
            jdata = json.load(fr)
            for tag in jdata['tags']:
                edges.append((jdata['id'], tag))

edges = list(set(edges))

