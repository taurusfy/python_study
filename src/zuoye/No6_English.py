#coding=utf-8
#!/usr/bin/env python
#支持英文
import os
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#d="E:\\A_WORK\\wordcloud_study\\"
#d = path.dirname(__file__)
d = os.getcwd()
#print d
# Read the whole text.
text = open(path.join(d,'a tale of two cities.txt')).read()

# read the mask / color image taken from
# http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010
alice_coloring = np.array(Image.open(path.join(d,"anne.png")))
stopwords = set(STOPWORDS)
stopwords.add("say")        #设置停止词
stopwords.add("said")
stopwords.add("yet")

wc = WordCloud( background_color="white",\
                max_words=2000,\
                mask=alice_coloring,\
                stopwords=stopwords,\
                max_font_size=40,\
                random_state=42)
# generate word cloud
wc.generate(text)

# create coloring from image
image_colors = ImageColorGenerator(alice_coloring)

# show
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.figure()
# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.figure()
plt.imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
plt.axis("off")
plt.show()

wc.to_file(path.join(d,"result_e.jpg"))
