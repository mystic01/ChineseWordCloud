import jieba, codecs, sys, pandas
import numpy as np
from scipy.misc import imread
from wordcloud import WordCloud, ImageColorGenerator
from os import listdir
from os.path import isfile, join

from Reader import Reader

stopwords_filename = 'data/stopwords.txt'
font_filename = 'fonts/STFangSong.ttf'
template_dir = 'data/templates/'


def main(folder_path):
    stopwords = set([line.strip() for line in codecs.open(stopwords_filename, 'r', 'utf-8')])
    words = get_all_words(folder_path, stopwords)
    words_stat = classify_words(words)
    print('# of different words =', len(words_stat))
    save_image(words_stat)


def classify_words(words):
    words_df = pandas.DataFrame({'word': words})
    words_stat = words_df.groupby(by=['word'])['word'].agg({'number': np.size})
    words_stat = words_stat.reset_index().sort_values(by="number", ascending=False)
    return words_stat


def get_all_words(folder_path, stopwords):
    words = []
    for file in listdir(folder_path):
        print("analyze ", file, "...")
        ext_name = file.split(".")[-1]
        reader = Reader.get_reader(ext_name)
        content = reader.read(join(folder_path, file))
        words = classify_content(content, stopwords)
    return words


def save_image(words_stat):
    for file in listdir(template_dir):
        if file[-4:] != '.png' and file[-4:] != '.jpg':
            continue
        background_picture_filename = join(template_dir, file)
        if isfile(background_picture_filename):
            prefix = file.split('.')[0]

            bimg = imread(background_picture_filename)
            word_cloud = WordCloud(font_path=font_filename, background_color='white', mask=bimg, max_font_size=600,
                                   random_state=100)
            word_cloud = word_cloud.fit_words(dict(words_stat.head(4000).itertuples(index=False)))

            bimgColors = ImageColorGenerator(bimg)
            word_cloud.recolor(color_func=bimgColors)

            output_filename = prefix + '.png'

            print('Saving', output_filename)
            word_cloud.to_file(output_filename)


def classify_content(content, stopwords):
    segs = jieba.cut(content, cut_all=True)
    words = []
    for seg in segs:
        word = seg.strip().lower()
        if len(word) > 1 and word not in stopwords:
            words.append(word)
    return words


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('[usage] <input>')



