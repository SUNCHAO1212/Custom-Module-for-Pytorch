
import re
import jieba
import os

jieba.load_userdict('userfiles/dict_catalog.txt')
jieba.load_userdict('userfiles/dict_entity1.txt')
jieba.load_userdict('userfiles/dict_pinpai.txt')


class DataProcessing:
    def __init__(self, cut_level='char'):
        self.cut_level = cut_level

    def clean_sent(self, sent):
        sent = re.sub('\t', '', sent)
        return sent

    def cut_sent(self, sent):
        if self.cut_level == 'word':
            sent = ' '.join(jieba.cut(sent.strip()))
        elif self.cut_level == 'char':
            this_list = []
            for word in sent.strip():
                this_list.append(word)
                sent = ' '.join(this_list)
        else:
            print("wrong parameter: 'cut_level'")
        return sent

    def dataset_file(self, input_file, output_file):
        with open(input_file) as f:
            with open(output_file, 'w') as fo:
                for line in f:
                    line = self.clean_sent(line)
                    line = self.cut_sent(line)
                    fo.write(line)
                    fo.write('\n')

    def dataset_dir(self, input_dir, output_dir):
        if not os.path.isdir(output_dir):
            os.makedirs(output_dir)
        for _, dirnames, filenames in os.walk(input_dir):
            for filename in filenames:
                input_path = input_dir + '/' + filename
                output_path = output_dir + '/' + filename
                self.dataset_file(input_path, output_path)
