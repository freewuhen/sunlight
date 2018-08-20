from os import path
from PIL import Image
import numpy as np
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
def Pretreatment():
    with open("../resource/sunlight.txt","r") as readfile:
        with open("../resource/new.txt","at") as writefile:

            while True:
                line = readfile.readline()
                if line is '':
                    break
                else:
                    line = readfile.readline().replace("[表情]","").replace("[图片]","")
                    writefile.write(str(line))
                    line = readfile.readline()
            print("ok")

def sunlight():
    text = open("../resource/new.txt","r").read()
    worldlist = jieba.cut(text,cut_all=False, HMM=True)
    wl = "/".join(worldlist)
    print(wl)

    coloring = np.array(Image.open("../resource/SF.jpg"))
    wc = WordCloud(background_color="white", max_words=2000, mask=coloring,
                   max_font_size=50, random_state=42, font_path='../resource/simsun.ttf')
    wc.generate(wl)

    # create coloring from image
    image_colors = ImageColorGenerator(coloring)

    # show
    # 在只设置mask的情况下,你将会得到一个拥有图片形状的词云
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.figure()
    plt.show()
    wc.to_file("loveagin.png")
sunlight()
