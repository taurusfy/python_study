#coding:utf-8
import os
import jieba #支持中文分词
import numpy as np
from PIL import Image
from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS

#d="E:\\A_WORK\\wordcloud_study\\"
d = os.getcwd()
abel_mask = np.array(Image.open(path.join(d,"anne.png")))
text_from_file_with_apath = open(path.join(d,'report.txt')).read()

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)
#my_wordcloud = WordCloud().generate(wl_space_split)
my_wordcloud = WordCloud(
            background_color='white',   
            mask = abel_mask,        
            max_words = 200,           
            stopwords = STOPWORDS,       
            font_path = path.join(d,'simhei.ttf'),
            max_font_size = 50,
            random_state = 30).generate(wl_space_split)

image_colors = ImageColorGenerator(abel_mask)
#my_wordcloud.recolor(color_func=image_colors)

plt.imshow(my_wordcloud, interpolation="bilinear")
plt.axis("off")
#plt.figure()
plt.show()

#写文件
my_wordcloud.to_file(path.join(d,"result_c.jpg"))
