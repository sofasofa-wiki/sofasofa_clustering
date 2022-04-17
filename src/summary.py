import json
import os
from collections import defaultdict

from wordcloud import WordCloud, ImageColorGenerator
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image


path = '../data/sofasofa-data'

_g = defaultdict(list)
_inv_g = defaultdict(list)


def graph(id, tags):
    _g[id] = tags


def inv_graph():
    new_keys = []
    for v in _g.values():
        new_keys.extend(v)
    for k in new_keys:
        _inv_g[k] = []
    for k, v in _g.items():
        for el in v:
            _inv_g[el].append(k)


for _, _, c in os.walk(path):
    for name in c:
        if name != '.DS_Store':
            file_path = os.path.join(path, name)
            with open(file_path, 'r', encoding='utf-8') as fr:
                jdata = json.load(fr)
                graph(jdata['id'], jdata['tags'])

inv_graph()

summary1 = []
for k, v in _inv_g.items():
    summary1.append([k, len(v)])

tag_text = ' '.join([' '.join(el) for el in _g.values()])

img_mask = np.array(Image.open('../data/img/liening.png'))
image_colors = ImageColorGenerator(img_mask)
wc = WordCloud(collocations=False, font_path='/System/Library/Fonts/STHeiti Light.ttc',
               mask=img_mask, width=1400, height=1400, margin=2, background_color='white').generate(tag_text)

plt.figure(dpi=800)
plt.imshow(wc.recolor(color_func=image_colors), interpolation='bilinear')
plt.axis("off")
plt.savefig('../data/img/word_cloud_jogo.png')

plt.show()

