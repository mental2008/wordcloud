from wordcloud import WordCloud
import numpy as np
import jieba
from PIL import Image
from scipy.misc import imread
import os
from os import path
import matplotlib.pyplot as plt

def draw_wordCloud():
    comment_text = open('text.txt', 'r').read()
    cut_text = "".join(jieba.cut(comment_text))
    color_mask = imread('a770e9a89504c1cfd3be62c3b6b3b2c6.jpg')
    temp_path = path.dirname(__file__)
    cloud = WordCloud(
        font_path = path.join(temp_path, 'font.ttf'),
        background_color = 'white',
        mask = color_mask,
        max_words = 2000,
        max_font_size = 80
    )
    word_cloud = cloud.generate(cut_text)
    word_cloud.to_file('result.jpg')
    os.startfile('result.jpg')
    # plt.imshow(word_cloud)
    # plt.axis('off')
    # plt.show()


def main():
    draw_wordCloud()

main()
